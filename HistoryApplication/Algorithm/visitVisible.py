import sqlite3
import time,re
import matplotlib.pyplot as plt
from matplotlib import font_manager
import csv

# 设置font，支持中文
my_font = font_manager.FontProperties(fname="./Resource/STSONG.TTF")
address_count = set()

class dataForm:
    """
    本类适用于生成连续的时间。包括时，天，月。
    数据用于数据分析，只考虑今年的情况-----2018年。
    hours:# 用于生成2020年的任意一个月份的每天的时间字典。单位是小时
    """
    #hours_dic = {}
    days_dic={}
    months_dic={}
    def __init__(self):
        pass
    def hours(self,num):
        hours_dic = {}
        if num in [1, 3, 5, 7, 8, 10, 12]:
            for day in range(1,32):
                day_to_str="2020-"+str(num).zfill(2)+"-"+str(day).zfill(2)
                for h in range(24):
                    hour = day_to_str + " "+str(h).zfill(2)+":00:00"
                    hours_dic[hour]=[0,self.FormatToStamp(hour)]
        elif num == 2:
            for day in range(1,29):
                day_to_str="2020-"+str(num).zfill(2)+"-"+str(day).zfill(2)
                for h in range(24):
                    hour = day_to_str + " "+str(h).zfill(2)+":00:00"
                    hours_dic[hour]=[0,self.FormatToStamp(hour)]
        elif num in [4, 6, 9, 11]:
            for day in range(1,31):
                day_to_str="2020-"+str(num).zfill(2)+"-"+str(day).zfill(2)
                for h in range(24):
                    hour = day_to_str + " "+str(h).zfill(2)+":00:00"
                    hours_dic[hour]=[0,self.FormatToStamp(hour)]
        else:
            print("输入格式不正确")
        return hours_dic
    def days(self):
        pass
    def months(self):
        pass
    def years(self):
        pass
    def FormatToStamp(self,string):
        #转成Unix时间戳
        flag = True
        while flag:
            try:
                formatTime = string.strip()
                formatTime = time.mktime(time.strptime(formatTime, '%Y-%m-%d %X'))
                return formatTime
            except Exception as e:
                print("转换失败，请重新输入。失败原因：%s" % e)



def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print('URL format error!')


def filter_data(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        data=re.search('\w+\.(com|cn|net|tw|la|io|org|cc|info|cm|us|tv|club|co|in)',sublevel_split[0])
        if data:
            return data.group()
        else:
            address_count.add(sublevel_split[0])
            return "ok"
    except IndexError:
        print('URL format error!')


def FormatToStamp():
    flag=True
    while flag:
        try:
            formatTime=input("请输入时间（格式：2018-06-24 11:50:00）").strip()
            formatTime=time.mktime(time.strptime(formatTime,'%Y-%m-%d %X'))
            return formatTime
        except Exception as e:
            print("转换失败，请重新输入。失败原因：%s"%e)

            
def analyze(results):
    #条形图
    prompt = input("[.] Type <c> to print or <p> <b>to plot\n[>] ")

    if prompt == "c":
        with open('./history.txt', 'w') as f:
            for site, count in results.items():
                f.write(site + '\t' + str(count) + '\n')
    elif prompt == "p":
        key = []
        value = []
        for i in results:
            key.append(i[0])
            value.append(i[1])
        n = 25
        X=range(n)
        Y = value[:n]#数量

        plt.bar( X,Y, align='edge')
        plt.xticks(rotation=-90,fontproperties=my_font)
        plt.xticks(X, key[:n])
        for x, y in zip(X, Y):
            plt.text(x + 0.4, y + 0.05, y, ha='center', va='bottom')



        plt.show()
    elif prompt == "b":
        history_lst = [(url, count) for url, count in results]
        history_lst.sort(key=lambda item: item[1], reverse=True)

        top_20_url = history_lst[:20]
        # 获得饼状图数据
        pie_data = [item[1] for item in top_20_url]
        # 获得label
        pie_labels = [item[0] for item in top_20_url]

        plt.figure(1, figsize=(10, 10))
        plt.title('访问频率排名前20的网站', fontproperties=my_font)
        plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
        plt.show()
        plt.savefig('./浏览频率前20的网站.pdf')
    else:
        print("[.] Uh?")
        quit()


def analyze2(results):
    print("我一看就知道你要打印折线图")
    key=[]
    value=[]
    for i in results:
        key.append(i[0])
        value.append(i[1])
    n = 20
    X = key[:n]
    Y = value[:n]

    plt.plot(X,Y,label="number count")
    plt.xticks(rotation=-90,fontproperties=my_font)
    plt.xlabel('webname')
    plt.ylabel('numbers')
    plt.title('number count')
    plt.show()

def analyzeKey(results):
    #条形图
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 有中文出现的情况，需要u'内容'
    print("I will generate histograms directly ！！")
    key = []
    value = []
    for i in results:
        key.append(i[0])
        value.append(i[1])
    n = 20
    X=range(n)
    Y = value[:n]#数量

    plt.bar( X,Y, align='edge',color="g")
    plt.xticks(rotation=-90,fontproperties=my_font)
    plt.xticks(X, key[:n])
    for x, y in zip(X, Y):
        plt.text(x + 0.4, y + 0.05, y, ha='center', va='bottom')
    plt.show()


def analyzeSearch_engine(results):
    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    slices=[]
    activities=[]
    for i,j in results.items():
        activities.append(i)
        slices.append(j)
    cols=['c','m','y','b']#给饼图配颜色
    num=len(slices)#取到一个需要几个数组
    cols=cols[:num]#需要一个颜色，取几个
    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            # shadow=True,
            # explode=(0,0,0,0.1),
            autopct='%1.1f%%')
    plt.title(u"搜索引擎使用占比")
    plt.show()

