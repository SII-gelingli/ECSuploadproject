#!/bin/bash
# Daemon script for Condition Agent Web UI
# Keeps the Gradio app running permanently with --share
# Automatically restarts on crash, logs output to daemon.log
#
# Usage:
#   ./run_daemon.sh start   # Start in background
#   ./run_daemon.sh stop    # Stop the daemon
#   ./run_daemon.sh status  # Check if running
#   ./run_daemon.sh restart # Restart

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PIDFILE="$SCRIPT_DIR/.daemon.pid"
LOGFILE="$SCRIPT_DIR/daemon.log"

: "${ANTHROPIC_API_KEY:?Please export ANTHROPIC_API_KEY before running (e.g. in ~/.bashrc)}"
export ANTHROPIC_API_KEY
export ANTHROPIC_BASE_URL="${ANTHROPIC_BASE_URL:-https://api.boyuerichdata.opensphereai.com}"
export ANTHROPIC_MODEL="${ANTHROPIC_MODEL:-claude-opus-4-6}"

start() {
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        echo "Daemon already running (PID $(cat "$PIDFILE"))"
        return 1
    fi
    echo "Starting daemon..."
    nohup "$SCRIPT_DIR/run_daemon.sh" _loop > /dev/null 2>&1 &
    echo $! > "$PIDFILE"
    echo "Daemon started (PID $!). Log: $LOGFILE"
    echo "Wait ~30s for the Gradio share link to appear in the log."
}

stop() {
    if [ ! -f "$PIDFILE" ]; then
        echo "No PID file found. Killing any web_app.py processes..."
        pkill -f "web_app.py --share" 2>/dev/null
        return
    fi
    PID=$(cat "$PIDFILE")
    echo "Stopping daemon (PID $PID) and child processes..."
    pkill -P "$PID" 2>/dev/null
    kill "$PID" 2>/dev/null
    pkill -f "web_app.py --share" 2>/dev/null
    rm -f "$PIDFILE"
    echo "Stopped."
}

status() {
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        echo "Daemon running (PID $(cat "$PIDFILE"))"
        grep -o 'https://[^ ]*gradio.live[^ ]*' "$LOGFILE" 2>/dev/null | tail -1 && true
    else
        echo "Daemon not running."
        pgrep -f "web_app.py" > /dev/null && echo "(web_app.py is running outside daemon)"
    fi
}

# Internal: the actual restart loop (called via nohup)
_loop() {
    while true; do
        echo "[$(date)] Starting web_app.py --share ..." >> "$LOGFILE"
        python -u "$SCRIPT_DIR/web_app.py" --share --port 7860 >> "$LOGFILE" 2>&1
        EXIT_CODE=$?
        echo "[$(date)] web_app.py exited with code $EXIT_CODE, restarting in 10s ..." >> "$LOGFILE"
        sleep 10
    done
}

case "${1:-status}" in
    start)   start ;;
    stop)    stop ;;
    restart) stop; sleep 2; start ;;
    status)  status ;;
    _loop)   _loop ;;
    *)       echo "Usage: $0 {start|stop|restart|status}" ;;
esac
