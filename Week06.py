#week06-functions
#Week 6 - $ python squareroot.py
#Author: Ciara O Sullivan 
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

import math #importing a module/library 

def main(): #setting up the function
    a = float(input("Please enter a positive number: ")) #setting up the variable as the users input
    b = math.sqrt(a) #using the built in function and applying it to the first variable
    print (b) #printing the outcome

main() #calling the function


num = float(input("May I have a number please? ")) #ask for input and placing it as a float
num_Squared = num ** 0.5 #square root of a number is multiply itself or by half
print(" The answer is ", num_Squared) #final output