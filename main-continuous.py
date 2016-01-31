import numpy
import math
import random
import networkx as nx
total = 1000
internetDelay = 0.08
timeInterval = 0.01
rePostRate = 0.1
explosiveness = 0.5
newspaperDelay = 0.5
totalTime = 4
klink = 15
randlink = 200
radioDens = 10

def produceMediaDictionary(population,rnewspaper,rradio,rtv,rinternet):
    if rnewspaper > 100:
        rnewspaper = 100
    nradio = int(population*(100- rradio))/100
    ntv = int(population*(100-rtv))/100
    ninternet = int(population*(100-rinternet))/100
    nnewspaper = int(population*(100-rnewspaper))/100
    aradio = range(0,population)
    atv = range(0,population)
    ainterest = range(0,population)
    anewspaper = range(0,population)
    for i in range(0,nradio):
        del aradio[random.randint(0,len(aradio)-1)]
    for i in range(0,ntv):
        del atv[random.randint(0,len(atv)-1)]
    for i in range(0,ninternet):
        del ainterest[random.randint(0,len(ainterest)-1)]
    for i in range(0,nnewspaper):
        del anewspaper[random.randint(0,len(anewspaper)-1)]
    aaradio = []
    aatv = []
    aainterest = []
    aanewspaper = []
    for i in range(0,population):
        if i in aradio:
            aaradio.append(True)
        else:
            aaradio.append(False)
    for i in range(0,population):
        if i in atv:
            aatv.append(True)
        else:
            aatv.append(False)
    for i in range(0,population):
        if i in ainterest:
            aainterest.append(True)
        else:
            aainterest.append(False)
    for i in range(0,population):
        if i in anewspaper:
            aanewspaper.append(True)
        else:
            aanewspaper.append(False)

    for i in range(0,population):
        if aanewspaper[i]:
            if aainterest[i]:
                aatv[i] = False
                aaradio[i] = False
            else:
                if aatv[i]:
                    aaradio[i] = False

        else:
            if aainterest[i]:
                if aatv[i]:
                    aaradio[i] = False
    return (aanewspaper,aaradio,aatv,aainterest)

def customInt(fl):
    if fl-int(fl)<0.5:
        return int(fl)
    else:
        return int(fl)+1

def negativeExpo(time):
    return math.e**(-2.575*time)

def judgeWithRate(r):
    if random.random()<r:
        return True
    else:
        return False

def gammaFunc(value,rate):
        randomVar = numpy.random.gamma(value*rate, scale=1.0/rate, size=None)
        return randomVar

class Person:
    def __init__(self,info,count,access=False,inInternetSystem=False,inNewspaperSystem=False,inRadioSystem=False,inTVSystem=False):
        self.info = info
        self.count = count
        self.access = access
        self.repost = False
        self.inInternetSystem = inInternetSystem
        self.inNewspaperSystem = inNewspaperSystem
        self.inRadioSystem = inRadioSystem
        self.inTVSystem = inTVSystem
        self.repostrate = rePostRate*explosiveness
        self.reposted = False

    def calcRepostProb(self,rate,time):
        p = rate
        self.repostrate=p*negativeExpo(time)*explosiveness



class newspaperMOD:
    def __init__(self,dg):
        self.dg = dg
        self.timeLine = 0
        self.record = []
        self.timerec = []
        edgebox = []
        for i in range(total/50):
            lcstr = 'local-'+str(i)
            self.dg.add_node(lcstr)
            for j in range(total/20):
                index = j+i*50
                edgebox.append((lcstr,index,gammaFunc(newspaperDelay,40)))
        self.dg.add_weighted_edges_from(edgebox)
        for i in range(20):
            lcstr = 'local-'+str(i)
            for j in range(50):
                index = i*50 + j
                self.dg.node[index].count = self.dg.edge[lcstr][index]['weight']
                self.dg.node[index].access = True

    def update(self):
        self.timeLine += timeInterval
        for i in range(total):
            if self.dg.node[i].info or self.dg.node[i].inNewspaperSystem == False:
                continue
            self.dg.node[i].count -= timeInterval
            if self.dg.node[i].count<=0:
                self.dg.node[i].info=True
                self.record.append(i)
                self.timerec.append(self.timeLine)

    def updateWithTime(self,time):
        count = int(time/timeInterval)
        for i in range(count):
            self.update()

    def getResult(self):
        result = {}
        self.updateWithTime(totalTime)
        for i in range(len(self.record)):
            result[self.record[i]] = self.timerec[i]
        for i in range(1000):
            if not (i in result):
                result[i] = -1
        return result

