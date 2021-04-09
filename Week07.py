#week07-Reading in files
#Week 7 - $ python es.py moby-dick.txt
#Author: Ciara O Sullivan 
#Write a program that reads in a text file and outputs the number of e's it contains.

import time #importing the time library, to allow time between the different parts, easier to read then as the user.

with open ('Dancing.txt', 'r') as f: #calls for the file
    file_Contents = f.read() #variable name is set up with the function to read the contents of the file
    print (file_Contents) #prints the contents of the file.

time.sleep(3) #delay of 3 secs

words =file_Contents.split() #process of observing all the words in the txt file and asigning it to the variable
print ('The Number of words in this certain text file: ', len(words)) #prints the outcome of the len of words ie the number of words in the file. 

time.sleep (2) #delay of 2 secs

occurance_Small = file_Contents.count("e") #counting the small letter 'e' in the txt file
print("This small letter occured",occurance_Small,"times!") #displaying how many times it actually occured.

time.sleep (2) #delay of 2 secs

occurance_Big = file_Contents.count("E") #counting the capital letter 'E' in the txt file
print("This big letter occured",occurance_Big,"times!") #displaying how many times it actually occured.

time.sleep (2)

print("Thank you!")