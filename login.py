import mysql.connector
from datetime import datetime

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Klienty@7322',
    database='login_zima'
)
my_cursor=db.cursor()

#my_cursor.execute("CREATE DATABASE login")

#my_cursor.execute("CREATE TABLE user_login (NAME VARCHAR(500) NOT NULL, PASSWORD VARCHAR(500) NOT NULL, EMAIL VARCHAR(500) NOT NULL, AGE smallint NOT NULL, DATE_CREATED datetime NOT NULL)")

#my_cursor.execute("ALTER TABLE user_login ADD COLUMN DATE_CREATED datetime NOT NULL")

'''my_cursor.execute("SELECT * FROM user_login")
for x in my_cursor:
    print(x)
    
    
#my_cursor.execute("INSERT INTO user_login (NAME, PASSWORD, EMAIL, AGE) VALUES (%s,%s,%s,%s)", ("your name", "@123Ab", "youremail@gmail.com", 45))
#db.commit()'''

name= input("Enter your name: ")
passwd= input("Enter a strong password: ")
email= input("enter your email address: ")
age= input('Enter your age: ')
print('Your information succesfully received')
my_cursor.execute("INSERT INTO user_login (NAME, PASSWORD, EMAIL, AGE, DATE_CREATED) VALUES (%s,%s,%s,%s,%s)", (name, passwd, email, age, datetime.now()))
db.commit()
#these lines of code are commented in order to avoid execution that may disrupt the menu app

my_cursor.execute("SELECT * FROM user_login")
