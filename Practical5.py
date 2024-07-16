
# 1. Create a list containing several strings. Take input from the user (search string); display whether 
# entered string is available in the list or not.

# lst = ['Khan','Vishal','Milan','Jeet']

# search=input('Enter a value to search from the list : ')

# if search in lst:
#     print('The search value present in list ',lst)
# else:
#     print('The search value is not available in list ')



# #2. Accept the string from the user; display the message whether the entered string is palindrome 
# #or not.

# str=input('Enter a string ')

# str1=str[-1::-1]

# if str1 == str:
#     print('string is palindrome')
# else:
#     print('The string not palindrome')



# #3. Accept the string from the user; display the string in the reverse order.

# str=input('Enter any string value : ')
# print('The value of the string  is : ',str)
# str1=str[-1::-1]
# print('The value of the reversed string  is : ',str1)


# # 4. Accept the string from the user; allow user to choose from the following options and perform 
# # the task as per users choice. i). Convert to the upper case, ii). Convert to the lower case, iii). 
# # Convert to the swap case, iv). Convert to the title case

# str=input('Enter a string value : ')
# print('Press 1 to convert string to uppercase')
# print('Press 2 to convert string to lowercase')
# print('Press 3 to convert string to swapcase')
# print('Press 4 to convert string to titlecase')

# num=int(input('Enter value here : '))

# if num==1:
#     print(str.upper())
# elif num==2:
#     print(str.lower())
# elif num==3:
#     print(str.swapcase())
# elif num==4:
#     print(str.title())
# else:
#     print('invalid input')


# #5. Allow users to enter multiple strings in the list; arrange the entered string into alphabetical 
# #order and display.
# for()
# lst=[]
# Nolst=int(input('Enter number of string you want to enter : '))
# for i in range(Nolst):
#     lst.append(input('Enter the value of string : '))
# print(lst)
# print(sorted(lst))


# #6. Create a tuple and display it. Enter 25 at the third position and display it again

# tpl=(1,2,34)
# print(tpl)
# l=list(tpl)
# l[2]=25
# tpl=tuple(l)
# print(tpl)


# # 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).

# library={'BookId':7,'Title':'The Invisible Man','Author':'H.G. Wells','Price':2000,'Publisher':'C. Arthur Pearson '}

# # a) Display the dictionary
# print(library)

# # b) Display the name of Author
# print('The name of the author is : ',library['Author'])

# # c)Display the Bookid
# print('The book id is : ',library['BookId'])

# # d) Display the length of the dictionary
# print('The length of the dictionary is : ',len(library))

# # e) Update the price
# library['Price']=4900
# print('The renewed price is : ',library['Price'])

# # f) Insert year as the new key and display the dictionary again.
# library['Year']=2001
# print('The updated library is : ',library)
    

# # 8. Create a numeric array and perform following operations on it:

# from numpy import *
# # 1) Add 2 to each elements
# ar=array([34,56,67,3,33,4])
# print(ar)
# nar=[i+2 for i in ar]
# print('After Addition with 2 : ',nar)

# # 2)Subtract 3 from each element
# from numpy import *
# ar=array([34,56,67,3,33,4])
# print(ar)
# nar=[i-3 for i in ar]
# print('After subraction with 3 : ',nar)
    
# # 3) Multiply each element with 3
# from numpy import *
# ar=array([34,56,67,3,33,4])
# print(ar)
# nar=[i*3 for i in ar]
# print('After multiplication with 3 : ',nar)

# # 4)Divide each element by 2
# from numpy import *
# ar=array([34,56,67,3,33,4])
# print(ar)
# nar=[i/2 for i in ar]
# print('After division with 2 : ',nar)

# # 5) max and min
# from numpy import *
# ar=array([34,56,67,3,33,4])
# print(ar)
# print('The maximum element from the array is : ',max(ar))
# print('The minimum element from the array is : ',min(ar))

# # 6) find the average of all elements.
# from numpy import *
# ar=array([34,56,67,3,33,4])
# print(ar)
# print('The average of the array is : ',average(ar))



# # 9. Create a numeric array and do the following: append the element, pop the element, insert an 
# # element at the desired postion, reverse the elements in the array, convert the array to list.

# from array import *
# ar=array('i',[4,56,98,4,5,77,32])
# print(ar)

# # append the element
# ar.append(4)
# print('After appending the element : ',ar)

# # pop the element
# ar.pop(1)
# print('After removing the element : ',ar)

# # insert an element at the desired postion
# ar.insert(2,23)
# print('After inserting the elemtnt : ',ar)

# # reverse the elements in the array
# ar.reverse()
# print('After reversing the array : ',ar)

# # convert the array to list
# lst = list(ar)
# print('Converted into the list : ',lst)



# # 10. Accept numeric elements from the user, store it to the array and display. Ask user to enter
# #search element. Display the position of the searched element.
# from array import*
# ar=array('i',[])
# no=int(input('Enter number of elements you want to enter'))
# for i in range(no):
#     ar.append(int(input('Enter any value : ')))
# x=int(input('Enter value to search in element : '))

# for i in range(no):
#     if ar[i]==x:
#         print('The element is present in the array at position : ',i,'And the value is : ',ar[i])


# # 11. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each 
# # array and display only the bigger number.
# from numpy import *
# ar1=array([2,45,634,4,5])
# ar2=array([23,2,33,12,39])
# print(fmax(ar1,ar2))



# # 12. Accept dimension of the array and its values from the user, create an array as desired.
# from numpy import *
# no=int(input('Enter number of dimensional array you want to create : '))

# # 13. Create a function to calculate the simple interest.
# def simpleInterest(p,r,n):
#     si=(p*r*n)/100
#     return si
# print('The simple interest of the  given data is : ',simpleInterest(1000,5,1))


# # 14. Create a function to perform basic arithmetic operations on the number.

# def arithmatic(a,b):
#     print('Addition is : ',a+b)
#     print('Subtraction is : ',a-b)
#     print('Multiplication is : ',a*b)
#     print('Division is : ',a/b)
# arithmatic(10,5)


# # 15. Accept multiple strings and store it into the list using function.

# def lste(no):
#     lst=[]
#     for i in range(no):
#        lst.append(input('Enter value of string : '))
#     print(lst)

# no=int(input('Enter number of strings you want to insert : '))
# lste(no)


# # 16. Find the biggest number from three values using lambda.
# big= lambda a,b,c:max(a,b,c)
# print(big(9,4,5))

# #17. Demonstrate the use of:  and ii). pass.
# i). break
# n=5
# for i in range(n):
#     if i==3:
#         break # this will break the loop when the conditon is true
#     else:
#         print(i)


# ii). pass
# n=5
# for i in range(n):
#     if i==3:
#         pass # this will pass the current element from the loop
#     else:
#         print(i)


import matplotlib.pyplot as plt
# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
# Create bar chart
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()

