#!/usr/bin/python3

"""Append a string at the end of a txt file return the nb of char."""


def append_write(filename="", text=""):
    """append_write"""
    with open(filename, 'a', encoding='utf-8') as f:
        content = f.write(text)
        return content
