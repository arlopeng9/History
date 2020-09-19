from Algorithm import apriori
from Algorithm import visitVisible
from Algorithm import fpGrowth
from Algorithm import K_Means
from Algorithm import recommend

import re
import os
# dataSet = visitVisible.visitondays()
# visitVisible.write_to_apriori(dataSet)
# L,supportData = apriori.apriori(dataSet)
# print(apriori.generateRules(L,supportData))
# minSup =5
# initSet = fpGrowth.createInitSet(dataSet)
# myFPtree, myHeaderTab = fpGrowth.createTree(initSet, minSup)
# myFPtree.disp()
# myFreqList = []
# fpGrowth.mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
## 过滤纯数字以及特殊符号
# a = []
# for line in open('./Resource/0.txt', 'r',encoding='utf-8').readlines():
#     #print line
#     line = line.strip()
#     line = re.sub('[^,a-zA-Z0-9\u4E00-\u9FFF]','',line)   #去除特殊符号
#     line = re.sub(r'\b\d+\b','',line)  #\b 单词边界( 空格，句号，逗号)  匹配字符串中纯数字
#     a.append(line)
#     print(line)

# os.system('mitmdump.exe -s D:\\Document\\repo\\History\\HistoryApplication\\Algorithm\\Proxy.py')
for i in range(6):
    word,weight = K_Means.cal_TF_IDF('./Resource/KMeansData/{}.txt'.format(i))
    recon = recommend.findKeyword(word,weight)
    print("第{}类".format(i+1))
    print(recon)

