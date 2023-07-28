import json
import os
import random
import time

import requests

rootPath = 'F:/'
authorization = 'Bearer eyJraWQiOiI4MjY5Y2U2NS01NzE5LTQyMzMtOGZmMi04OTgwZjUwOTgwOWMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoid2ViIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjM4NDQ2NzIiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2MjA0Njk4MzAsImlhdCI6MTYyMDQ2MjYzMCwianRpIjoiQUFBQmVVc1pkcE43SXVCX0tnZXFudXhpYTh3MzVCREoifQ.cjRgU774L_R19EnYrBC2_9m_cK2ip7C9gBigazOoBcIJazKsLBzwYFC-0u3ol5ZiYXEXqAfpggckwTG_tNC_gwYwMXfkZpDRZItwcu8NrhAHZvzvXZMlWXm0xL6bCZ_iLZpmG3y1_wvlC6tJvFGz5hFX1OUBHgIZ3BiZFkrC8svnu34kyv7D6qWnQX1FIrV78vbz0N52PP4LXB3Ph3YB6KKKixfZd7pwr6ywCl9mTAu_g6-E19WbRD46t0NlHQh5PeSQ4OH7j4iFDWEM52AFJ7s6ss_fLLMn-TebO_No9pJDsxMrXo3suATw3-vFZGoG_fW4-LzEQcEDeD2hC2j57A'
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
    path = rootPath + xmName + '/' + zyName
    f = os.path.exists(path)
    # 目录存在
    if f == False :
        #多层创建目录
        os.makedirs(path)
    with open(path + resource_path[resource_path.find('/'):] , "wb") as code:
        code.write(pdf.content)

def downItems(items, zyFl, zyName, xmName):
    time.sleep(random.randint(2,5))
    for item in items:
        time.sleep(random.randint(2,5))
        downLoad(item['resource_url'], zyFl, zyName, xmName)

def getName(packag):
    url = 'https://eduzone.codemao.cn/edu/zone/lesson/offical/packages/'+packag+'?TIME=1620462655061'
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

def getItems(packag):
    name = getName(packag)
    print(name)
    url = 'https://eduzone.codemao.cn/edu/zone/lesson/offical/lessons?page=1&package_id='+packag+'&limit=100&TIME=1620462655061'
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
    items = jresponse['items']
    for item in items:        # 循环
        print('下载资源：' + str(item['name']))
        print('item：' + str(item))
        # 下载资源
        downItems(item['attachment_url'], 'attachment', item['name'], name['name'])
        downItems(item['courseware_url'], 'courseware', item['name'], name['name'])
        downItems(item['material_url'], 'material', item['name'], name['name'])
        downItems(item['mind_mapping_url'], 'mind_mapping', item['name'], name['name'])
        downItems(item['mission_url'], 'mission', item['name'], name['name'])
        downItems(item['teaching_plan_url'], 'teaching_plan', item['name'], name['name'])
        downItems(item['test_url'], 'test', item['name'], name['name'])
        downItems(item['video_url'], 'video', item['name'], name['name'])

if __name__ == "__main__":

    #pages = '46'
    #getItems(pages)
    #print(str[str.find('/'):])
    url = 'https://sapi.guanfu.cn/shop/product/6879323406580322304'
    headers = {
            'out_ver': '1.1.17',
            'ver': '30',
            'device': 'A',
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; Mi 10 Build/RKQ1.200826.002)',
            'Host': 'sapi.guanfu.cn',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
    }
    response = requests.get(url=url, headers=headers)
    jresponse = response.json()
    print(jresponse)



