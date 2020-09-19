import json
import requests
from scapy.all import *
from scapy.layers import http
api_key = ''


def getData(domain):
    query = 'https://api.similarweb.com/v1/website/{}/similar-sites/similarsites?api_key={}&start_date=2020-05&end_date=2020-06&format=json'.format(domain,api_key)
    response = requests.get(query)
    j = json.loads(response.text)
    print(j)


def processStr(data):
    pattern = re.compile('^b\'(.*?)\'$', re.S)
    res = re.findall(pattern, str(data))
    print(res)
    print(str(data))
    final = re.split('\\\\r\\\\n', res[0])
    return final


# if __name__ == "__main__":
#     # getData('facebook.com')
    packets = sniff(count = 100)
    wrpcap("./Resource/test.pcap",packets)
    # packets = rdpcap('./Resource/test.pcap')
    load = packets[40]['Raw'].load
    items = processStr(load)
    for i in items:
        print(i)
    # for p in packets:
    #     for f in p.payload.payload.payload.fields_desc:
    #         fvalue = p.payload.payload.getfieldval(f.name)
    #         reprval = f.i2repr(p.payload.payload, fvalue)# 转换成十进制字符串
    #         if 'HTTP' in reprval:
    #             lst = str(reprval).split(r'\r\n')
    #             for l in lst:
    #                 print(l)
    # count = 0
    # while count<10:
    #     count = count+1
    #     packets = sniff(count = 10)
    #     for p in packets:
    #         if 'TCP' in p:
    #             print('=' * 78)
    #             Ether_name = p.name
    #             Ether_dst =  p.dst


    #             Ether_src = p.src
    #             IP_name = p.payload.name
    #         # IP_proto = p.payload.proto
    #             IP_src = p.payload.src
    #             IP_dst = p.payload.dst

    #             print(Ether_name)
    #             print('dst : ' + Ether_dst)
    #             print('src : ' + Ether_src)

    #             print(IP_name)
    #             # print('protcol : ' + IP_proto)
    #             print('src : ' + IP_src)
    #             print('dst : ' + IP_dst)
    #             if p.haslayer(http.HTTPRequest):
    #                 print("*********request******")
    #                 http_name = 'HTTP Request'
    #                 http_header = p[http.HTTPRequest].fields
    #                 headers = http_header['Headers']
    #                 items = processStr(headers)
    #                 for i in items:
    #                     print(i)

    #             elif p.haslayer(http.HTTPResponse):
    #                 print("*********response******")
    #                 http_name = 'HTTP Response'
    #                 http_header = p[http.HTTPResponse].fields
    #                 headers = http_header['Headers']
    #                 items = processStr(headers)
    #                 for i in items:
    #                     print(i)

    #                 if 'Raw' in p:
    #                     load = p['Raw'].load
    #                     items = processStr(load)
    #                     for i in items:
    #                         print(i)
