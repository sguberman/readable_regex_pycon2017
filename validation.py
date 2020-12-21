"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re


def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r"[aeiouAEIOU]", string))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r"^-?[0-9]+$", string))


def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    return bool(re.search(r"^-?[0-9]+/[0-9]*[1-9]+[0-9]*$", string))


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    return bool(re.search(r"^\d{4}-(0[1-9]|1[012])-([012][0-9]|3[01])$", string))


def is_number(string):
    """Return True iff the string represents a decimal number."""
    return bool(re.search(r"^-?(\d+|\d+\.|\d*\.\d+)$", string))


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
    return bool(re.search(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$", string))
