import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
n = 20        #Population Count
m = 150       #Relationship Count
time = 0.08

dg = nx.DiGraph()
dg.add_nodes_from([1,2,3])
dg.add_weighted_edges_from([(1,2,1),(1,3,0.5)])
dg.add_node('a')
print dg.edge[1][2]['weight']
#nx.draw_networkx(dg,pos)
#plt.show()
