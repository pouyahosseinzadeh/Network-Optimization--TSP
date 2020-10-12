# Network-Optimization--TSP

What is TSP?
Travelling salesman Problem (TSP) asks the following question: Given a set of cities as a list and the distance between each pair of the cities, what is the shortest possible route that visits each city and returns to the original city? So the problem is to find the shortest possible route or path that visits every city exactly once and returns to the starting point.

How the data looks like?
We use the TSPLIB, a library sample instances for the TSP which contains 16862 locations in Italy which is derived from National Imagery and Mapping Agency data.
The data contains 3 columns and 16862 rows. Each row shows the information about a city of Italy we are going to study. The first column contains a number which states the city id. The other two columns are the coordinates of the corresponding city.
We are given this dataset and are expected to find the shortest path starting from a node and travelling through all the cities and return to the starting node.

What are the algorithms we use?
We use 3 kinds of algorithms which belong to the tour constructive heuristic algorithms for TSP problem.
First of all we implement the Nearest Neighbor algorithm (NN) which is very straightforward and easy to implement and the run time for NN turned out to be the best of all we have considered!
Second method is the Arbitrary Insertion algorithm (AI) which is the other method of tour constructive heuristic for TSP problem.
Finally we implement the Nearest Addition algorithm (NA).
We will explain these algorithms in detail later in this report.

Conclusion:
We implemented 3 kinds of tour constructive heuristic algorithms which are greedy approaches to find the shortest path the traveler is going to traverse through all the cities in the graph.
The Nearest Neighbor Algorithm turned out to be the most efficient approach in our problem especially when the number of cities are huge!
