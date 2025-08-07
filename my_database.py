# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import pymysql
database = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Solokim059@",
)

# Prepare a cursor object
cursor_object = database.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE IF NOT EXISTS SKOON")
print("All Done!")