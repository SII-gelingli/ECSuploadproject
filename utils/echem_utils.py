"""
Electrochemical parameter parsing utilities.

Parse string-formatted electrochemical values (e.g., "40 mA", "8.3 mA/cm²", "3.0 V")
into numeric floats for use in ML models and experimental protocol estimation.
"""
import re
from typing import Optional


def parse_current_mA(s) -> Optional[float]:
    """
    Parse current strings into milliamperes.

    Examples:
        "40 mA" -> 40.0
        "10mA" -> 10.0
        "0.5 A" -> 500.0
        "2.0 mA" -> 2.0
    """
    if not s:
        return None
    s = str(s).strip()

    # Try mA first
    m = re.search(r'([\d.]+)\s*mA\b', s, re.IGNORECASE)
    if m:
        return float(m.group(1))

    # Try A (convert to mA)
    m = re.search(r'([\d.]+)\s*A\b', s)
    if m:
        return float(m.group(1)) * 1000.0

    # Try bare number (assume mA)
    m = re.match(r'^([\d.]+)$', s)
    if m:
        return float(m.group(1))

    return None


def parse_current_density_mA_cm2(s) -> Optional[float]:
    """
    Parse current density strings into mA/cm².

    Examples:
        "8.3 mA/cm²" -> 8.3
        "16.08 mA/cm2" -> 16.08
        "0.5 A/dm2" -> 5.0  (1 A/dm² = 10 mA/cm²)
        "5 mA cm-2" -> 5.0
    """
    if not s:
        return None
    s = str(s).strip()

    # mA/cm² variants
    m = re.search(r'([\d.]+)\s*mA\s*[/\s]?\s*cm[\u00b2²]?', s, re.IGNORECASE)
    if m:
        return float(m.group(1))

    # mA cm-2
    m = re.search(r'([\d.]+)\s*mA\s*cm\s*-\s*2', s, re.IGNORECASE)
    if m:
        return float(m.group(1))

    # A/dm² -> multiply by 10 to get mA/cm²
    m = re.search(r'([\d.]+)\s*A\s*[/\s]?\s*dm', s)
    if m:
        return float(m.group(1)) * 10.0

    # A/cm² -> multiply by 1000
    m = re.search(r'([\d.]+)\s*A\s*[/\s]?\s*cm', s)
    if m:
        return float(m.group(1)) * 1000.0

    return None


def parse_potential_V(s) -> Optional[float]:
    """
    Parse potential/voltage strings into Volts.

    Examples:
        "3.0 V" -> 3.0
        "1.8V" -> 1.8
        "2.9 V vs SCE" -> 2.9
        "-1.5 V" -> -1.5
    """
    if not s:
        return None
    s = str(s).strip()

    m = re.search(r'(-?[\d.]+)\s*V\b', s, re.IGNORECASE)
    if m:
        return float(m.group(1))

    return None


def parse_echem_params(echem_dict: dict) -> dict:
    """
    Parse all electrochemical parameters from a raw metadata dictionary.

    Args:
        echem_dict: Dict with string keys like 'current', 'current_density', 'potential'

    Returns:
        Dict with parsed numeric values (None if unparseable)
    """
    return {
        'current_mA': parse_current_mA(echem_dict.get('current')),
        'current_density_mA_cm2': parse_current_density_mA_cm2(echem_dict.get('current_density')),
        'potential_V': parse_potential_V(echem_dict.get('potential')),
    }
