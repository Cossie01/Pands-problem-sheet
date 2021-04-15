#Weekly Task 03
#A program that takes asks a user to input a string and outputs every second letter in reverse order.
#Author: Ciara O' Sullivan


#Testing
x = str(input("In one sentence, how is the recent lockdown going for you? ")) #getting input from the user
print(len(x))  #lenght of the sentence 
print (x[::2])  #getting every second letter 
print (x[::-2]) #getting it in reverse


y =input("Please copy this sentence: The quick brown fox jumps over the lazy dog") #asking the user to copy this sentence
print(y[::-2]) #using the above to get the final outcome of the sentence in reverse
