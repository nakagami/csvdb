#!/usr/bin/env python3
##############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2016 Hajime Nakagami
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##############################################################################
# https://github.com/nakagami/csvdb/
import csv

VERSION = (0, 1, 0)
__version__ = '%s.%s.%s' % VERSION
apilevel = '2.0'


class Cursor(object):
    def __init__(self, csv):
        self.csv = csv

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        self.close()

    def callproc(self, procname, args=()):
        raise NotSupportedError()

    def nextset(self, procname, args=()):
        raise NotSupportedError()

    def setinputsizes(sizes):
        pass

    def setoutputsize(size, column=None):
        pass

    def execute(self, query):
        self.fieldnames = query.split(',')
        self.description = [(name, -1, -1, -1, -1, -1, False) for name in self.fieldnames]
        # TODO: csvreader

    def fetchone(self):
        # TODO:
        pass

    def fetchmany(self, size=1):
        rs = []
        for i in range(size):
            r = self.fetchone()
            if not r:
                break
            rs.append(r)
        return rs

    def fetchall(self):
        return list(self)

    def close(self):
        # TODO:
        pass

    @property
    def rowcount(self):
        raise NotSupportedError()

    def __iter__(self):
        return self

    def __next__(self):
        r = self.fetchone()
        if not r:
            raise StopIteration()
        return r


class Connection(object):
    def __init__(self, fname, enc='utf-8', delimiter=',')
        self.reader = csv.DictReader(csvfile)
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        self.close()

    def cursor(self):
        return Cursor(self)

    def close(self):
        # TODO:
        pass
