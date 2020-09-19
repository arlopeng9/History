import numpy as np
from collections import Counter
import re


def findKeyword(word,weight):
    X,Y = weight.shape
    word_weight = []
    top_k = 5
    for i in range(X):
        temp = []
        top_k_Y = np.argsort(-weight[i])[0:top_k]
        for j in top_k_Y:
            temp.append([word[j],weight[i][j]])
        word_weight.append(temp)  
    return word_weight



def findFrequence(file):
    corpus = []
    frequent_word = []
    top_k = 4
    with open(file, 'r',encoding='utf-8')as f:
        line = f.readlines()
        line = line[0].strip()
        line = re.sub('[^,a-zA-Z0-9\u4E00-\u9FFF]','',line)   #去除特殊符号
        line = re.sub(r'\b\d+\b','',line)  #\b 单词边界( 空格，句号，逗号)  匹配字符串中纯数字
        line = line.split(',')
        corpus.extend(line)#文件就是存放所有文档分词结果的文件，一共13行，每行代表一篇文本，把它读取到corpus中
    top_k_Lenth = Counter(corpus) 
    frequent = top_k_Lenth.most_common(top_k)
    for i in frequent:
        frequent_word.append(i[0])
    return frequent_word