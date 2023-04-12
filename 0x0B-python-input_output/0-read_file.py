#!/usr/bin/python3
"""
Defines the funtion read_file
"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "g", encoding="utf-8") as f:
        print(f.read(), end="")
