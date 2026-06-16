#!/usr/bin/env python3
"""
电化学反应产率预测与条件推荐系统
主入口脚本
"""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='电化学反应产率预测与条件推荐系统',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 训练产率预测模型
  python run.py train-yield

  # 训练条件推荐模型
  python run.py train-condition

  # 运行预测演示
  python run.py predict --demo

  # 批量预测
  python run.py predict --input reactions.json --output results.json
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # 训练产率模型
    train_yield_parser = subparsers.add_parser('train-yield', help='训练产率预测模型')
    train_yield_parser.add_argument('--config', default='configs/config.yaml', help='配置文件路径')
    train_yield_parser.add_argument('--device', default=None, help='设备 (cuda/cpu)')

    # 训练条件模型
    train_cond_parser = subparsers.add_parser('train-condition', help='训练条件推荐模型')
    train_cond_parser.add_argument('--config', default='configs/config.yaml', help='配置文件路径')

    # 训练 CVAE 条件模型
    train_cvae_parser = subparsers.add_parser('train-condition-cvae', help='训练CVAE条件推荐模型')
    train_cvae_parser.add_argument('--config', default='configs/config.yaml', help='配置文件路径')
    train_cvae_parser.add_argument('--epochs', type=int, default=60, help='训练轮数')
    train_cvae_parser.add_argument('--warmup_epochs', type=int, default=20, help='β warmup轮数')
    train_cvae_parser.add_argument('--beta_max', type=float, default=0.1, help='KL权重上限')

    # 预测
    predict_parser = subparsers.add_parser('predict', help='运行预测')
    predict_parser.add_argument('--demo', action='store_true', help='运行演示')
    predict_parser.add_argument('--input', type=str, help='输入JSON文件')
    predict_parser.add_argument('--output', type=str, help='输出JSON文件')
    predict_parser.add_argument('--yield-model', type=str, help='产率模型路径')
    predict_parser.add_argument('--condition-model', type=str, help='条件模型路径')

    args = parser.parse_args()

    project_root = Path(__file__).parent

    if args.command == 'train-yield':
        cmd = [sys.executable, str(project_root / 'scripts' / 'train.py'),
               '--config', args.config]
        if args.device:
            cmd.extend(['--device', args.device])
        subprocess.run(cmd)

    elif args.command == 'train-condition':
        cmd = [sys.executable, str(project_root / 'scripts' / 'train_condition.py'),
               '--config', args.config]
        subprocess.run(cmd)

    elif args.command == 'train-condition-cvae':
        cmd = [sys.executable, str(project_root / 'scripts' / 'train_condition_cvae.py'),
               '--config', args.config,
               '--epochs', str(args.epochs),
               '--warmup_epochs', str(args.warmup_epochs),
               '--beta_max', str(args.beta_max)]
        subprocess.run(cmd)

    elif args.command == 'predict':
        cmd = [sys.executable, str(project_root / 'scripts' / 'predict.py')]
        if args.demo:
            cmd.append('--demo')
        if args.input:
            cmd.extend(['--input', args.input])
        if args.output:
            cmd.extend(['--output', args.output])
        if args.yield_model:
            cmd.extend(['--yield-model', args.yield_model])
        if args.condition_model:
            cmd.extend(['--condition-model', args.condition_model])
        subprocess.run(cmd)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
