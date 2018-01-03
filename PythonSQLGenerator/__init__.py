"""
IDGFF License

Copyright (c) 2017 Tim Muzzin

The IDGFF License is a "I don't give a flying fuck" what you do with this code.
If it makes you a billionare, then pat yourself on the back and pour out a cold
one in my honor.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re


class PythonSQLGenerator():

    @staticmethod
    def insert(table, fields):
        """ Function for generating an SQL insert from a dict structure
        Args:
            table (str): The name of the table to be inserted into
            fields (dict): A dict that contains column names and the values to be inserted
        Returns:
            dictionary: returns a complete SQL string that can then be executed with parameter formatting.

            For example you can return the string and run a db execute.
            qry = PythonSQLGenerator.insert('my_table_name', my_dict)
            cursor.execute(qry['query'], qry['params'])
        """
        k = ""
        v = ()
        i = 0
        params = ""
        for key, val in fields.iteritems():
            i += 1
            k += "`" + key + "`"
            v = v + (val,)
            params += '%s'
            if i < len(fields):
                k += ", "
                params += ", "
        qry = {
            'query': "Insert Into " + table + " (%s) Values (%s);" % (k, params),
            'params': v
        }
        return qry


    @staticmethod
    def update(table, fields, where={}):
        """ Function for generating an SQL update from a dict structure
        Args:
            table (str): The name of the table to be updated
            fields (dict): A dict that contains column names and the values to be inserted
            where (dict): A dict that contains the where key and values
        Returns:
            string: returns a complete SQL string that can then be executed.

            For example you can return the string and run a db execute.
            qry = PythonSQLGenerator.update('my_table_name', my_dict, my_where_dict)
            cursor.execute(qry)
        """
        qry = ""
        i = 0
        #  loop through fields and set key and value string
        for key, val in fields.iteritems():
            i += 1
            if type(val) is str:
                qry += "`" + key + "`='" + val + "'"
            else:
                qry += "`" + key + "`=" + str(val)
            if i < len(fields):
                qry += ", "
        # if a where clause has been passed, loop through the where dict and set the key value string
        if len(where) > 0:
            i = 0
            qry += " where "
            for key, val in where.iteritems():
                i += 1
                qry += key + "='" + str(val) + "'"
                if i < len(where):
                    qry += " and "
        qry = "update " + table + " set %s;" % (qry)
        return qry


    @staticmethod
    def delete(table, where={}):
        """ Function for generating an SQL delete from a dict structure
        Args:
            table (str): The name of the table to be deleted from
            where (dict): A dict that contains the where key and values
        Returns:
            string: returns a complete SQL string that can then be executed.

            For example you can return the string and run a db execute.
            qry = PythonSQLGenerator.delete('my_table_name', my_where_dict)
            cursor.execute(qry)
        """
        qry = ""
        # if a where clause has been passed, loop through the where dict and set the key value string
        i = 0
        for key, val in where.iteritems():
            i += 1
            qry += key + "='" + str(val) + "'"
            if i < len(where):
                qry += " and "
        qry = "delete from " + table + " where %s;" % (qry)
        return qry