def analyzeCount(results):
     #折线图
    a=dataForm()#定义一个时间生成对象
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 有中文出现的情况，需要u'内容'
    def go(string):
        col=['black','brown','red','goldenrod',"blue","y","g"]
        s_to=string
        for i,j in enumerate(col):
            # s=string[:8]+str(int(string[-2:])-i)
            select_day = a.FormatToStamp("%s 00:00:00" % s_to)-i*86400*2
            keys = []
            values = []
            for line in results:
                if select_day < line[1][1]:
                    keys.append(line[0][-11:-3])
                    values.append(line[1][0])
            # x = keys[:48]
            x=range(48)
            y = values[:48]
            plt.plot(x, y, label="%s 登陆网站走势图" %(time.strftime("%Y-%m-%d %X",time.localtime(select_day))), color=j)
            plt.xticks(x, rotation=0)
    go("2020-08-25")

    plt.xlabel('当日时刻：小时')
    plt.ylabel('登陆次数：次')
    plt.title("用户登陆网站48小时走势图")
    plt.legend()
    plt.show()


def analyzeCount2(results):
     #散点图
    a=dataForm()#定义一个时间生成对象
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 有中文出现的情况，需要u'内容'
    def go(string):
        col=['black','brown','red','goldenrod',"blue","y","g"]
        s_to=string
        for i,j in enumerate(col):
            # s=string[:8]+str(int(string[-2:])-i)
            select_day = a.FormatToStamp("%s 00:00:00" % s_to)-i*86400*2
            keys = []
            values = []
            for line in results:
                if select_day < line[1][1]:
                    keys.append(line[0][-11:-3])
                    values.append(line[1][0])
            # x = keys[:48]
            x=range(48)
            y = values[:48]
            plt.scatter(x, y, label="%s 登陆网站散点图" %(time.strftime("%Y-%m-%d %X",time.localtime(select_day))))
            plt.xticks(x, rotation=0)
    go("2020-08-25")

    plt.xlabel('当日时刻：小时')
    plt.ylabel('登陆次数：次')
    plt.title("用户登陆网站48小时走势图")
    plt.legend()
    plt.show()


def drawurl():
    conn,cur = allconnect()
    SQL="SELECT urls.url,urls.title,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    newdata = {}
    for line in res:
        url = filter_data(line[0])
        item = line[1]
        if url in newdata:
            newdata[url] +=1
        else:
            newdata[url] = 1
    del newdata["ok"]
    sites_count_sorted = sorted(newdata.items(),key=lambda item:item[1],reverse=True)
    # print(sites_count_sorted[:25])
    analyze(sites_count_sorted)
    allclose(conn,cur)


def drawtitle():
    conn,cur = allconnect()
    SQL="SELECT urls.url,urls.title,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    newdata = {}
    newres = []
    for line in res:
        url = filter_data(line[0])
        title = line[1]
        if title is '':
            continue
        if title in newdata:
            newdata[title] += 1
        else:
            newdata[title]  = 1
        visit_time = time.strftime("%Y-%m-%d %X",time.localtime((line[2] / 1000000) - 11644473600))
        newres.append([url,title,visit_time])
    sites_count_sorted = sorted(newdata.items(),key=lambda item:item[1],reverse=True)
    # print(sites_count_sorted[:25])
    analyze2(sites_count_sorted)
    allclose(conn,cur)


def drawkeywords():
    conn,cur = allconnect()
    SQL = "SELECT keyword_search_terms.term,urls.url,urls.visit_count,urls.last_visit_time from keyword_search_terms LEFT JOIN urls on keyword_search_terms.url_id=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    newdata = []
    ky_count={}#统计关键词数量
    search_engines_count={}#统计搜索引擎使用数量
    for item in res:
        keyword=item[0]
        url= filter_data(item[1])
        count=item[2]
        last_vist_time=time.strftime("%Y-%m-%d %X",time.localtime((item[3] / 1000000) - 11644473600))
        newdata.append([keyword,url,count, last_vist_time])
        if keyword in ky_count:
            ky_count[keyword]+=1
        # elif url in search_engines_count:
        #     search_engines_count[url]+=1
        else:
            ky_count[keyword]=1
            # search_engines_count[url] = 1

    # for i in new_data:
    # print(new_data)
    # print(ky_count)
    # print(search_engines_count)
    #对关键词进行排序
    ky_count_sorted = sorted(ky_count.items(), key=lambda item: item[1], reverse=True)
    analyzeKey(ky_count_sorted)
    allclose(conn,cur)


