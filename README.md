# PythonSQLGenerator
Simple Package for generating SQL from Dictionary Objects

Example Insert:
```python
import MySQLdb
from PythonSQLGenerator import PythonSQLGenerator

# Open database connection
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DB_NAME)
# prepare a cursor object using cursor() method
cursor = db.cursor()

#  returns SQL string execute.
qry = PythonSQLGenerator.insert('my_table_name', my_dict)
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

#  returns SQL string execute.
qry = PythonSQLGenerator.update('my_table_name', my_dict, my_where_dict)
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

#  returns SQL string execute.
qry = PythonSQLGenerator.delete('my_table_name', my_where_dict)
cursor.execute(qry)
```
