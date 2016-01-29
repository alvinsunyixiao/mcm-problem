import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
n = 20        #Population Count
m = 150       #Relationship Count
time = 0.08




dg = nx.DiGraph()
dg.add_nodes_from([1,2,3,4])
dg.add_edges_from([(1,2),(1,3),(4,1),(2,3)])
for n in dg:
    nodes = dg[n]
    print nodes
    for k in nodes:
        print k
    print ' '
nx.draw_networkx(dg)
#plt.show()