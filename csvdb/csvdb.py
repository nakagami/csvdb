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
import io
import csv

VERSION = (0, 1, 0)
__version__ = '%s.%s.%s' % VERSION
apilevel = '2.0'

class Error(Exception):
    pass


class Cursor(object):
    def __init__(self, conn):
        self.conn = conn
        self._fieldnames = []
        self._reader = None

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
        self._fieldnames = query.split(',')
        if isinstance(self.conn._path, io.StringIO):
            self._stringio = self.conn._path
        else:
            self._stringio = open(self.conn._path, 'r', encoding=self.conn._encoding)
        self._header = self._stringio.readline().strip().split(',')
        self._reader = csv.DictReader(
            self._stringio,
            fieldnames=self._header,
            delimiter=self.conn._delimiter,
        )

    @property
    def description(self):
        return [(name, -1, -1, -1, -1, -1, name != self._header[0]) for name in self._fieldnames]

    def _fetchone(self):
        if self._reader is None:
            raise Error("Not call execute().")
        r = next(self._reader)
        return tuple([r.get(f) for f in self._fieldnames])

    def fetchone(self):
        try:
            return self._fetchone()
        except StopIteration:
            return None

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
        self._stringio.close()
        self._reader = None

    @property
    def rowcount(self):
        raise NotSupportedError()

    def __iter__(self):
        return self

    def __next__(self):
        r = self._fetchone()
        if not r:
            raise StopIteration()
        return r


class Connection(object):
    def __init__(self, path, encoding='utf-8', delimiter=','):
        self._path = path
        self._encoding = encoding
        self._delimiter = delimiter

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        self.close()

    def cursor(self):
        return Cursor(self)

    def close(self):
        pass

def connect(path, encoding='utf-8', delimiter=','):
    return Connection(path, encoding, delimiter)
