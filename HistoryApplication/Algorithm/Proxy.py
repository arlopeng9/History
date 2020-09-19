from mitmproxy import ctx, flow
import json,re,datetime
import os
# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):
    # 获取请求对象
    request = flow.request
    # 实例化输出类
    info = ctx.log.info
    # # 打印请求的url
    # info(request.url)
    # # 打印请求方法
    # info(request.method)
    # # 打印host头
    # info(request.host)
    # # 打印请求端口
    # info(str(request.port))
    # # 打印所有请求头部
    # info(str(request.headers))
    # # 打印cookie头
    # info(str(request.cookies))

# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    # 获取响应对象
    response = flow.response
    # 实例化输出类
    info = ctx.log.info
    if 'text/html' in response.headers['content-type']:  # 过滤掉不需要数据包
        # # 打印响应码
        info(str(response.status_code))
        # # 打印所有头部
        # info(str(response.headers['content-type']))
        # # 打印cookie头部
        # info(str(response.cookies))
        # # 打印响应报文内容
        # info(str(response.text))
        with open('./Resource/sql.txt','a',encoding='gb2312') as f:
            html = decode_response_text(response.content)
            if gettitle(html) != '':
                info(str(gettitle(html)))
                f.write(str(gettitle(html))+',')
                info((flow.request.url))
                f.write(flow.request.url+',')
                # f.write(response.headers['date']+'\t')
                info(response.headers['date'])
                f.write(str(int((response.timestamp_end + 11644473600) * 10**7))+'\n')


def gettitle(html):
    pattern = re.compile(u'<title>(.*?)</title>',re.S)
    res = re.findall(pattern, html)
    if len(res) > 0:
        return res[0]
    return ''

def decode_response_text(content):
    for _ in ['UTF-8', 'GB2312', 'GB2312', 'iso-8859-1', 'big5']:
        try:
            return content.decode(_)
        except :
            continue
    return content


def timestamp2string(timeStamp): 
    try: 
        d = datetime.datetime.fromtimestamp(timeStamp) 
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f") 
        # 2015-08-28 16:43:37.283000' 
        return str1 
    except Exception as e: 
        print(e)
        return '' 


def str2timestamp(str_time): 
    try: 
        d = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
        time = d.timestamp() * 10**6
        # 2015-08-28 16:43:37.283000' 
        return str(int(time))
    except Exception as e: 
        print(e)
        return '' 


# if __name__ == "__main__":
#     sql = []
#     with open('./Resource/sql.txt','r',encoding='gb2312') as f:
#         data = f.readlines()
#         for line in data:
#             line = line.split(',')
#             line[2] = str2timestamp(line[2].strip())
#             sql.append(line)
#             print(line)


#     with open('./Resource/sql.txt','w',encoding='gb2312') as f:
#         for line in sql:
#             f.writelines(','.join(line)+'\n')