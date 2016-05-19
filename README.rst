=============
csvdb
=============

Csv reader like PEP 249 API.

Requirements
-----------------

- Python 3.x


Installation
-----------------

::

    $ pip install csvdb

Example
-----------------

::

   import csvdb
   conn = minitds.connect('/foo/bar/baz.csv')
   cur = conn.cursor()
   cur.execute('field1,field2')
   for r in cur.fetchall():
      print(r[0], r[1])
   conn.close()

