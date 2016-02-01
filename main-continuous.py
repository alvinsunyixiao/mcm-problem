import numpy
import math
import random
import networkx as nx
import copy
import matplotlib.pyplot as plt
##########################
#------DATA Section------#
##########################

tvdata = [0,0,0,0,0,0,9,63,85,90,95,97,98,98,98,98,98,98,98,98,98,98,98]
radiodata = [0,20,39,55,73,82,80,91,94,94,95,99,99,99,99,99,99,99,99,99,99,99,99]
yearsdata = [1920,1925,1930,1935,1940,1945,1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2011,2012,2013,2014]
internetdata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.8,9.2,43.1,68.0,71.7,69.7,79.3,84.2,87.4]
newspaperdata =[109.90184324158706, 122.45127616294623, 135.29367795575217, 126.23338096668866, 130.92343894289897, 145.57656127924932, 148.7016534119077, 142.29382454163897, 137.20741052347248, 130.8302448582204, 127.4612907946311, 118.28779924660442, 114.95516483268226, 110.83677952700845, 104.9032884174072, 93.1205015131286, 86.80000000006874, 75.91375002826089, 59.05552451777496, 59.95106320184407, 59.358991191811846, 60.637578515055914, 58.201582314251176]

for i in range(2015,2051):
    yearsdata.append(i)
    tvdata.append(98)
    radiodata.append(99)
    newspaperdata.append(2978.4369263956787 - 1.448409993618103*i)
    internetdata.append(99.83367 - 66.6891*math.e**(-0.0996124*i + 199.0255752))

#####################################################
#-----------------------CODE------------------------#
#####################################################
total = 1000
internetDelay = 0.08
timeInterval = 0.01
rePostRate = 0.3
explosiveness = 0.5
newspaperDelay = 0.7
totalTime = 3
klink = 25
randlink = klink*40+200
radioDens = 5
radioTrust = 0.1
alpha = 0.5
radioDelay = 0.5
TVDelay = 0.5
TVDens = 20
TVTrust = 1.0/TVDens*0.8
convience = {'newspaper':1,'radio':0.6,'TV':0.8,'internet':0.4}

print 'note: '
print 'klink: '+str(klink)

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
    def __init__(self,info,count,access=False,inInternetSystem=False,inNewspaperSystem=False,inRadioSystem=False,inTVSystem=False,believe=0.5):
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
        self.believe = believe
        self.infoCount = 0
        self.spreading = False

    def calcRepostProb(self,rate,time):
        p = rate
        self.repostrate=p*negativeExpo(time)*explosiveness

class TVMOD:
    def __init__(self,dg):
        copy_dg = copy.deepcopy(dg)
        self.dg = copy_dg
        self.timeLine = 0
        self.record = []
        self.timerec = []
        self.edgeCount = 0
        for i in range(1000):
            self.dg.node[i].count = gammaFunc(TVDelay,30)
            self.dg.node[i].access = True
            if self.dg.node[i].inTVSystem:
                self.edgeCount += 20
    def update(self):
        self.timeLine += timeInterval
        for i in range(total):
            if self.dg.node[i].info or self.dg.node[i].inTVSystem == False:
                continue
            self.dg.node[i].count -= timeInterval
            if self.dg.node[i].count<=0:
                rate = 1-(1-explosiveness*TVTrust)**TVDens
                if judgeWithRate(rate):
                    self.dg.node[i].info=True
                    self.record.append(i)
                    self.timerec.append(self.timeLine)
                else:
                    self.dg.node[i].inTVSystem = False

    def updateWithTime(self,time):
        count = int(time/timeInterval)
        for i in range(count):
            self.update()

    def getResult(self):
        result = {}
        self.updateWithTime(totalTime)
        for i in range(len(self.record)):
            result[self.record[i]] = {'time':self.timerec[i],'trust':self.dg.node[self.record[i]].believe*convience['TV']}
        for i in range(1000):
            if not (i in result):
                result[i] = {'time':None,'trust':0}
        return result

class radioMOD:
    def __init__(self,dg):
        copy_dg = copy.deepcopy(dg)
        self.dg = copy_dg
        self.timeLine = 0
        self.record = []
        self.timerec = []
        self.edgeCount = 0
        for i in range(1000):
            self.dg.node[i].count = gammaFunc(radioDelay,30)
            self.dg.node[i].access = True
            if self.dg.node[i].inRadioSystem:
                self.edgeCount += 5

    def update(self):
        self.timeLine += timeInterval
        for i in range(total):
            if self.dg.node[i].info or self.dg.node[i].inRadioSystem == False:
                continue
            self.dg.node[i].count -= timeInterval
            if self.dg.node[i].count<=0:
                rate = 1-(1-explosiveness*radioTrust)**radioDens
                if judgeWithRate(rate):
                    self.dg.node[i].info=True
                    self.record.append(i)
                    self.timerec.append(self.timeLine)
                else:
                    self.dg.node[i].inRadioSystem = False

    def updateWithTime(self,time):
        count = int(time/timeInterval)
        for i in range(count):
            self.update()

    def getResult(self):
        result = {}
        self.updateWithTime(totalTime)
        for i in range(len(self.record)):
            result[self.record[i]] = {'time':self.timerec[i],'trust':self.dg.node[self.record[i]].believe*convience['radio']}
        for i in range(1000):
            if not (i in result):
                result[i] = {'time':None,'trust':0}
        return result


