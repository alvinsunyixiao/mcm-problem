import matplotlib.pyplot as plt
import networkx as nx
import random

def calcRandPoint(reg):
    xmin = reg[0]
    xmax = reg[1]
    ymin = reg[2]
    ymax = reg[3]
    randx = random.random()*(xmax-xmin)+xmin
    randy = random.random()*(ymax-ymin)+ymin
    return (randx,randy)

pos = {}
node_color = []
dg = nx.DiGraph()
edgeBox = []
for i in range(100):
    dg.add_node(i)
    node_color.append((1,0,0))
    pos[i] = calcRandPoint((1,5,1,4))
for i in range(5):
    rdstr = 'radio-'+str(i)
    dg.add_node(rdstr)
    node_color.append((0,1,0))
    pos[rdstr] = (i+1,5)
for i in range(100):
    randn1 = random.randint(0,4)
    randn2 = random.randint(0,4)
    while randn2==randn1:
        randn2 = random.randint(0,4)
    for j in range(5):
        if j==randn1 or j==randn2:
            continue
        rdstr = 'radio-'+str(j)
        edgeBox.append((rdstr,i))
dg.add_edges_from(edgeBox)

nx.draw_networkx(dg,arrows=False,with_labels=False,node_color=node_color,pos=pos)
plt.show()