class internetMOD:
    def __init__(self,dg,rate,initialQuan):
        self.dg = self.creatLittleWorldEdges(dg)
        self.rate = rate
        self.timeLine = 0
        self.record = []
        insystemCount = int(rate*1000)
        chosen = []
        for i in range(insystemCount):
            randn = random.randint(0,999)
            while randn in chosen:
                randn = random.randint(0,999)
            chosen.append(randn)
        for i in range(1000):
            if i in chosen:
                self.dg.node[i] = Person(False,0,inInternetSystem=True)
            else:
                self.dg.node[i] = Person(False,0,inInternetSystem=False)
        initialGuys = []
        for i in range(initialQuan):
            randn = random.randint(0,999)
            while not (randn in chosen) or randn in initialGuys:
                randn = random.randint(0,999)
            initialGuys.append(randn)
        for n in initialGuys:
            self.dg.node[n].info = True
            self.dg.node[n].repost = True
            self.record.append((n,0))

    def creatLittleWorldEdges(self,dg):
        fullbox = []
        edgebox = []
        for i in range(50):
            fullbox.append(i)
        for reg in range(20):
            for j in range(50):
                index1 = reg*50+j
                chosen = []
                for k in range(klink):
                    randn = random.randint(0,49)
                    while (randn in chosen) or (reg*50+randn==index1):
                        randn = random.randint(0,49)
                    chosen.append(randn)
                for k in range(klink):
                    index2 = reg*50+chosen[k]
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

    def update(self):
        self.timeLine += timeInterval
        for n in self.dg:
            if self.dg.node[n].inInternetSystem == False:
                continue
            if self.dg.node[n].info == True and self.dg.node[n].repost == True:
                nodes = self.dg[n]
                nodesCount = len(nodes)
                repostCount = customInt(self.dg.node[n].repostrate*nodesCount)
                repostIndexBox = []
                for i in range(repostCount):
                    randn = random.randint(0,nodesCount-1)
                    while randn in repostIndexBox:
                        randn = random.randint(0,nodesCount-1)
                    repostIndexBox.append(randn)
                index = 0
                if not self.dg.node[n].reposted:
                    self.dg.node[n].reposted = True
                    for child in nodes:
                        if self.dg.node[child].inInternetSystem == False or self.dg.node[child].info == True:
                            continue
                        else:
                            if self.dg.node[child].access == False:
                                self.dg.node[child].count = internetDelay
                                self.dg.node[child].access = True
                            if index in repostIndexBox:
                                self.dg.node[child].repost = True
                        index += 1
            else:
                if self.dg.node[n].access == True and self.dg.node[n].info == False and self.dg.node[n].count < 0:
                    self.dg.node[n].info = True
                    self.dg.node[n].calcRepostProb(rePostRate,self.timeLine)
                    self.record.append((n,self.timeLine))
                elif self.dg.node[n].access == True and self.dg.node[n].count > 0:
                    self.dg.node[n].count -= timeInterval
        return

    def howManyWorldKnows(self):
        regCount = 0
        for reg in range(20):
            for j in range(50):
                index = reg*50+j
                if self.dg.node[index].info == True:
                    regCount += 1
                    break
        return regCount

    def updateWithTime(self,days):
        ct = int(days/timeInterval)
        for i in range(ct):
            self.update()



class Crowd:
    def __init__(self,newspaperRate,radioRate,TVRate,internetRate):
        calculatedRates = produceMediaDictionary(total,newspaperRate,radioRate,TVRate,internetRate)
        self.newspaperBox = calculatedRates[0]
        self.radioBox = calculatedRates[1]
        self.TVBox = calculatedRates[2]
        self.internetBox = calculatedRates[3]
        self.dg = self.creatSmallWorld(randlink)

    def creatSmallWorld(self,randlink):
        dg = nx.DiGraph()
        node = []
        for i in range(1000):
            node.append(i)
        dg.add_nodes_from(node)
        for i in range(1000):
            dg.node[i] = Person(False,None,inNewspaperSystem=self.newspaperBox[i],inRadioSystem=self.radioBox[i],inTVSystem=self.TVBox[i],inInternetSystem=self.internetBox)
        edgebox = []
        fullbox = []
        return dg

myCrowd = Crowd(0,0,0,1)
dg = myCrowd.dg
myNews = newspaperMOD(dg)
myNews.updateWithTime(totalTime)
print len(myNews.record)