class newspaperMOD:
    def __init__(self,dg):
        copy_dg = copy.deepcopy(dg)
        self.dg = copy_dg
        self.timeLine = 0
        self.record = []
        self.timerec = []
        self.edgeCount = 0
        edgebox = []
        for i in range(total/50):
            lcstr = 'local-'+str(i)
            self.dg.add_node(lcstr)
            for j in range(total/20):
                index = j+i*50
                edgebox.append((lcstr,index,gammaFunc(newspaperDelay,40)))
                if self.dg.node[index].inNewspaperSystem:
                    self.edgeCount += 1
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
                if judgeWithRate(explosiveness/10):
                    self.dg.node[i].info=True
                    self.record.append(i)
                    self.timerec.append(self.timeLine)
                else:
                    self.dg.node[i].inNewspaperSystem = False

    def updateWithTime(self,time):
        count = int(time/timeInterval)
        for i in range(count):
            self.update()

    def getResult(self):
        result = {}
        self.updateWithTime(totalTime)
        for i in range(len(self.record)):
            result[self.record[i]] = {'time':self.timerec[i],'trust':self.dg.node[self.record[i]].believe*convience['newspaper']}
        for i in range(1000):
            if not (i in result):
                result[i] = {'time':None,'trust':0}
        return result

class internetMOD:
    def __init__(self,dg,initialQuan):
        copy_dg = copy.deepcopy(dg)
        self.edgeCount = 0
        self.dg = self.creatLittleWorldEdges(copy_dg)
        self.timeLine = 0
        self.record = []
        self.timerec = []
        initialGuys = []
        totalInSys = 0
        for n in dg:
            if self.dg.node[n].inInternetSystem:
                totalInSys += 1
        if initialQuan>totalInSys:
            initialQuan = totalInSys
        for i in range(initialQuan):
            randn = random.randint(0,999)
            while not self.dg.node[randn].inInternetSystem or randn in initialGuys:
                randn = random.randint(0,999)
            initialGuys.append(randn)
        for n in initialGuys:
            self.dg.node[n].info = True
            self.dg.node[n].repost = True
            self.record.append(n)
            self.timerec.append(0)
            self.dg.node[n].infoCount += 1
            self.dg.node[n].spreading = True
        self.spreadCount = []

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
                    if dg.node[index1].inInternetSystem and dg.node[index2].inInternetSystem:
                        self.edgeCount += 1
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
            if dg.node[a].inInternetSystem and dg.node[b].inInternetSystem:
                self.edgeCount += 1
        dg.add_edges_from(edgebox)
        return dg

    def update(self):
        self.timeLine += timeInterval
        spreadCt = 0
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
                spread = False
                if not self.dg.node[n].reposted:
                    self.dg.node[n].reposted = True
                    for child in nodes:
                        self.dg.node[child].infoCount += 1
                        if self.dg.node[child].inInternetSystem == False or self.dg.node[child].info == True:
                            continue
                        else:
                            spread = True
                            if self.dg.node[child].access == False:
                                self.dg.node[child].count = internetDelay
                                self.dg.node[child].access = True
                            if index in repostIndexBox:
                                self.dg.node[child].repost = True
                        index += 1
                else:
                    for child in nodes:
                        if not (self.dg.node[child].inInternetSystem):
                            continue
                        elif self.dg.node[child].access == True and self.dg.node[child].info == False:
                            spread = True
                            break
                if spread:
                    spreadCt += 1
            else:
                if self.dg.node[n].access == True and self.dg.node[n].info == False and self.dg.node[n].count < 0:
                    self.dg.node[n].info = True
                    self.dg.node[n].calcRepostProb(rePostRate,self.timeLine)
                    self.record.append(n)
                    self.timerec.append(self.timeLine)
                elif self.dg.node[n].access == True and self.dg.node[n].count > 0:
                    self.dg.node[n].count -= timeInterval
        self.spreadCount.append(spreadCt)
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

    def getResult(self):
        result = {}
        self.updateWithTime(totalTime)
        for i in range(len(self.record)):
            result[self.record[i]] = {'time':self.timerec[i],'trust':self.dg.node[self.record[i]].believe*self.dg.node[self.record[i]].infoCount*convience['internet']}
        for i in range(1000):
            if not (i in result):
                result[i] = {'time':None,'trust':0}
        return result




