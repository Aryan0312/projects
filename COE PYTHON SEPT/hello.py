import matplotlib.pyplot as plt
import numpy as np
# #basic plotting
# x= [1,2,3,4,5]
# y = [2,4,16,32,64]

# line graph

# plt.plot(x,y,color="green",marker="d",linestyle="--",linewidth=2)
# plt.title("Aryan awesomness chart")
# plt.xlabel("TIME IN YEARS")
# plt.ylabel("AWESOMENESS")
# plt.grid(True)
# plt.savefig("plot.png",dpi=400)
# plt.show()


# bar graph

# categories=["a","b","c","d","e","f"]
# values=[10,20,30,40,50,60]
# plt.bar(categories,values,color="blue")
# plt.title("bar chart")
# plt.savefig("bar.png",dpi=400)
# plt.show()



# histogram 


# data = np.random.randint(2010,2025,200)
# bins = np.arange(2010,2025,1)
# plt.hist(data,bins=bins,color="green",edgecolor="black")
# plt.title("fossil discoveries over the years")
# plt.xlabel("year")
# plt.ylabel("number of discoveries")
# plt.savefig("histogram.png",dpi=400)
# plt.show()


# pie chart
labels = ["GYM","MERN","GF","COLLEGE","MISC","EAT","SLEEP"]
sizes =[1.5,3.5,2,7.5,2,1.5,6]

color=["blue","green","pink","red","yellow","orange","grey"]

plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title("A day in my life")
plt.savefig("DAYINMYLIFE.png",dpi=800)
plt.show()