#Week 5 - $ python collatz.py
#Author: Ciara O Sullivan 
#Write a program whether or not today is a weekday.

import datetime #importing the module
import calendar #importing the module
todaysDate = datetime.datetime.today() #defining the variable
print(todaysDate) #prints todays date

today = todaysDate.isoweekday() #using the iso week that starts Monday as 1 up to Sunday 6

#td = input("what day is it? ")

if today <= 5: #if todays day is less or equal to five 
 print ("Yes today is a weekday! Nearly there.") #it will print this
else:  #or else it will print the below
    print ("Yay, it's the weekend!!!!")


#print (td.isoweekday()) #Monday 1 Sunday 7 #helps make sense of the what number corrilates with which day. 



#asking the user for input 
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #defining the variable weekday in a list 
weekend = ["Saturday", "Sunday"]#defining the variable weekday in a list 

response =input("What day is it today?")   #asking the user for input

if response == weekday:  #if statement, checking if the response is equal to weekend
    print ("Yes today is a weekday! Nearly there.") #if true prints whats in the brackets

else:  #if not true, will print the below
    print ("Yay, it's the weekend!!!!")

