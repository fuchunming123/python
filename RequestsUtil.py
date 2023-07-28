import requests


def downFile(fileName, url, headers, payload, **kwargs):
    re = requests.get(url=url, json=payload, headers=headers, params=payload, **kwargs)
    o = open(fileName, "wb").write(re.content)


def requestGet(url, headers, payload, **kwargs):
    print("请求：" + url)
    print("参数：" + str(payload))
    re = requests.get(url=url, json=payload, headers=headers, params=payload, **kwargs)
    print(str(re.text))
    return re;


def requestPost(url, headers, payload, **kwargs):
    print("请求：" + url)
    print("参数：" + str(payload))
    re = requests.post(url=url, json=payload, headers=headers, params=payload, **kwargs)
    print(str(re.text))
    return re;

def requestPost1(url, headers, payload, **kwargs):
    print("请求：" + url)
    print("参数：" + str(payload))
    re = requests.post(url=url, data=payload, headers=headers, **kwargs)
    print(str(re.text))
    return re;



def request(moth, url, headers, payload, **kwargs):
    re = requests.put(url=url, json=payload, headers=headers, params=payload, **kwargs)
    return re


def uploadFile(fileName, url, headers, payload, **kwargs):
    file = open(fileName, "rb")
    # with open(fileName) as f:
    # response = requests.post(url, files={"form_field_name": file}, data=payload, headers=headers)
    payload['file'] = file
    kwargs['timeout'] = 10000
    headers['timeout'] = 10000
    response = requests.request(method="post", url=url, params=payload, headers=headers, **kwargs)

    return response
