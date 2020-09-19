import jieba
import numpy as np
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
import re
from jieba import enable_paddle, posseg


def read_from_file(file_name):
    ret = []
    with open(file_name,"r",encoding='utf-8') as fp:
        str = fp.readlines()
        for line in str:
            if line != '\n':
                line = line.split(',',1)[1].replace('\n','')
                line = line.replace('\r','')    #去除回车换行符
                ret.append(line)
    return ret


def cut_words(stop_word_file):
    words = read_from_file(stop_word_file)
    new_words = []
    for r in words:
        cutwords = jieba.cut(r)
        new_words.append(cutwords)
    
    return set(new_words)


def del_stop_words(stop_word_file):
#   words是已经切词但是没有去除停用词的文档。
#   返回的会是去除停用词后的文档
    words = cut_words(stop_word_file)
    stop_words = []
    with open('./Resource/hit_stopwords.txt',"r",encoding='utf-8') as fp:
        str = fp.read()
        stop_words = str.split('\n')
    new_words = []
    for line in words:
        new_word = []
        for r in line:
            if r not in stop_words:
                new_word.append(r)
        new_words.append(new_word)
        if new_word != []:    # 去除全是停用词文本
            new_words.append(new_word)
    return new_words


def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)


def setOfWords2Vec(vocabList, dataSet):
    returnVec = []
    for line in dataSet:
        lineVec = [0]*len(vocabList)
        for word in line:
            if word in vocabList:
                lineVec[vocabList.index(word)] = 1
            else: print("the word: %s is not in my Vocabulary!" % word)
        returnVec.append(lineVec)
    return returnVec


def write_to_file(dataSet):
    with open('./Resource/TitleData.txt','w',encoding='utf-8') as fp:
        for line in dataSet:
            if line != []:
                fp.writelines(','.join(line)+'\n')


def cal_TF_IDF(file):
    corpus = []
    for line in open(file, 'r',encoding='utf-8').readlines():
    #print line
        line = line.strip()
        line = re.sub('[^,a-zA-Z0-9\u4E00-\u9FFF]','',line)   #去除特殊符号
        line = re.sub(r'\b\d+\b','',line)  #\b 单词边界( 空格，句号，逗号)  匹配字符串中纯数字
        corpus.append(line.strip())#文件就是存放所有文档分词结果的文件，一共13行，每行代表一篇文本，把它读取到corpus中
    vectorizer = CountVectorizer()#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer() #该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names() #获取词袋模型中的所有词语
    weight = tfidf.toarray() #将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    return word,weight


def K_Means(weight):
    clf=KMeans(n_clusters=6)
    clf.fit(weight)
    # #20个中心点
    # print(clf.cluster_centers_)
    
    # # 聚类结果汇总
    # cluster_labels = clf.labels_  # 聚类标签结果
    # comment_matrix = np.hstack((weight,  cluster_labels.reshape(weight.
    #     shape[0], 1)))  # 将向量值和标签值合并为新的矩阵
    # word_vectors.append('cluster_labels')  # 将新的聚类标签列表追加到词向量后面
    # comment_pd = pd.DataFrame(comment_matrix, columns=word_vectors)  # 创建包含词向量和聚类标签的数据框
    # comment_pd.to_csv('comment.csv')
    # print(comment_pd.head(1))  # 打印输出数据框第1条数据
    # # 聚类结果分析
    # comment_cluster1 = comment_pd[comment_pd['cluster_labels'] == 1].drop('cluster_labels', axis=1)  # 选择聚类标签值为1的数据，并删除最后一列
    # word_importance = np.sum(comment_cluster1, axis=0)  # 按照词向量做汇总统计
    # print(word_importance.sort_values(ascending=False)[:5])   # 按汇总统计的值做逆序排序并打印输出前5个词
    #每个样本所属的簇
    # print(clf.labels_)
    with open('./Resource/KMeansResults.txt','w',encoding='utf-8')as fpwrite:
        with open('./Resource/TitleData.txt', 'r',encoding='utf-8') as fpread:
            line = fpread.readlines()
            i = 1
            for line_list in line:
                line_list = line_list.replace('\n','') + ',' + str(clf.labels_[i-1]) + '\n'
                i = i+1
                fpwrite.write(line_list)

    # ms = cluster.MeanShift()
    # ms.fit_predict(weight)
    # two_means = cluster.MiniBatchKMeans(n_clusters=3)
    # two_means.fit_predict(weight)
    # ward = cluster.AgglomerativeClustering(n_clusters=3, linkage='ard')
    # ward.fit_predict(weight)
    # spectral = cluster.SpectralClustering(n_clusters=3,eigen_solver='arpack',affinity="nearest_neighbors")
    # spectral.fit_predict(weight)
    # dbscan = cluster.DBSCAN(eps=.2)
    # dbscan.fit_predict(weight)
    # affinity_propagation = cluster.AffinityPropagation()
    # affinity_propagation.fit_predict(weight)
    return clf.labels_


def extract_keyword():
    word,weight = cal_TF_IDF('./Resource/TitleData.txt')
    X,Y = weight.shape
    word_weight = []
    top_k = 3
    for i in range(X):
        temp = []
        top_k_Y = np.argsort(-weight[i])[0:top_k]
        for j in top_k_Y:
            temp.append(word[j])
        word_weight.append(temp)        
    
    #tsne算法进行降维
    tsne = TSNE(n_components=2)
    decomposition_data = tsne.fit_transform(weight)
    label = K_Means(decomposition_data)


    #浏览记录总数
    alllen = len(label)
    cataword = [[],[],[],[],[],[]]
    for i in range(alllen):
        if label[i] == 0:
            cataword[0].append(word_weight[i])
        elif label[i] == 1:
            cataword[1].append(word_weight[i])
        elif label[i] == 2:
            cataword[2].append(word_weight[i])
        elif label[i] == 3:
            cataword[3].append(word_weight[i])
        elif label[i] == 4:
            cataword[4].append(word_weight[i])
        elif label[i] == 5:
            cataword[5].append(word_weight[i])
        else:
            break
    
    enable_paddle()    #加载词性字典
    for i in range(6):
        with open('./Resource/KMeansData/{}.txt'.format(i),'w',encoding='utf-8')as f:
            for line in cataword[i]:
                for word in line:
                    flag = posseg.lcut(word,use_paddle=True)[0].flag
                    if 'n' in flag:
                        f.write(word+',')
    


if __name__ == "__main__":
    extract_keyword()
    # new_words = del_stop_words('./Resource/KNNtrainning.csv')
    # write_to_file(new_words)
    # vocabList = createVocabList(new_words)
    # print(setOfWords2Vec(vocabList,new_words))
    # word,weight = cal_TF_IDF('./Resource/0.txt')
    # X,Y = weight.shape
    # word_weight = []
    # top_k = 10
    # for i in range(X):
    #     temp = []
    #     top_k_Y = np.argsort(-weight[i])[0:top_k]
    #     for j in top_k_Y:
    #         temp.append([word[j],weight[i][j]])
    #     word_weight.append(temp)  
    # print(word_weight)