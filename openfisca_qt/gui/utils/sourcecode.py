# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 Pierre Raybaut
# Licensed under the terms of the MIT License
# (see spyderlib/__init__.py for details)

"""
Source code text utilities
"""

# Order is important:
EOL_CHARS = (("\r\n", 'nt'), ("\n", 'posix'), ("\r", 'mac'))

def get_eol_chars(text):
    """Get text EOL characters"""
    for eol_chars, _os_name in EOL_CHARS:
        if text.find(eol_chars) > -1:
            return eol_chars

def get_os_name_from_eol_chars(eol_chars):
    """Return OS name from EOL characters"""
    for chars, os_name in EOL_CHARS:
        if eol_chars == chars:
            return os_name

def get_eol_chars_from_os_name(os_name):
    """Return EOL characters from OS name"""
    for eol_chars, name in EOL_CHARS:
        if name == os_name:
            return eol_chars

def has_mixed_eol_chars(text):
    """Detect if text has mixed EOL characters"""
    eol_chars = get_eol_chars(text)
    if eol_chars is None:
        return False
    correct_text = eol_chars.join((text+eol_chars).splitlines())
    return repr(correct_text) != repr(text)

def fix_indentation(text):
    """Replace tabs by spaces"""
    return text.replace('\t', ' '*4)


def is_builtin(text):
    """Test if passed string is the name of a Python builtin object"""
    import __builtin__
    return text in [str(name) for name in dir(__builtin__)
                    if not name.startswith('_')]

def is_keyword(text):
    """Test if passed string is the name of a Python keyword"""
    import keyword
    return text in keyword.kwlist
