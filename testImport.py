
import requests

import RequestsUtil

def sendPost(url,files,data):
    response=requests.post(url,files=files,data=data,headers=header)
    return response.json()

if __name__ == "__main__":
    header = {'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Connection': 'keep-alive',
              'Content-Length': '7215',
              'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryhiEElp3sQnAaQj1o',
              'Cookie': 'access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE4MTY0MTMsInVzZXJfbmFtZSI6ImNvbS5qYi5jb3JlLm1vZGVsLlVzZXJNb2RlbEBmNmVhZDBlMSIsImF1dGhvcml0aWVzIjpbIlJPTEVfU1VQRVIiXSwianRpIjoiY2E5ZTE3N2ItNzY5Yy00NDgzLWIwZDItYTNiZDM5MGQ3YWFiIiwiY2xpZW50X2lkIjoiZjFhdXRvYXV0aCIsInNjb3BlIjpbIndyaXRlIl19.z5dbzGKITkDQ0nTdeL07LahirHdhJcX5nTKA_9KXf2M; SESSION=Yzc3OTEyNWItYjg3OC00ODJlLTkzM2MtMDljNmFlZWFlZmYz',
              'Host': '192.168.1.161:10415',
              'Origin': 'http://192.168.1.161:10415',
              'Referer': 'http://192.168.1.161:10415',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


    file = open('C:\\Users\\fcm\\Desktop\\新建 Microsoft Excel 工作表.xlsx', "rb")
    files = [
        ('file', (
            '新建 Microsoft Excel 工作表.xlsx',  # 文件名称
            open('C:\\Users\\fcm\\Desktop\\新建 Microsoft Excel 工作表.xlsx', 'rb'),  # 读取文件
            'application/octet-stream'
        ))
    ]
    files1 = {
        'file': open('C:\\Users\\fcm\\Desktop\\新建 Microsoft Excel 工作表.xlsx', 'rb')
    }
    re=requests.post(url="http://192.168.1.161:10415/importXlsxController/importXlsx", headers=header,
                         files=files1)
    print(re)
    # 获取文件

