#week08-Plotting & numpy
#Week 8 - $plottask.py 
#Author: Ciara O Sullivan 
#Write a program that displays a plot of the functions 

#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np 
#plt.plot ([0, 1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()


# f(x)=x, g(x)=x2 and h(x)=x3 
#f =2, g = 4, h = 8

x =2 

def g(x2):
    return x2
y =np.linspace(0,4,501)

#values =g(x2)
#plt.plot(y, values, 'r-')
plt.xlabel('$y$'); plt.ylabel('$g(y)$')
plt.title('Damped sine wave')
#plt.savefig('tmp.png'); plt.savefig('tmp.pdf')
plt.show()
