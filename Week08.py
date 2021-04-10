#week08-Plotting & numpy
#Week 8 - $plottask.py 
#Author: Ciara O Sullivan 
#Write a program that displays a plot of the functions 


import matplotlib.pyplot as plt
import numpy as np 


#f(x)=x, g(x)=x2 and h(x)=x3 
#f =2, g = 4, h = 8

allTimes_x = [2,4,8] #creating values for the x axis
dev_y =[2, 3, 4] #creating values for the y axis
sec_y =[3,5,9] #creating second set of values for the y axis so we can compare

plt.plot(allTimes_x, dev_y, color ="m", linestyle="--", marker ="o", linewidth ="3") #asking the system to plot the both, making the line dash-dash and the colour purple
plt.plot(allTimes_x,sec_y, color ="#0040ff", marker= "s") #plotting the second values also adding square markers to this line, adding a certain hex colour. 

plt.title("My First Attempt at a Plot") #Naming the plot title

plt.xlabel("X-Label") #naming the x axis label
plt.ylabel ("Y-Label") #naming the y axis label
plt.legend(["Yesterday", "Today"]) #naming the legend of the two set of values

plt.grid(True) #creating a grid on the plot

plt.show() #asking for the program to show the plot visually

# plt.savefig("Plot.png") #saving your plotted figure to your computer


# ds.plot.scatter(x="A", y="B", hue="w", hue_style="discrete") 
