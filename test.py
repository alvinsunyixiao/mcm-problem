import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
n = 20        #Population Count
m = 150       #Relationship Count
time = 0.08

def rePostJudge(rate):
        p = 1.0 * rate / 100
        print p
        print random.random()
        if p<random.random():
            return True
        else:
            return False

print rePostJudge(10)