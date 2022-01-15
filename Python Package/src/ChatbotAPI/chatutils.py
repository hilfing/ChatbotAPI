from textblob import TextBlob

import errors

def correction(data):
    if not isinstance(data, str):
        raise errors.ArgumentError("No text input provided!")
    text = TextBlob(data)
    text = text.correct()
    return text

