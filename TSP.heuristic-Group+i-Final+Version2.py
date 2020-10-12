
# coding: utf-8

# In[1]:


# Group i
# a family of Tour Constructive Heuristic for TSP

# beginning of the codes


# In[ ]:


# this gives the user a better view of what she/he wants to do...
# A window as a user interface comes up as soon as you run the code :)
from tkinter import *
class Demo:
    def __init__(self, top):
        self.name=""
        frame_e = Frame(top)
        frame_e.pack()
        self.t_name = StringVar()
        back = Frame(frame_e, width=500, height=500, bg='black')
        back.pack()
        text = Entry(frame_e, textvariable=self.t_name, bg="white", width=70)
        text.pack()
        text.focus_force()
        myButton = Button(root, text="Enter Your Algorithm and click the button :) \n Options:\n NN...Nearest Neighbor\nAI... Arbitrary Insertion\n NA... Nearest Addition \nALL  ...     All of them! ", command=self.Naming)
        myButton.pack()


    def Naming(self):
        self.name = self.t_name.get()
        print(self.name)
        root.destroy()
    
root = Tk()
root.geometry=("100x100+100+50")
D=Demo(root)
root.mainloop()
alg = D.name
print(alg)


# In[ ]:


# importing the libraries we are going to use during the project.. for calculating, visualization stuffs, etc.
import math
import time
import networkx as nx
import matplotlib.pyplot as plt


# In[ ]:


# creating a class called City which includes city number, and two x and y coordinates for each city
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x/1000
        self.y = y/1000
    def printCity (self):
        print (self.id, self.x, self.y)


# In[ ]:


# getting data fron input text file
inputfilename = "D:\\DRIVE D\\daneshgah.arshad\\UNISIENA\\Network Optimization\\our final projects\\tsp-data.txt"
cities = []
G=nx.Graph()
with open(inputfilename, "r") as file_input:
    for line in file_input:
        str_city = line.split()
        cities.append(City(int(str_city[0]),float(str_city[1]), float(str_city[2])))
        G.add_node(int((str_city[0])), pos=((float(str_city[1])),(float(str_city[2]))))

for val in cities:
    val.printCity()


# In[ ]:


# Showing the graph of our problem
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels = True)
print("plotting the graph...")
plt.show()


# In[ ]:


# calculating the distance between two cities given their coordinates!
def getDistance(city1, city2):
    distance = (math.sqrt(pow(((city1.x) - (city2.x)), 2) + pow(((city1.y) -(city2.y)), 2)))
    return distance


# In[ ]:


# go through all the cities in path and then add the distance between the last visited city and the first one
def getTotalDistance(path):
    totalDistance = 0
    for i in range(0, len(path) - 1):
        totalDistance += getDistance(path[i], path[i + 1])
    totalDistance += getDistance(path[len(path) - 1], path[0])
    return totalDistance


# In[ ]:


# plotting the final path the traveller is going to travel..
# It gets the path and plots it according to its coordinates x and y
def plotTour(path):
    x = []; y = []
    for i in range(len(path)):
        x.append(path[i].x)
        y.append(path[i].y)
    x.append(path[0].x)
    y.append(path[0].y)
    plt.figure(figsize=(16,10))
    plt.plot(x,y,'ko-')
    for i in range(len(path)):
        plt.plot(x[i],y[i],'bo')
    plt.plot(x[0],y[0],'rs')
    plt.grid()    
    plt.show()


# In[ ]:


# here we get the path and print the cities the traveller must visit according to the path
def showPath(path):
    for i in range(len(path)):
        print(path[i].id)


# In[ ]:


# nearest neighbor algorithm... 
def nearestNeighbor(availableCities):
    print("running the Nearest Neighbor algorithm...")
    global startingTime_NN
    startingTime_NN = time.time()
    # to keep availableCities unchanged inside the function 
    TemporaryCities = availableCities.copy()
    path = []
    currentCity = TemporaryCities.pop()
    path.append(currentCity)
    # go through cities in availableCity until it's empty
    while (TemporaryCities):
        # set minDistance to infinite number
        minDistance = float("inf")
        # go through available city list to find the nearest city
        for i in TemporaryCities:
            # calculating the distance between cities
            newDistance = getDistance(currentCity, i)
            if newDistance < minDistance:
                minDistance = newDistance
                nextCity = i 
        # we set the current city to nextCity, so the next city will be city i
        currentCity = nextCity
        path.append(currentCity)
        TemporaryCities.remove(currentCity)
    return path


# In[ ]:


