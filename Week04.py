#Week 4 - $ python collatz.py
#Author: Ciara O Sullivan 
#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation



def numberOne (number):     #makes the function
        
        if number % 2 == 0: #checking if the number is even 
                print(number//2)
                return number//2
            

        elif number %2 !=0:    #checking if the number is odd 
                result = (number*3 + 1)
                print(result)
                return result



try:
    n =input("Please enter a valid number!")     # getting input from the user and naming it n to store it in memory
    while n !=1:    #while loop, stays in loop until n becomes 1
        n= numberOne(int(n))   # once it becomes one it passes it into the function numberOne

except ValueError:
        print("Please enter a valid number!") #handles errors, should the user not put in a positive integer. Such as a letter or symbol




