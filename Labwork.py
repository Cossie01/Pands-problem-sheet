#testTypes lab
#Author: Ciara O' Sullivan


#lab2.3.1 Introduction to different types of Variables
a = 2 #int
b = 3.2 #float
c = True #bool
d = "My name is " #str
e = Friends = ["Kevin", "Karen", "Jim"] #list

print (type (a))
print (type (b))
print (type (c))
print (type (d))
print (type (e))


#lab2.3.2 Program to subtract from another

f = int(input("What age is Ted? ") )
print (f)

g = int(input ("What age is Paul? ") )
print (g)

h = (f-g)
print ("The calculation is ", h)

#lab2.3.2 Program to subtract from another
h = int(input("Please enter your first number?: "))
i = int(input("Please give me the number you wish to divide by: "))
j = (h/i)
print (j)

x = str(input("How is the recent lockdown going for you? "))

#Division - Roughwork

books = int(input("How many books do you want to read? "))
months = int(input("How many months do you think it will take to read? "))
perMonth = books/months
print ("You will read ", perMonth, "books per month. ")

#multi variables

k, l, m = "orange", "apple", "zest"
print(k)
print(l)
print (m)

#random function - gives back a random number between 1 and 10

import random
print(random.randrange(1,10))