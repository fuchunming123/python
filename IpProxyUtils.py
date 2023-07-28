# 用到的库
import json
import os
import random
import traceback

import bs4
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class IpProxyUtils:
    # 获取Ip池网站
    __proxyUrl = 'http://www.goubanjia.com/'
    # 是否使用代理IP
    __isProxy = False
    # 本地缓存的IP池
    __ipList = []

    def __init__(self, proxyUrl, isProxy):
        if proxyUrl is not None:
            self.__proxyUrl = proxyUrl
        if isProxy is not None:
            self.__isProxy = isProxy

    # 随机产生一个User-Agent
    def mkUser_Agent(self):
        try:
            header = self.ua.random
        except:
            print("获取User_Agent失败")
            traceback.print_exc()
        return header

    # 模仿浏览器头部信息
    def mkHead(self):
        # 随机产生一个User-Agent
        userAgent = self.mkUser_Agent()
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'utf-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
        }
        return header

    ua = UserAgent()

    def getIp(self):
        if self.__ipList == []:
            self.getProxyIp()
            print("代理ip池为空,正在初始化ip池")
            if self.__ipList != []:
                ip = random.choice(self.__ipList)
                return ip
            else:
                return None
        else:
            ip = random.choice(self.__ipList)
            return ip

    def getProxyIp(self):
        if self.__ipList != []:
            return
        # 读取本地缓存IpProxy
        textIpProxy = open('IpProxy.text', 'w')
        # 文件为空
        if os.path.getsize('IpProxy.text') == 0:
            # 获取Web上的Ip
            response = self.getIpListWeb()
            # 将list装成Json字符串并写入本地文件
            textIpProxy.write(json.dumps(response, indent=2, ensure_ascii=False))
            textIpProxy.flush()
            textIpProxy.close()
        text = open('IpProxy.text').read()
        responseJson = json.loads(text)
        self.__ipList = responseJson

    """
        读取URL
    """

    def readWeb(self, url):
        head = self.mkHead()
        if self.__isProxy:
            proxy = self.getIp()
            response = requests.get(url=url, headers=head, proxies=proxy, timeout=(3, 7))
            if response.status_code == 200:
                return response.text
        else:
            response = requests.get(url=url, headers=head)
            if response.status_code == 200:
                return response.text
        return None

    """
        从http://www.goubanjia.com/获取代理IP
    """

    def getIpListWeb(self):
        print("正在获取WebIpProxy")
        head = self.mkHead()
        response = requests.get(url=self.__proxyUrl, headers=head)
        if response.status_code != 200:
            print("获取WebIpProxy失败")
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        trList = soup.select("tbody > tr")
        ipList = []
        for tr in trList:
            ips = tr.contents[1].contents
            tempIp = ''
            for ip in ips:
                if type(ip) == bs4.element.NavigableString:
                    tempIp = tempIp + ip.string.replace(' ', '')
                    continue
                style = ip.attrs.get('style')
                if style is not None:
                    style = style.replace(' ', '')
                if (style is None or 'display:none' not in style) and len(ip.contents) != 0:
                    tempIp = tempIp + ip.contents[0].string.replace(' ', '')
            http = tr.contents[5].next.next
            ipList.append({http: http + "://" + tempIp})
        return ipList


