# -*- coding: UTF-8 -*-
import re
import sys
import traceback
from bs4 import BeautifulSoup
import pymysql

# 获取数据源
from IpProxyUtils import *

class CrawlerBk:


    #IP池管理器
    __ipProxyUtils = None
    #数据库链接
    __myConnect = None
    # 使用cursor()方法获取操作游标
    __myCursor = None
    #最大分页
    __pageSize = 10

    def __init__(self):
        self.__ipProxyUtils = IpProxyUtils(None, False)
        self.__myConnect = self.connectMysql()
        self.__myCursor = self.__myConnect.cursor()


    def connectMysql(self):
        # 打开数据库连接
        try:
            db = pymysql.connect("localhost", "root", "root", "testDb", charset='utf8')
        except BaseException:
            traceback.print_exc()
            print("获取数据链接失败")
            db.close()
        return db




    # 根据首页获取地区URL
    def openHtml(self, url):

        html = self.__ipProxyUtils.readWeb(url)
        soup = BeautifulSoup(html, "html.parser")
        # 根据所有地区地址
        dqList = soup.select("div[data-role='ershoufang'] > div > a[class='CLICKDATA']")
        for dq in dqList:
            # 地区，小区，名称，单价，总价，楼层，建设年度，户型，面积，朝向，url
            data = {}
            # 地区
            dq1 = dq.string
            url1 = dq.get('href')
            #myThread(url + url1, dq1).start()
            for i in range (1, 11):
                list = self.openFy(url + url1.split('/')[2] + '/pg%d'%i + 'p1p2p3' , dq1)
                self.insertData(list)


    # 获取房源信息
    def openFy(self, url, dq):
        fyListData = []
        html = self.__ipProxyUtils.readWeb(url)
        soup = BeautifulSoup(html, "html.parser")
        fyListSoup = soup.select(".sellListContent > .clear > div[class='info clear']")
        for fyInfo in fyListSoup:
            fyData = []
            fyData.append(fyInfo.select(".title > a")[0].string.strip().replace(' ', ''))
            fyData.append(fyInfo.select(".title > a")[0].get("href"))
            houseInfo = fyInfo.select(".address > .houseInfo")[0].next_element.next_element.next
            fyData.append(houseInfo.strip().replace('\n', '').replace(' ',''))
            jgInfo = fyInfo.select(".address > .priceInfo")[0]
            # 单价
            fyData.append(float(re.findall(r"\d+\.?\d*",jgInfo.select(".totalPrice > span")[0].string)[0]))
            # 总价
            fyData.append(float(re.findall(r"\d+\.?\d*", jgInfo.select(".unitPrice > span")[0].string.strip().replace(' ', ''))[0]))
            fyData.append(dq)
            fyListData.append(tuple(fyData))
        return fyListData


    def insertData(self, fyListData):
        try:
            # 使用execute方法执行SQL语句
            sql = "insert fyxx(mc,url,info,zj,dj,dq) values('%s','%s','%s','%.5f','%.5f','%s')"
            #cursor.executemany(sql % fyListData)
            for fy in fyListData:
                self.__myCursor.execute(sql % fy)
            self.__myConnect.commit()
            print("数据插入成功")
        except:
            print("插入数据失败")
            traceback.print_exc()

    def init(self, url):
        self.openHtml(url)


if __name__ == "__main__":
    crawlerBk = CrawlerBk()
    crawlerBk.init("https://cd.ke.com/ershoufang/")
    sys.exit(0)
