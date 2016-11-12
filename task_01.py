#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Exception handling to a function that already exists.

    Args:
        var1(any): any type
        var2(any): any type

    Return:
        var1[var2]: attempts to access any index or key of var1 that
        do not exist will print a warning message and return var1.

    Example:
        >>> simple_lookup([1, 2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        var1[var2]
    except(IndexError, KeyError):
        print "Warning: Your index/key doesn't exist."
        return var1
