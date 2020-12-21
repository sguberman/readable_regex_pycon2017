"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path."""
    return re.search(r".(\w+)$", filename).group(1)


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    return re.findall(r"\b.*[aeiouAEIOU]{4}.*\b", dictionary)


def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    return re.findall(r"\b[a-fA-F]+\b", dictionary)


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    return re.findall(r"\b.*[^aeiouyAEIOUY]{6}.*\b", dictionary)


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    template = partial_word.replace('_', r'\w')
    return re.findall(r"\b" + template + r"\b", dictionary, re.IGNORECASE)


def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    template = r"\b(?:\w*" + letter + r"){5,}\w*\b"
    return re.findall(template, dictionary, re.IGNORECASE)


def abbreviate(phrase):
    """Return an acronym for the given phrase."""
    return ''.join(g0 if g0 else g1
                   for g0, g1 in re.findall(r"(\b\w)|([A-Z])\w*\b", phrase)
                   ).upper()


def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""
    return [m.group()
            for m in re.finditer(r"\b([a-z])([a-z])[a-z]\2\1\b",
                                 dictionary,
                                 re.IGNORECASE)]


def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """
    return [m.group()
            for m in re.finditer(r"\b\w*(\w)\1\w\1\1\w*\b",
                                 dictionary,
                                 re.IGNORECASE)]


def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
    return [m.group()
            for m in re.finditer(r"\b(\w+)\1\b",
                                 dictionary,
                                 re.IGNORECASE)]
