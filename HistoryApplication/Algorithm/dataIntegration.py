import sqlite3


def IntegrationWithDB(dbA):
    conn,cur = connect()
    connA = sqlite3.connect('./Resource/{}'.format(dbA))
    curA = connA.cursor()
    selectorURL = 'select * from urls'
    selectorVISIT = 'select urls.url,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id'
    selectorKey = 'select urls.url, keyword_search_terms.term from keyword_search_terms LEFT JOIN urls on keyword_search_terms.url_id=urls.id'
    curA.execute(selectorURL)
    resUrl = curA.fetchall()
    for line in resUrl:
        # cur.execute('INSERT OR REPLACE INTO keyword_search_terms(url,title,visit_count,typed_count,last_visit_time,hidden) VALUES (?,?,?,?,?,?)',line[1:])
        cur.execute('select * from urls where url = ?',(line[1],)) #需要传递一个序列，但是忘记了逗号使您的参数成为元组
        url = cur.fetchall()
        if url != []:
            last_visit_time = line[5] if line[5] > url[0][5] else url[0][5]
            cur.execute('update urls SET visit_count = ? , last_visit_time = ? WHERE id=?',(url[0][3]+1,last_visit_time,url[0][0]))
        else:
            cur.execute('insert into urls(url,title,visit_count,typed_count,last_visit_time,hidden) VALUES (?,?,?,?,?,?)',line[1:])
    conn.commit()
    curA.execute(selectorVISIT)
    resVisit = curA.fetchall()
    for line in resVisit:
        cur.execute("select visits.id,visits.url,visits.visit_time from visits LEFT JOIN urls on visits.url=urls.id where urls.url = ? and visits.visit_time = ?",line)
        visit = cur.fetchall()
        if visit == []:
            cur.execute('select id from urls where url = ?',(line[0],))
            ur = cur.fetchall()
            cur.execute('insert into visits(url,visit_time) VALUES (?,?)',(ur[0][0],line[1]))
    conn.commit()
    curA.execute(selectorKey)
    resKey = curA.fetchall()
    for line in resKey:
        cur.execute('select keyword_search_terms.keyword_id,keyword_search_terms.url_id,keyword_search_terms.term from keyword_search_terms LEFT JOIN urls on keyword_search_terms.url_id=urls.id where urls.url = ? and keyword_search_terms.term = ?',line)
        key = cur.fetchall()
        if key == []:
            cur.execute('select id from urls where url = ?',(line[0],))
            ur = cur.fetchall()
            cur.execute('insert into keyword_search_terms(keyword_id,url_id,term,normalized_term) VALUES (?,?,?,?)',(2,ur[0][0],line[1],line[1]))
    conn.commit()
    curA.close()
    connA.close()
    close(conn,cur)

def connect():
    conn = sqlite3.connect('./Resource/History.db')
    cur = conn.cursor()
    return conn,cur


def close(conn,cur):
    cur.close()
    conn.close()


def IntegrationWithRecord():
    conn,cur = connect()
    with open('./Resource/sql.txt','r',encoding='gb2312') as f:
        data = f.readlines()
        for line in data:
            line = line.split(',')
            cur.execute('select * from urls where url = ?',(line[1],)) #需要传递一个序列，但是忘记了逗号使您的参数成为元组
            url = cur.fetchall()
            if url != []:
                last_visit_time = float(line[2]) if float(line[2]) > url[0][5] else url[0][5]
                cur.execute('update urls SET visit_count = ? , last_visit_time = ? WHERE id=?',(url[0][3]+1,last_visit_time,url[0][0]))
            else:
                cur.execute('insert into urls(url,title,last_visit_time) VALUES (?,?,?)',(line[1],line[0],line[2].strip()))
            cur.execute('select * from urls where url = ?',(line[1],)) #需要传递一个序列，但是忘记了逗号使您的参数成为元组
            ur = cur.fetchall()
            cur.execute('insert into visits(url,visit_time) VALUES (?,?)',(ur[0][0],line[2].strip()))
        conn.commit()
        close(conn,cur)


# IntegrationWithRecord()
# IntegrationWithDB('History1.db')
# 验证合并成功与否
# conn,cur = connect()
# selectorKey = "select * from urls where urls.title = 'A股：震荡加大！下周，A股走势展望'"
# cur.execute(selectorKey)
# resUrl = cur.fetchall()
# for line in resUrl:
#     print(line)
# conn,cur = connect()                                            
# sql = 'select id,last_visit_time from urls where last_visit_time<13200000000000000'
# sql1 = 'select id,visit_time from visits where visit_time<13200000000000000'
# cur.execute(sql)
# ret = cur.fetchall()
# for line in ret:
#     visit_time = line[1]-11644473600 *10 **6
#     cur.execute('update urls set last_visit_time = ? where id =?',(visit_time,line[0]))
# conn.commit()

# cur.execute(sql1)
# ret1 = cur.fetchall()
# for line in ret1:
#     visit_time1 = line[1] -11644473600 *10 **6
#     cur.execute('update visits set visit_time = ? where id =?',(visit_time,line[0]))
# conn.commit()
