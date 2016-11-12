#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger docstring"""
    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Log docstring"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush docstring"""
        handled = []

        for index, entry in enumerate(self.msgs):
            try:
                fhandler = open(self.logfilename, 'a')
            except IOError:
                self.log(msg='IOError')
                raise IOError
            else:
                self.log(msg='Error')
                break
            finally:
                fhandler.close()
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
                for index in handled[::-1]:
                    del self.msgs[index]
            except IOError:
                self.log(msg='IOError')
                break
            finally:
                fhandler.close()
