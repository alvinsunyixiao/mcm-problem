import networkx as nx
import matplotlib.pyplot as plt
dg = nx.DiGraph()
dg.add_nodes_from([1,2,3])
dg.add_edges_from([(1,2),(1,3),(2,3)])
nx.draw_networkx(dg)
plt.show()