# arbitrary insertion algorithm... 
def arbitratyInsertion(availableCities):
    print("running the Arbitrary Insertion algorithm...")
    global startingTime_AI
    startingTime_AI = time.time()
    # to keep availableCities unchanged inside the function
    TemporaryCities = availableCities.copy()
    path = []
    currentCity = TemporaryCities.pop()
    path.append(currentCity)
    # go through cities in availableCity until it's empty
    while (TemporaryCities):
        # set minDistance to infinite number
        minDistance = float("inf")
        # # go through available city list to find the nearest city
        for i in TemporaryCities:
            # calculating the distance between cities
            newDistance = getDistance(currentCity, i)
            for j in path:
                minDistance1 = getDistance(i, j)
                if minDistance1 < minDistance:
                    myval = 0
                    minDistance = minDistance1
                    nextCity2 = i
            if newDistance < minDistance:
                myval = 1
                minDistance = newDistance
                nextCity = i
        if myval == 0:
            firstCity = nextCity2
            path.insert(0, firstCity)
            TemporaryCities.remove(firstCity)

        else:
            currentCity = nextCity
            path.append(currentCity)
            TemporaryCities.remove(currentCity)
            
    return path


# In[ ]:


# nearest addition algorithm...
def nearestAddition(availableCities):
    print("running the Nearest Addition algorithm...")
    global startingTime_NA
    startingTime_NA = time.time()
    # to keep availableCities unchanged inside the function 
    TemporaryCities = availableCities.copy()
    path = []
    currentCity = TemporaryCities.pop()
    path.append(currentCity)
    # go through cities in availableCity until it's empty
    while (TemporaryCities):
        # set minDistance to infinite number
        minDistance = float("inf")
        # loop through available city list to find the nearest city
        for i in TemporaryCities:
            # calculating the distance between cities
            newDistance = getDistance(currentCity, i)
            for j in path:
                minDistance1 = getDistance(i, j)
                newDistance2 = newDistance + minDistance1
                if newDistance2 < minDistance:
                    myval = 0
                    minDistance = newDistance2
                    nextCity2 = i
            if newDistance < minDistance:
                minDistance = newDistance
                nextCity = i
                
        if myval == 0:
                firstCity = nextCity2
                path.insert(0, firstCity)
                TemporaryCities.remove(firstCity)

        else:
                currentCity = nextCity
                path.append(currentCity)
                TemporaryCities.remove(currentCity)

            
    return path


# In[ ]:


if alg == "NN" or alg == "ALL":
    path_NN = nearestNeighbor(cities)
    totalDistance_NN = getTotalDistance(path_NN)
    runningTime_NN = time.time() - startingTime_NN
    if (len(cities) == len(set(path_NN))):
        print("Tour validity:   ACCEPTED")
    else:
        print("Tour validity:   REJECTED")
    print("Total distance:   %s" % str(totalDistance_NN))
    print("Running time:   %.2f seconds" % runningTime_NN)
    plotTour(path_NN)

else:
    print("No info")


# In[ ]:


# print all valid cities we are travelling according to the path computed by the algorithm
if alg == "NN" or alg == "ALL":
    showPath(path_NN)
else:
    print("No info")


# In[ ]:


if alg == "AI" or alg == "ALL":
    path_AI = arbitratyInsertion(cities)
    totalDistance_AI = getTotalDistance(path_AI)
    runningTime_AI = time.time() - startingTime_AI
    if (len(cities) == len(set(path_AI))):
        print("Tour validity:   ACCEPTED")
    else:
        print("Tour validity:   REJECTED")
    print("Total distance:   %s" % str(totalDistance_AI))
    print("Running time:   %.2f seconds" % runningTime_AI)
    plotTour(path_AI)

else:
    print("No info")


# In[ ]:


# print all valid cities we are travelling according to the path computed by the algorithm
if alg == "AI" or alg == "ALL":
    showPath(path_AI)
else:
    print("No info")


# In[ ]:


if alg == "NA" or alg == "ALL":
    path_NA = nearestAddition(cities)
    totalDistance_NA = getTotalDistance(path_NA)
    runningTime_NA = time.time() - startingTime_NA
    if (len(cities) == len(set(path_NA))):
        print("Tour validity:   ACCEPTED")
    else:
        print("Tour validity:   REJECTED")
    print("Total distance:   %s" % str(totalDistance_NA))
    print("Running time:   %.2f seconds" % runningTime_NA)
    plotTour(path_NA)

else:
    print("No info")


# In[ ]:


# print all valid cities we are travelling according to the path computed by the algorithm
if alg == "NA" or alg == "ALL":
    showPath(path_NA)
else:
    print("No info")


# In[ ]:


# Comparison between the algorithms
print("Here you can see the table which gives you the comparison between the performance of the Algorithms you chose!\n")
print('\033[94m' + '\033[1m' + '\033[4m' + 
      '---Algorithm---             ',      '---Total Distance---      ',            '---Running Time--- '+ '\033[0m')
if alg == "NN" or alg == "ALL":
    print('\033[4m'
              "1) Nearest Neighbour                %.2f" % totalDistance_NN,        "                %.2f seconds" % runningTime_NN)
if alg == "AI" or alg == "ALL":
    print('\033[4m'
              "2) Arbitrary Insertion              %.2f" % totalDistance_AI,        "                %.2f seconds" % runningTime_AI)
if alg == "NA" or alg == "ALL":
    print('\033[4m'
              "3) Nearest Addition                 %.2f" % totalDistance_NA,        "                %.2f seconds" % runningTime_NA)

