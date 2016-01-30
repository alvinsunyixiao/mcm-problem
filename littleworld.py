import networkx as nx
import random
import numpy
import matplotlib.pyplot as plt

total = 1000
def creatSmallWorld(randlink):
    dg = nx.DiGraph()
    node = []
    for i in range(1000):
        node.append(i)
    dg.add_nodes_from(node)
    edgebox = []
    for reg in range(20):
        for j in range(50):
            index1 = reg*50+j
            for k in range(50):
                index2 = reg*50+k
                if index2==index1:
                    continue
                edgebox.append((index1,index2))
    dg.add_edges_from(edgebox)
    edgebox = []
    for i in range(randlink):
        a = random.randint(0,999)
        b = random.randint(0,999)
        areg = a/50
        breg = b/50
        while a==b or areg==breg or ((a,b) in edgebox):
            a = random.randint(0,999)
            b = random.randint(0,999)
            areg = a/50
            breg = b/50
        edgebox.append((a,b))
    dg.add_edges_from(edgebox)
    return dg

dg,edgebox = creatSmallWorld(200)
print edgebox
