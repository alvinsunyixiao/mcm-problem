import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
import math
#import multiprocessing
print 'note: 3.01-4'
n = 3         #Newspaper Seller Count
m = 5         #Region Count
interval = 0.01
totalTime = 4
posreg = [(0,3,0,1),(6,9,0,1),(12,15,0,1),(18,21,0,1),(24,27,0,1)]

def calcRandPoint(reg):
    xmin = reg[0]
    xmax = reg[1]
    ymin = reg[2]
    ymax = reg[3]
    randx = random.random()*(xmax-xmin)+xmin
    randy = random.random()*(ymax-ymin)+ymin
    return (randx,randy)

def uniformdis(n):
    if random.random()<n:
        return True
    else:
        return False

def negativeExpo(time):
    return math.e**(-2.575*time)

class Person:
    def __init__(self,info,count,region):
        self.info = info
        self.count = count
        self.region = region

class Crowd:
    def __init__(self,n,m):
        self.dg,self.edgebox = self.creatRelationshipMap(n,m)
        self.nodecolor = []
        self.posdict = {}
        for i in self.dg:
            if i<1000:
                ireg = int((i-1)/10)+1
                self.dg.node[i] = Person(False,0,ireg)
                self.nodecolor.append((1,0,0))
                cord = calcRandPoint(posreg[self.dg.node[i].region-1])
                self.posdict[i] = cord
            else:
                nm = i/1000
                cord = (6*nm-4.5,-3.0)
                self.dg.node[i] = Person(True,0,nm)
                self.nodecolor.append((1,0,0))
                self.posdict[i] = cord
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

    def initwithOne(self,n):
        self.FirstGuy = 1
        self.dg.node[self.FirstGuy] = Person(True,0)
        self.dg.node[self.FirstGuy].repost = True
    def getMap(self):
        return self.dg


    def creatRelationshipMap(self,n,m):
        dg = nx.DiGraph()
        nbox = []
        for i in range(n):
            nbox.append((i+1)*1000)
        for i in range(m*10):
            nbox.append(i+1)
        edgebox = []
        print nbox
        dg.add_nodes_from(nbox)
        for i in range(m*10):
            ireg = int(i/m)+1
            mark = uniformdis(0.8)
            if mark and ireg<=n:
                edgebox.append((ireg*1000,i+1,0.08))
            else:
                randreg = random.randint(1,n)
                while randreg==ireg:
                    randreg = random.randint(1,n)
                randreg *= 1000
                edgebox.append((randreg,i+1,2))
        dg.add_weighted_edges_from(edgebox)
        return dg,edgebox

    def update(self):
        self.timeLine += interval
        #print self.timeLine
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
                    self.nodecolor[n-1]=((self.timeLine/totalTime)**(1.0/3),(self.timeLine/totalTime)**(1.0/4),0.5+0.5*(self.timeLine/totalTime)**(1.0/5))
                    #self.linkrecord.append(len(self.dg[n]))
                elif self.dg.node[n].access == True:
                    self.dg.node[n].count -= interval
        return

    def updateWithTime(self,days):
        ct = int(days/interval)
        for i in range(ct):
            self.update()

avgbox = []
totalTimebox = []
'''
while totalTime<=4:
    totalTimebox.append(totalTime)
    total = 0
    for i in range(100):
        myCrowd = Crowd(n,m,time)
        myCrowd.updateWithTime(totalTime)
        total += len(myCrowd.record)
    avg = int(total/100)
    avgbox.append(avg)
    totalTime += 0.01
print totalTimebox
print avgbox
'''


myCrowd = Crowd(n,m)
#myCrowd.updateWithTime(totalTime)
dg = myCrowd.getMap()


nx.draw_networkx(dg,arrows=False,node_color=myCrowd.nodecolor,with_labels=False,pos=myCrowd.posdict)
plt.show()