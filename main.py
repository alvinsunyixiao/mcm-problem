import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
import math
import multiprocessing

n = 1000        #Population Count
m = 20000       #Relationship Count
time = 0.08
interval = 0.01
repostRate = 10
explosiveness = 1

def negativeExpo(time):
    return math.e**(-2.575*time)

class Person:
    def __init__(self,info,count):
        self.info = info
        self.count = count
        self.access = count
        self.repost = False

    def calcPost(self,time):
        self.repost = self.rePostJudge(repostRate,time)

    def rePostJudge(self,rate,time):
        p = 1.0 * rate / 100
        self.repostrate=p*negativeExpo(time)*explosiveness
        if random.random()<self.repostrate:
            return True
        else:
            return False

class Crowd:
    def __init__(self,n,m,time):
        self.dg,self.edgebox = self.creatRelationshipMap(n,m)
        self.nodecolor = []
        for n in self.dg:
            self.dg.node[n] = Person(False,0)
            self.nodecolor.append('r')
        #self.linkrecord = [self.initwithMostSocial()]
        self.initwithMostSocial()
        self.time = time
        self.record = [(self.FirstGuy,0)]
        self.nodecolor[self.FirstGuy-1]='b'
        self.timeLine = 0


    def initwithMostSocial(self):
        maxcount = 0
        maxindex = 0
        for n in self.dg:
            if len(self.dg[n])>maxcount:
                maxcount = len(self.dg[n])
                maxindex = n
        self.FirstGuy = maxindex
        self.dg.node[self.FirstGuy] = Person(True,0)
        self.dg.node[self.FirstGuy].repost = True
        return maxcount

    def getMap(self):
        return self.dg


    def creatRelationshipMap(self,n,m):
        dg = nx.DiGraph()
        nbox = []
        for i in range(n):
            nbox.append(i+1)
        edgebox = []
        dg.add_nodes_from(nbox)
        for i in range(m):
            a = random.randint(1,n)
            b = random.randint(1,n)
            while ((a,b) in edgebox) or a==b:
                a = random.randint(1,n)
                b = random.randint(1,n)
            edgebox.append((a,b))
        dg.add_edges_from(edgebox)
        return dg,edgebox

    def gammaFunc(self):
        randomVar = numpy.random.gamma(self.time, scale=1.0, size=None)
        return randomVar

    def update(self):
        self.timeLine += interval
        for n in self.dg:
            if self.dg.node[n].info == True:
                nodes = self.dg[n]
                for child in nodes:
                    if self.dg.node[child].info == True:
                        continue
                    elif self.dg.node[n].repost:
                        if self.dg.node[child].access == False:
                            self.dg.node[child].count = self.gammaFunc()
                            self.dg.node[child].access = True
            else:
                if self.dg.node[n].access == True and self.dg.node[n].count <= 0:
                    self.dg.node[n].info = True
                    self.dg.node[n].calcPost(self.timeLine)
                    self.record.append((n,self.timeLine,self.dg.node[n].repost,self.dg.node[n].repostrate))
                    self.nodecolor[n-1]='b'
                    #self.linkrecord.append(len(self.dg[n]))
                elif self.dg.node[n].access == True:
                    self.dg.node[n].count -= interval
        return

    def updateWithTime(self,days):
        ct = int(days/interval)
        for i in range(ct):
            self.update()

countBox = []
for i in range(20):
    countBox.append(0)





myCrowd = Crowd(n,m,time)
myCrowd.updateWithTime(4)
countBox[int((len(myCrowd.record)-1)/50)] += 1
print i

print countBox
nx.draw_networkx(dg,arrows=False,node_color=myCrowd.nodecolor)
plt.show()