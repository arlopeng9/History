from numpy import *

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])    
    C1.sort()
    return map(frozenset, C1)#使用冷冻集可以作为字典的键  

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for can in Ck:
        for tid in D:
            if can.issubset(tid):
                if not can in ssCnt.keys(): ssCnt[can]=1
                else: ssCnt[can] = ssCnt[can] + 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k): 
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #开始的k-2个集合相等的
                retList.append(Lk[i] | Lk[j]) #集合并
    return retList

def apriori(dataSet, minSupport = 0.35):
    C1 = createC1(dataSet)
    D = dataSet
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#扫描项集得到得到非重复结果
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


def generateRules(L, supportData, minConf=0.7):  #supportData是支持度字典
    bigRuleList = []
    for i in range(1, len(L)):#遍历L中的每一个频繁项集
        for freqSet in L[i]: 
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList         

def calcConf(freqSet, H, supportData, brl, minConf):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #计算可信度
        if conf >= minConf: 
            print(freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): 
        Hmp1 = aprioriGen(H, m+1)#生成H中元素的无重复组合,下一次迭代的H列表
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #如果不止一条规则满足要求，那么使用Hmp1迭代调用函数rulesFromConseq()来判断是否可以进一步组合这些规则。
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
            
def pntRules(ruleList, itemMeaning):
    for ruleTup in ruleList:
        for item in ruleTup[0]:
            print(item)
        print("           -------->")
        for item in ruleTup[1]:
            print(item)
        print("confidence: %f\t" % ruleTup[2])
        
 