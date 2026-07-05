"""
Formatter untuk angka Indonesia.
"""


def format_number(number):
    """
    1234567 -> 1.234.567
    """

    try:
        return f"{int(number):,}".replace(",", ".")
    except Exception:
        return "0"


def format_percent(value):
    """
    4.234 -> 4.23%
    """

    try:
        return f"{value:.2f}%"
    except Exception:
        return "0.00%"


def format_currency(number):
    """
    Rp 1.234.567
    """

    try:
        return f"Rp {int(number):,}".replace(",", ".")
    except Exception:
        return "Rp 0"