class Crowd:
    def __init__(self,newspaperRate,radioRate,TVRate,internetRate,netInitial = 1):
        calculatedRates = produceMediaDictionary(total,newspaperRate,radioRate,TVRate,internetRate)
        self.newspaperBox = calculatedRates[0]
        self.radioBox = calculatedRates[1]
        self.TVBox = calculatedRates[2]
        self.internetBox = calculatedRates[3]
        self.dg = self.creatSmallWorld(randlink)
        self.netInitial = netInitial

    def creatSmallWorld(self,randlink):
        dg = nx.DiGraph()
        node = []
        for i in range(1000):
            node.append(i)
        dg.add_nodes_from(node)
        for i in range(1000):
            #######################################
            # Beta Distribution!! --------------> #
            #######################################
            dg.node[i] = Person(False,None,inNewspaperSystem=self.newspaperBox[i],inRadioSystem=self.radioBox[i],inTVSystem=self.TVBox[i],inInternetSystem=self.internetBox[i],believe=numpy.random.beta(alpha,1-alpha))
        edgebox = []
        fullbox = []
        return dg

    def getMin(self,tup):
        Min = None
        for i in tup:
            if i == None:
                continue
            elif Min == None:
                Min = i
            elif i < Min:
                Min = i
        return Min

    def combineResults(self):
        myNews = newspaperMOD(self.dg)
        myRadio = radioMOD(self.dg)
        myTV = TVMOD(self.dg)
        myInternet = internetMOD(self.dg,self.netInitial)
        newsResult = myNews.getResult()
        radioResult = myRadio.getResult()
        TVResult = myTV.getResult()
        internetResult = myInternet.getResult()
        finalResult = {}
        for key in range(1000):
            eachTime = self.getMin((newsResult[key]['time'],radioResult[key]['time'],TVResult[key]['time'],internetResult[key]['time']))
            eachTrust = newsResult[key]['trust']+radioResult[key]['trust']+TVResult[key]['trust']+internetResult[key]['trust']
            finalResult[key] = {'time':eachTime,'trust':eachTrust}
        return finalResult

relationDev = []
for dataIndex in range(len(yearsdata)):
    myCrowd = Crowd(newspaperdata[dataIndex],radiodata[dataIndex],tvdata[dataIndex],internetdata[dataIndex],netInitial=10)
    myNewspaper = newspaperMOD(myCrowd.dg)
    myRadio = radioMOD(myCrowd.dg)
    myTV = TVMOD(myCrowd.dg)
    myInternet = internetMOD(myCrowd.dg,myCrowd.netInitial)
    edgeTotal = myNewspaper.edgeCount+myRadio.edgeCount+myTV.edgeCount+myInternet.edgeCount
    relationDev.append(edgeTotal)
print yearsdata
print relationDev
plt.plot(yearsdata,relationDev)
plt.show()

'''
def iterateLink():
    klst = []
    avelst = []
    global klink
    for klink in range(15,36):
        print klink
        average = 0
        experiment = 100
        for kkk in range(0,experiment):
            myCrowd = Crowd(0,0,0,100,netInitial=10)
            result = myCrowd.combineResults()
            count = 1000
            for i in range(0,1000):
                if result[i]["time"] == None:
                    count -= 1
            average += count
        average /= experiment
        klst.append(klink)
        avelst.append(average)
    print klst
    print avelst

def iterateExp():
    expLst = []
    aveLst_sp = []
    aveLst_b = []
    global explosiveness
    explosiveness = 0.2
    while explosiveness < 0.81:
        print explosiveness
        average_b = 0.0
        average_sp = 0.0
        experiment = 50
        for kkk in range(0,experiment):
            myCrowd = Crowd(newspaperdata[-1],radiodata[-1],tvdata[-1],internetdata[-1],netInitial=10)
            result = myCrowd.combineResults()

            #qmax
            count = 1000
            for i in range(0,1000):
                if result[i]["time"] == None:
                    count -= 1
            average_sp += count
            '''
'''
            groupArray = []
            for i in range(0,20):
                groupArray.append(False)
            for i in range(0,1000):
                groupN = i/50
                if result[i]["time"] != None:
                    groupArray[groupN] = True
            count = 0
            for i in range(0,20):
                if groupArray[i]:
                    count += 1
            '''
'''
            count = 0
            for i in range(1000):
                if result[i]['trust'] > 1:
                    count += 1
            average_b += count

        average_sp /= experiment
        average_b /= experiment
        expLst.append(explosiveness)
        aveLst_sp.append(average_sp)
        aveLst_b.append(average_b)
        explosiveness += 0.01
    print expLst
    print aveLst_sp
    print aveLst_b
iterateExp()
#iterateLink()

myCrowd = Crowd(newspaperdata[-1],radiodata[-1],tvdata[-1],internetdata[-1],netInitial=10)
rs = myCrowd.combineResults()
for key in rs:
    print key,rs[key]['trust']

count = 0
for key in rs:
    if rs[key]['time'] != None:
        count+= 1
print count
count = 0
for key in rs:
    if rs[key]['trust'] > 1:
        count += 1
print count
'''