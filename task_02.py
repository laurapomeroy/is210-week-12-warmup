#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """InvalidAgeError docstring"""
    pass


def get_age(birthyear):
    """Raise the manual exception

    Args:
        birthyears(number): a year

    Returns:
        age(number): a number

    Examples:

        >>> get_age(2099)

        Traceback (most recent call last):
          File "<pyshell#0>", line 1, in <module>
        get_age(2099)
          File "/home/vagrant/Desktop/is210-week-
          12-warmup/task_02.py", line 17, in get_age
        raise InvalidAgeError
        InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
