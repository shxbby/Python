Working with Python Tuples using Pandas
#Creating data frame from Tuples
stud=[(1,'abc','rajkot'), (2,'cde','surat'), (3,'efg','goa'), (4,'ghi','diu'), (5,'ijk','vadodara')]
import pandas as pd
df=pd.DataFrame(stud, columns=['roll','name','city'])
print(df)
#Creating data frame from Tuples
stud=[(1,'abc','rajkot'), (2,'cde','surat'), (3,'efg','goa'), (4,'ghi','diu'), (5,'ijk','vadodara')]
import pandas as pd
df=pd.DataFrame(stud, columns=['roll','name','city'])
print(df)
# Knowing number of rows and columns
print(df.shape)
#Display first five records
print(df.head())
#Display last five records
print(df.tail())
#Display first two records
print(df.head(2))
#Display last two records
print(df.tail(2))
#Retrieving range of rows
print(df[2:5])
#Retrieving data from columns
print(df[['name','city']])
#Finding Maximum values
print(df['roll'].max())
#Finding Minimum values
print(df['roll'].min())
#Display students who belongs to rajkot
print(df[df.city=='rajkot'])
#Display students whose roll is bigger than 2.
print(df[df.roll>2])
#Display students' name who belongs to rajkot
print(df[['name']][df.city=='rajkot'])



#------#Regular expression (also known as re)-------------

#str = r'm\w\w'
#r is for regular expression , rowstring
#m = first character must start with m
#\w = it means any alpha numeric character followed by m
# str1 = 'This will be printed on the \n new line'
# print(str1)
# str1 = r'This will be printed on the \n new line'
# print(str1)


# #Create a regular expression to search for string with 'm' a having total 3 character using findall()
# import re
# #str1 = input('Enter string:')
# str1 = 'net cat mat matter'
# result = re.findall(r'm\w\w\w',str1)
# print(result)
# #findall() returns always a list

# #Create a regular expression that represents a string with the new string
# import re
# str1 = 'AITS is the best Organization'
# print(str1)
# result = re.sub(r'AITS','Atmiya University',str1) #Use of sub()
# print(result)

# #Create a regular expression that finds the words strating with 's'
# import re
# str1 = 'Sun shines sooner or later'
# result = re.findall(r's[\w]*',str1)
# #result = re.findall(r's\w+',str1)
# print(result)

# #Create a regular expression that finds the words starting with a number
# import re
# str1 = 'The special classess are arranged on 11th and 21st of every month'
# result = re.findall(r'\d[\w]*',str1)
# print(result)

# #Create a regular expression that retrive the words having 5 characters.
# import re
# str1 = 'sun mon tues wedn thurs frida saturday'
# result = re.findall(r'\b\w{5}\b',str1)
# print(result)

# #Create a regular expression that retrive the words having 4 or 5 characters.
# import re
# str1 = 'sun mon tues wedn thurs frida saturday'
# result = re.findall(r'\b\w{4,5}\b',str1)
# print(result)

# #Create a regular expression that retrive the words having 4 or more than 4 and less than 7characters.
# import re
# str1 = 'sun mon tues wedn thurs friday saturday'
# result = re.findall(r'\b\w{4,6}\b',str1)
# print(result)

# #create aregular expression that retrive words having 2 or more than 2 and less than 6 cgharacters
# import re
# str1 = 'su mon tues wedn thurs friday saturday'
# result = re.findall(r'\b\w{2,6}\b',str1)
# print(result)

# #Create a regular expression that retrives only single digit number from the string
# import re
# str1 = 'seven eight 9 10'
# result = re.findall(r'\b\d\b',str1)
# print(result)

# #Create a regular expression which retrive last wor of the string if it strats with 's'
# import re
# str1 = 'seven eight nine seventeen'
# result = re.findall(r's[\w]*\Z',str1)
# print(result)