def drawsearch_engines():
    conn,cur = allconnect()
    SQL = "SELECT keyword_search_terms.term,urls.url,urls.visit_count,urls.last_visit_time from keyword_search_terms LEFT JOIN urls on keyword_search_terms.url_id=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    newdata = []
    ky_count={}#统计关键词数量
    search_engines_count={}#统计搜索引擎使用数量
    for item in res:
        keyword=item[0]
        url= filter_data(item[1])
        count=item[2]
        last_vist_time=time.strftime("%Y-%m-%d %X",time.localtime((item[3] / 1000000) - 11644473600))
        newdata.append([keyword,url,count, last_vist_time])
        if url in search_engines_count:
            search_engines_count[url]+=1
        else:
            search_engines_count[url] = 1

    analyzeSearch_engine(search_engines_count)
    allclose(conn,cur)


def drawCountondays():
    conn,cur = allconnect()
    SQL="SELECT urls.url,urls.title,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    allclose(conn,cur)
    new_data1=[]#统计每小时访问网站数量
    new_data2=[]#统计每天的访问网站数量
    new_data3=[]#统计每月的访问网站数量
    for num,item in enumerate(res):
        new_data1.append([item, time.strftime("%Y-%m-%d %H", time.localtime((item[2] / 1000000) - 11644473600))+":00:00"])
        new_data2.append([item, time.strftime("%Y-%m-%d", time.localtime((item[2] / 1000000) - 11644473600))])
        new_data3.append([item, time.strftime("%Y-%m", time.localtime((item[2] / 1000000) - 11644473600))])

    new_data_hours = {}  # 统计每小时访问网站数量
    new_data_days = {}  # 统计每天的访问网站数量
    new_data_months = {}  # 统计每月的访问网站数量

    
    a = dataForm()
    ##############  统计每小时访问网站数量 #############################################
    for item in new_data1:
        if item[1] in new_data_hours:
            new_data_hours[item[1]][0]+=1
        elif item[1] not in new_data_hours:
            num=item[1][5:7]
            hours_dic = a.hours(int(num))
            new_data_hours.update(hours_dic)
            new_data_hours[item[1]][0]=1
    # print("统计每小时访问网站数量", new_data_hours)
    #对数据进行排序
    new_data_hours_sorted=sorted(new_data_hours.items(), key=lambda item: item[0])
    # for i in new_data_hours_sorted:
    #     print(i)
    analyzeCount(new_data_hours_sorted)


    #print("统计每小时访问网站数量", new_data_hours)
    # for item in new_data2:
    #     if item[1] in new_data_days:
    #         new_data_days[item[1]]+=1
    #     else:
    #         new_data_days[item[1]]=1
    # print("统计每天的访问网站数量",new_data_days)
    # for item in new_data3:
    #     if item[1] in new_data_months:
    #         new_data_months[item[1]]+=1
    #     else:
    #         new_data_months[item[1]]=1
    #
    # print("统计每月的访问网站数量",new_data_months)



#生成以天为单位的浏览集合
def visitondays():
    conn,cur = allconnect()
    SQL="SELECT urls.url,urls.title,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id"
    cur.execute(SQL)
    res = cur.fetchall()
    newdata = {}
    newres = []
    for line in res:
        url = parse(line[0])
        if url == '':
            continue
        title = line[1]
        if title is '':
            continue
        if title in newdata:
            newdata[title] += 1
        else:
            newdata[title]  = 1
        visit_time = time.strftime("%Y%m%d",time.localtime((line[2] / 1000000) - 11644473600))
        newres.append([url,title,visit_time])
    newres.sort(key=lambda item:item[2],reverse=True)
    lenres = len(newres)
    tempE = set()
    resdata = []
    for i in range(1,lenres):
        if newres[i-1][2] == newres[i][2] or int(newres[i-1][2]) == int(newres[i][2])+1:
            tempE.add(newres[i-1][0])
        else:
            tempE.add(newres[i-1][0])
            if len(tempE) >=5:
                resdata.append(tempE)
            tempE = set()
    allclose(conn,cur)
    return resdata


def allconnect():
    conn = sqlite3.connect('./Resource/History.db')
    cur = conn.cursor()
    return conn,cur


def allclose(conn,cur):
    cur.close()
    conn.close()


def write_to_apriori(dataSet):
    with open('./Resource/apriori.csv','w',encoding='utf-8',newline='') as csvf:
        writer = csv.writer(csvf,delimiter=',')
        writer.writerows(dataSet)


def write_to_KNNtrainning():
    conn,cur = allconnect()
    SQL="SELECT url,title from urls"
    cur.execute(SQL)
    res = cur.fetchall()
    with open('./Resource/KNNtrainning.csv','w',encoding='utf-8',newline='') as csvf:
        writer = csv.writer(csvf,delimiter=',')
        writer.writerows(res)
    allclose(conn,cur)


if __name__ == "__main__":
    # drawsearch_engines()
    drawCountondays()
    # drawurl()
    # drawkeywords()
    # drawtitle()