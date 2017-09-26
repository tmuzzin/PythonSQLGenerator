# PythonSQLGenerator
Simple Package for generating SQL from Dictionary Objects. Helpful when dealing with large tables with lots of fields.

Example Insert:
```python
import MySQLdb
from PythonSQLGenerator import PythonSQLGenerator

# Open database connection
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DB_NAME)
# prepare a cursor object using cursor() method
cursor = db.cursor()

my_field_dictionary = {
 'first_name': 'Joe'
}
#  returns SQL string execute.
qry = PythonSQLGenerator.insert('my_table_name', my_field_dictionary)
cursor.execute(qry)
```

Example Update:
```python
import MySQLdb
from PythonSQLGenerator import PythonSQLGenerator

# Open database connection
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DB_NAME)
# prepare a cursor object using cursor() method
cursor = db.cursor()

my_field_dictionary = {
 'last_name': 'Smith'
}
my_where_dictionary = {
  'id': 1
}
#  returns SQL string execute.
qry = PythonSQLGenerator.update('my_table_name', my_field_dictionary, my_where_dictionary)
cursor.execute(qry)
```


Example Delete:
```python
import MySQLdb
from PythonSQLGenerator import PythonSQLGenerator

# Open database connection
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DB_NAME)
# prepare a cursor object using cursor() method
cursor = db.cursor()

my_where_dictionary = {
  'id': 1
}
#  returns SQL string execute.
qry = PythonSQLGenerator.delete('my_table_name', my_where_dictionary)
cursor.execute(qry)
```
