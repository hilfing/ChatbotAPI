# pylint: disable = C0114
# pylint: disable = E0401

"""
Basic utility functions for the bot
"""

from textblob import TextBlob

from .errors import ArgumentError


def correction(data):
    """Spellcheck"""
    if not isinstance(data, str):
        raise ArgumentError("No text input provided!")
    text = TextBlob(data)
    text = text.correct()
    return text
