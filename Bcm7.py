import concurrent.futures
import json
import os
import random
import time
import traceback

import requests

#存入的路径

rootPath = 'F:/BCM/'
authorization = 'eyJraWQiOiJkNmYyNmY5Yi00ZWZjLTRhN2MtYjVhMy0zMmE1NmY5YzAwZDciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjQ5NDk2MTgiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2ODczMzQ5MjUsImlhdCI6MTY4NzMyNzcyNSwianRpIjoiQUFBQmlOeVIxcV9RZDQ3RGgtTkp1Q0xfeE5ORjhsbjYifQ.FNOk8PF7DMPIALWrTMtzsELOhsPE7MpzP4NGiBrz1b2rPiTo-1tCa_h5-OrcHOHV5iVTc4fzHQwgaooqHTqXx15tEzeZUB8n-Ir9sak-BFVNWE_3L-3swj2LURaDkICSpeLFxAipuDchwaIi7KAV3-6wavPEYN38b55v8qckPgRAuAzO2-C4blwfb6kGSR-SNkLamIjtFlnEz_JNBO53vH9B2_2uJgi7yfaRKk77O2KxFdpD1e8mY3f9fQscI8eivj_8bkawFWqLPdJkm4yz7VwF17OqWPKnVp5-doi56zEQKuQKTEm011SmthagPij-JFWFsN3vLT5YYcr7UwVFeA'
time1 = str(int(time.time() * 1000))
def downLoad(resource_path, zyFl, zyName, xmName):
    url = 'https://eduzone.codemao.cn/edu/qiniu/resource/url'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': authorization,
        'Authorization_Type': '3',
        'Content-Length': '50',
        'Connection': 'close',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'eduzone.codemao.cn',
        'Origin': 'https://teacher.edu.codemao.cn',
        'Referer': 'https://teacher.edu.codemao.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    payload = {
        'resource_path': resource_path
    }
    response = requests.post(url, json=payload, headers=headers,verify=False)
    jresponse = response.json()
    print(jresponse)
    print(jresponse['resource_url'])
    pdf = requests.get(jresponse['resource_url'])
    #判断一个目录是否存在
    spl = resource_path.split("/")
    path = rootPath + xmName + '/' + zyName
    f = os.path.exists(path)
    # 目录存在
    if f == False :
        #多层创建目录
        os.makedirs(path)

    with open(path + '/' + spl[spl.__len__() - 1], "wb") as code:
        code.write(pdf.content)

def downItems(items, item, zyFl, zyName, xmName):
    if item in items:
        myitem = items[item]
        for i in myitem:
            time.sleep(1)
            try:
                downLoad(i['resource_url'], zyFl, zyName, xmName)
            except BaseException:
                traceback.print_exc()

def getJson(url):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': authorization,
        'Authorization_Type': '3',
        'Content-Length': '50',
        'Connection': 'close',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'eduzone.codemao.cn',
        'Origin': 'https://teacher.edu.codemao.cn',
        'Referer': 'https://teacher.edu.codemao.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    payload = {
    }
    response = requests.get(url, json=payload, headers=headers)
    jresponse = response.json()
    return jresponse

def getItems(packag, name, index):
    #https://eduzone.codemao.cn/edu/zone/lesson/offical/lessons/4559/view?TIME=1687317247477
    url = 'https://eduzone.codemao.cn/edu/zone/lesson/offical/lessons/'+str(packag)+'/view?TIME='+time1+''
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': authorization,
        'Authorization_Type': '3',
        'Content-Length': '50',
        'Connection': 'close',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'eduzone.codemao.cn',
        'Origin': 'https://teacher.edu.codemao.cn',
        'Referer': 'https://teacher.edu.codemao.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    payload = {
    }
    response = requests.get(url, json=payload, headers=headers)
    jresponse = response.json()
    print('下载资源：' + str(jresponse['name']))
    print('item：' + str(jresponse))
    zyName = '【第'+str(index) + '课】' + jresponse['name'];
    # 下载资源
    downItems(jresponse, 'attachment_url', 'attachment', zyName, name)
    downItems(jresponse, 'courseware_url', 'courseware', zyName, name)
    downItems(jresponse, 'material_url', 'material', zyName, name)
    downItems(jresponse, 'mind_mapping_url', 'mind_mapping', zyName, name)
    downItems(jresponse, 'mission_url', 'mission', zyName, name)
    downItems(jresponse, 'teaching_plan_url', 'teaching_plan', zyName, name)
    downItems(jresponse, 'test_url', 'test', zyName, name)
    downItems(jresponse, 'video_url', 'video', zyName, name)

def getXm(id, name, ff):
    json = getJson('https://eduzone.codemao.cn/edu/zone/lesson/offical/lessons?package_id='+str(id)+'&page=1&limit=100&TIME='+time1+'')
    print('获取到Xm')
    print(json)
    index = 1
    for xm in json['items'] :
        print(xm)
        if ff :
            getItems(xm['id'], name, index)
        else:
            getBk(xm['id'], name, index)
        index = index + 1;
        #break

def getXms():
    json = getJson('https://eduzone.codemao.cn/edu/zone/lesson/offical/packages?pacakgeEntryType=1&topicType=all&topicId=all&tagId=all&page=1&limit=150&TIME='+time1)
    print('获取到Xms')
    print(json)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for xm in  json['items']:
            executor.submit(getXm, xm['id'], xm['name'], xm['status'] == 1)
    return json

def getBk(id, zyName, index):
    json = getJson('https://eduzone.codemao.cn/edu/zone/lesson/offical/lessons/detail/'+str(id)+'?TIME=1687326689923')
    print(json)
    #for item in json['fileUrl']:
    #    downLoad(item['url'], '', '【第'+str(index) + '课】' + json['name'], zyName)

if __name__ == "__main__":
    getXms()
    #getItems(4559,'aaaaa')
#downLoad('177,,《源码入门课》课后测试.png', 'sss', 'zyName', 'xmNc')
#getBk(569, "", "")
    #getXm(429, 'Python编程-小高入门', False)



