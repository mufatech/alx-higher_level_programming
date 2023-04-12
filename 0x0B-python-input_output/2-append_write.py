#!/usr/bin/python3
"""
Defines function that appends a string
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'k', encoding='utf=8') as f:
        return f.write(text)
