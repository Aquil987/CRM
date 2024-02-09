#Install Mysql in your computer
#Run this statements in terminal
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python


import mysql.connector
dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Jan@2024',
)

#create the cursor object
mycursor= dataBase.cursor()

#create the database
mycursor.execute("CREATE DATABASE elderco")

print("ALL Done")

#winpty manage.py createsuperuser