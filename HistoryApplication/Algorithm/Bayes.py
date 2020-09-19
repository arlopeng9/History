import jieba,re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer  # 从sklearn.feature_extraction.text里导入文本特征向量化模块
from sklearn.naive_bayes import MultinomialNB  # 从sklean.naive_bayes里导入朴素贝叶斯模型
from sklearn.metrics import classification_report
tag_name = ['搜索引擎','交易类网站','知识问答类','功能性质网站','娱乐类型网站','企业教育网站']

def generateTest(file_name):
    ret = []
    web_dic={0:["360.cn","baidu.com","so.com","bing.com","google.cn"],#搜索引擎
             1: ["www.cc","b2b.cc","mall.cc","creditcard.cc","taobao.com","alipay.com",
                 "tmall.com","jd.com","dangdang.com","company1.cc","ebank.cc"],#交易类网站
             2: ["csdn.net","2cto.com","liaoxuefeng.com","w3cschool.cn","cnblogs.com","zol.com",
                 "python.org","douban.com","shidastudy.com","v2ex.com","i.cn","home.cn","passport.cn",
                 "testerhome.com","aosabook.org","ggdoc.com","biqukan.com","runoob.com","scrapy.org","github.com",
                 "w3school.com","jb51.net","mycodes.net","360doc.com","zhihu.com","stackoverflow.com","pypi.org"],#知识问答类
             3: ["ccb.com",'ok',"163.com","ibsbjstar.cc","app.com","maiziedu.com","browsershots.org","gerensuodeshui.cn",
                 "gitlab.com","youdao.com","alicdn.com","qmail.com"],#功能性质网站
             4:["biqudao.com","biqudu.com","siluke.tw","biquge.cc","6mao.com","biqiuge.com","biquge.info",
                "dingdiann.com","qq.com","booktxt.net","biquge.com","xs.la","208xs.com","xxbiquge.com",
                "xuexi111.com","ufochn.com","ahzww.net","555zw.com","biquge5200.com","bequge.com","bqg99.com",
                "bqg99.cc","sbiquge.com","biquge5200.cc","166xs.com","youku.com","iqiyi.com","bilibili.com","huya.com",
                "v.qq.com","huya.com","mgtv.com","le.com","ixigua.com","tv.sohu.com","haokan.baidu.com"],#    娱乐类型网站
             5: ["microsoft.com","weaver.com","oa8000.com","goodwaysoft.com","lenosoft.net",
                 "lizheng.com","adobe.com","pexels.com","dingtalk.com","autodesk.com","qifeiye.com",
                 "lizhengyun.com","shuishandt.com","windows7en.com","coursera.org","smoson.com","gongboshi.com",
                 "huawei.com","spoon.net","jetbrains.com","sqlite.org","yesacc.com","sunlandzk.com",
                 "alibabagroup.com","turbo.net","cqttech.com","prezi.com","tradedoubler.com",
                 "renrendai.com","alizila.com","hongzhixx.cn","studyol.com","cnbim.com","apply.cc",
                 "ccopyright.com","gov.cn","jzjyy.cn","jseea.cn","jszk.net","qihoo.com","eastday.com","toutiao.com","ufochn.com","timeacle.cn","xfwed.com",
                 "docin.com","sohu.com","msn.cn","chouti.com","milkjpg.com","btime.com","51xuedu.com",
                 "joyme.com","whu.edu.cn"],#企业教育网站
             }
    with open(file_name,"r",encoding='utf-8') as fp:
            str = fp.readlines()
            for line in str:
                if line != '\n':
                    line = line.split(',',1)
                    line[1] = line[1].replace('\n','')
                    line[1] = line[1].replace('\r','')    #去除回车换行符
                    ret.append(line)  
    
    data = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for line in ret:
        flag = False
        if flag == False:
            for url in web_dic[0]:
                if url in line[0]:
                    data[0].append(line[1])
                    flag = True
                    break
        if flag == False:
            for url in web_dic[1]:
                if url in line[0]:
                    data[1].append(line[1])
                    flag = True
                    break
        if flag == False:
            for url in web_dic[2]:
                if url in line[0]:
                    data[2].append(line[1])
                    flag = True
                    break
        if flag == False:
            for url in web_dic[3]:
                if url in line[0]:
                    data[3].append(line[1])
                    flag = True
                    break
        if flag == False:
            for url in web_dic[4]:
                if url in line[0]:
                    data[4].append(line[1]) 
                    flag = True
                    break  
        if flag == False:
            for url in web_dic[5]:
                if url in line[0]:
                    data[5].append(line[1])  
                    flag = True
                    break
        if flag == False:
            data[6].append(line[1])        
    
    with open('./Resource/BayesTestData/0.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[0])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/1.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[1])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/2.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[2])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/3.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[3])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/4.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[4])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/5.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[5])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/Data.txt','w',encoding='utf-8')as f:
        cutwords = cut_words(data[6])
        for line in cutwords:
            f.write(','.join(line)+'\n')
    with open('./Resource/BayesTestData/BayesData.txt','w',encoding='utf-8')as f:
        with open('./Resource/BayesTestData/BayesTag.txt','w',encoding='utf-8')as f1:
            for i in range(6):
                cutwords = cut_words(data[i])
                for line in cutwords:
                    if line != []:
                        f.write(','.join(line)+'\n')
                        f1.write('%d\n'%i)
            cutwords = cut_words(data[6])
            for line in cutwords:
                if line != []:
                    f.write(','.join(line)+'\n')

