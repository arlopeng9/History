class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      
        self.children = {} 
    
    def inc(self, numOccur):
        self.count += numOccur
        
    def disp(self, ind=1):
        print(( '  '*ind, self.name, ' ', self.count))
        for child in self.children.values():
            child.disp(ind+1)

def createTree(dataSet, minSup=3): 
    headerTable = {}
    #扫描数据集两次
    for trans in dataSet:#第一遍对所有元素项的出现次数进行计数
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable.keys()):  #扫描头指针表删掉那些出现次数少于minSup的项
        if headerTable[k] < minSup: 
            del headerTable[k]
    freqItemSet = set(headerTable.keys())
    #print(( 'freqItemSet: ',freqItemSet))
    if len(freqItemSet) == 0: return None, None  #如果所有项都不频繁，就不需要进行下一步处理
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #重新定义头指针表以便于使用nodeLink 
    #print(( 'headerTable: ',headerTable))
    retTree = treeNode('Null Set', 1, None) #创建只包含空集合∅的根节点
    for tranSet, count in dataSet.items():  #再一次遍历数据集
        localD = {}
        for item in tranSet: 
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#让树生长
    return retTree, headerTable #返回树和头指针表

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#判断排序项集的第一个元素项是否作为子节点存在
        inTree.children[items[0]].inc(count) #该元素项计数增加
    else:   #创建一个新的treeNode并将其作为一个子节点添加到树中
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: #头指针表更新以指向新的节点
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#使用剩下的有序集作为参数调用updateHeader()
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
        
def updateHeader(nodeToTest, targetNode):   #未使用迭代,如果链表很长可能会遇到迭代调用的次数限制
    while (nodeToTest.nodeLink != None):    
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
        
def ascendTree(leafNode, prefixPath): 
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
    
def findPrefixPath(basePat, treeNode): 
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0])]#头指针表排序,从小到大
    for basePat in bigL:  #从头指针表最小开始
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        #print(( 'finalFrequent Item: ',newFreqSet    #append to set))
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        #print( 'condPattBases :',basePat, condPattBases)
        #2. 根据条件基创建条件树
        myCondTree, myHead = createTree(condPattBases, minSup)
        #print( 'head from conditional tree: ', myHead)
        if myHead != None: #如果树中有元素项的话，递归调用mineTree()函数
            print( 'conditional tree for: ',newFreqSet)
            myCondTree.disp(1)            
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)


def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict






