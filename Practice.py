
# import matplotlib.pyplot as plt
# import mysql.connector
# import sqlite3
# import re
# import os  //(file handling)
# import pandas as pd
# import openpyxl

# To Install above :
#     pip install matplotlib
#     pip install mysql.connector
#     pip install openpyxl
#     pip install pandas
#     pip install panda




# 1. Create a database
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="")
# mycursor = mydb.cursor()
# mycursor.execute("Create database mypy")


# # 2.Create a Table:
# import mysql.connector
# mydb = mysql.connector.connect(host = "localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute("create table stud(roll int, name varchar(25))")
# print("Table Successfully created")

# 3.Inserting data into table
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost',user = "root",password="",database="mypy")
# mycursor = mydb.cursor()
# q = "Insert into stud(roll,name) values(%s,%s)"
# value = [(1,'milan'),(2,"prince")]
# mycursor.executemany(q,value)
# mydb.commit()
# print("Record inserted successfully")

# 4. Showing the data ffrom database
# import mysql.connector
# mydb = mysql.connector.connect(host = "localhost",user = "root", password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute("Select * from stud")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

# 5.Updating the database
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute("update stud set name = 'abc' where roll=2")
# mydb.commit()
# mydb.close()


# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute("delete from stud where roll = 2")
# mydb.commit()








# SQLLITE DATABASE CONNECTION

# import sqlite3
# cnt = sqlite3.connect('mypy.dp')
# # cnt.execute("Create table demo(roll int, name varchar(25))")
# # print("Table successfully created")
# cnt.execute("""Insert into demo(roll,name) values
#     (25,'sdhg'),(21,'dgff'),(256,'gdsg')""")
# cnt.commit()
# # print("Record inserted successfully")
# res = cnt.execute("select * from demo")
# for i in res:
#     print(i)
# cnt.execute("update demo set name = 'abd' where roll = 25")
# cnt.commit()
# print("Updated successfully")
# cnt.execute("delete from demo where roll = 25")
# cnt.commit()








# Graph

# import matplotlib.pyplot as plt
# year = (2020,2021,2022,2023,2024)
# data = (52,25,36,56,82)
# plt.bar(year,data,label="data chart",color="red")
# plt.xlabel("Years")
# plt.ylabel("Data")
# plt.legend()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import openpyxl
# df = pd.read_excel('Stud.xlsx')
# print(df)

# x=df['year']
# y = df['sale']
# plt.bar(x,y,label="Sales Report")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import openpyxl

# df = pd.read_excel('1.xlsx')
# # print(df)
# cars = df['cars']
# x = df['sales']
# plt.pie(x)
# plt.title("Tata Motor Cars Sales")
# plt.xlabel("Cars Sales")
# plt.legend()
# plt.show()


#Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.
# import matplotlib.pyplot as plt
# years = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
# bsc = [89,59,74,84,85,94,16,45,36,47]
# plt.plot(years,bsc,color='teal') 
# plt.title("Bombay Stock Exchange") 
# plt.xlabel('Years') 
# plt.ylabel('BSC')
# plt.legend() 
# plt.show()


# Take five income source of the Government and display it on the pie chart.
# import xlrd
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_excel('Government.xlsx') 
# print(df)
# x = df['source'] 
# y = df['amount']
# plt.bar(x,y,label="")
# plt.xlabel('Source') 
# plt.ylabel('Amount') 
# plt.title('Government Income') 
# plt.legend()
# plt.show()



