import re


class PythonSQLGenerator():
    
    @staticmethod
    def dict_to_insert(table, fields):
        """ Function for generating an SQL insert from a dict structure
        Args:
            table (str): The name of the table to be inserted into
            fields (dict): A dict that contains column names and the values to be inserted
        Returns:
            string: returns a complete SQL string that can then be executed.

            For example you can return the string and run a db execute.
            qry = DBTools.dict_to_insert('my_table_name', my_dict)
            cursor.execute(qry)
        """
        k = ""
        v = ""
        i = 0
        for key, val in fields.iteritems():
            i += 1
            k += "`" + key + "`"
            if type(val) == int:
                v += str(val)
            else:
                v += "'" + str(val) + "'"
            if i < len(fields):
                k += ", "
                v += ", "
        qry = "Insert Into " + table + " (%s) Values (%s);" % (k, v)
        return qry


    @staticmethod
    def dict_to_update(table, fields, where={}):
        """ Function for generating an SQL insert from a dict structure
        Args:
            table (str): The name of the table to be updated
            fields (dict): A dict that contains column names and the values to be inserted
            where (dict): A dict that contains the where key and values
        Returns:
            string: returns a complete SQL string that can then be executed.

            For example you can return the string and run a db execute.
            qry = DBTools.dict_to_update('my_table_name', my_dict, my_where_dict)
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
    def dict_to_delete(table, where={}):
        """ Function for generating an SQL insert from a dict structure
        Args:
            table (str): The name of the table to be deleted from
            where (dict): A dict that contains the where key and values
        Returns:
            string: returns a complete SQL string that can then be executed.

            For example you can return the string and run a db execute.
            qry = DBTools.dict_to_update('my_table_name', my_dict, my_where_dict)
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