def cut_words(words):
    stop_words = []
    jieba_words = []
    for r in words:
        cutwords = jieba.cut(r)
        jieba_words.append(cutwords)
    with open('./Resource/hit_stopwords.txt',"r",encoding='utf-8') as fp:
        str = fp.read()
        stop_words = str.split('\n')
    new_words = []
    for line in jieba_words:
        new_word = []
        for r in line:
            if r not in stop_words:
                new_word.append(r)
        if new_word != []:    # 去除全是停用词文本
            new_words.append(new_word)
    return new_words


def cal_TF_IDF(file):
    corpus = []
    for line in open(file, 'r',encoding='utf-8').readlines():
    # #print line
    #     line = line.strip()
    #     line = re.sub('[^,a-zA-Z0-9\u4E00-\u9FFF]','',line)   #去除特殊符号
    #     line = re.sub(r'\b\d+\b','',line)  #\b 单词边界( 空格，句号，逗号)  匹配字符串中纯数字
        corpus.append(line.strip())#文件就是存放所有文档分词结果的文件，一共13行，每行代表一篇文本，把它读取到corpus中
    vectorizer = CountVectorizer()#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer() #该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names() #获取词袋模型中的所有词语
    weight = tfidf.toarray() #将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    return weight


def testNB():
    XWeight = cal_TF_IDF('./Resource/BayesTestData/BayesData.txt')
    TrainX,TrainY = XWeight.shape
    with open('./Resource/BayesTestData/BayesTag.txt','r',encoding='utf-8')as f1:
        Tag = f1.readlines()
        TagWeight = []
        for line in Tag:
            TagWeight.append(line.strip())
    TargetX = len(TagWeight)
    #将训练集和测试集分割
    X_train, X_test, y_train, y_test = train_test_split(XWeight[0:TargetX], TagWeight,test_size=0.25,random_state=33)  # 随机采样25%的数据样本作为测试集
    MNB = MultinomialNB()  # 使用默认配置初始化朴素贝叶斯
    MNB.fit(X_train, y_train)  # 利用训练数据对模型参数进行估计
    y_predict = MNB.predict(X_test)  # 对参数进行预测
    print('朴素贝叶斯分类器的精度为:', MNB.score(X_test, y_test))
    print(classification_report(y_test, y_predict, target_names=tag_name))


def classifyNB(file):
    TrainWeight = cal_TF_IDF('./Resource/BayesTestData/BayesData.txt')
    TrainX,TrainY = TrainWeight.shape
    with open('./Resource/BayesTestData/BayesTag.txt','r',encoding='utf-8')as f1:
        Tag = f1.readlines()
        TagWeight = []
        for line in Tag:
            TagWeight.append(line.strip())
    TargetX = len(TagWeight)
    MNB = MultinomialNB()  # 使用默认配置初始化朴素贝叶斯
    MNB.fit(TrainWeight[0:TargetX], TagWeight)  # 利用训练数据对模型参数进行估计
    Target_predict = MNB.predict(TrainWeight[TargetX:])  # 对参数进行预测
    with open('./Resource/BayesTestData/BayesTag.txt','w',encoding='utf-8')as f1:
        for i in TagWeight:
            f1.writelines(i+'\n')
        for j in Target_predict:
            f1.writelines(j+'\n')
    return Target_predict

generateTest('./Resource/KNNtrainning.csv')
print(classifyNB('./Resource/BayesTestData/Data.txt'))
testNB()