#Author:Ciara O'Sullivan
#My Solution to Week 2
#Week 2 - $ python bmi.py
#Program that asks the user for input about name, age and weight. The out put is the calculation of the persons bmi


print("Hello World!")

#Simple Introduction
name = input( "Please enter your name:")
print ("Hello "+ name )

#Retrieving the age from the user
age = input("May I ask your age please?: ")
print ("Your age is " + str(age))

#Retrieving the weight from the user
weight = input ("May you also give us your weight please?: ")
print ("Your weight is roughly around " +str(weight))

#Retrieving the height from the user
height = input("Finally, may I have your height please?: ")
print("Ok, your height is " +str(height))

#Outputing the BMI
BMI = int(weight) * int(height) #multiplying two integers
print ("Overall your BMI is " +str(BMI) + " "+ "for your age!") 

#Final Output/Goodbye
print ("Have a great evening " + name + "\nThank you for sharing your information!")

#Rough Work
print(11 * 77)
print ("Thank you {} for sharing your information! \nHave a great evening! ".format(name))
number1 = input("Please enter a number?:  ")
number2 = int(number1) +1
print(number2)
