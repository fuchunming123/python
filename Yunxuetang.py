import traceback
import urllib
import json

import pymysql
import requests

import RequestsUtil


class Yunxuetang:
    # 数据库链接
    myConnect = None
    # 使用cursor()方法获取操作游标
    myCursor = None

    def connectMysql(self):
        # 打开数据库连接
        try:
            self.myConnect = pymysql.connect(host="192.168.1.120", port=32784, user="root", password="myjcyf",
                                             database="test", charset='utf8')
            self.myCursor = self.myConnect.cursor()
        except BaseException:
            traceback.print_exc()

    def __init__(self):
        self.connectMysql()

        # 打开数据库连接
        try:
            self.myConnect = pymysql.connect(host="192.168.1.120", port=32784, user="root", password="myjcyf",
                                             database="test", charset='utf8')
            self.myCursor = self.myConnect.cursor()
        except BaseException:
            traceback.print_exc()
            print("获取数据链接失败")
            self.myConnect.close()

    def insertData(self, fyListData):
        try:
            # 使用execute方法执行SQL语句
            sql = "insert exam(ExamName,QuestionId,QuestionContent,QuestionType,Answer,IsAnswer,CombinedQuestions,ImportTime) values('%s','%s','%s','%s','%s','%s','%s',now())"
            for fy in fyListData:
                self.myCursor.execute(sql % fy)
            self.myConnect.commit()
            print("数据插入成功")
        except:
            print("插入数据失败")
            traceback.print_exc()

    def checkInfo(self, questionId):
        try:
            # 使用execute方法执行SQL语句
            sql = "select ExamName,IsAnswer,Answer from exam where QuestionId = '%s'"
            # cursor.executemany(sql % fyListData)
            self.myCursor.execute(sql % questionId)
            re = self.myCursor.fetchall()
            return re
        except:
            print("查询数据失败" + questionId)
            traceback.print_exc()

    def deleteExam(self, id):
        try:
            # 使用execute方法执行SQL语句
            sql = "delete from exam where QuestionId = '%s'"
            self.myCursor.execute(sql % tuple([id]))
            self.myConnect.commit()
            print("删除数据成功")
        except:
            print("删除数据失败")
            traceback.print_exc()
    #获取单个考试
    def getList(self):
        cookiesStr = 'XXTOWN_COOKIE_00018=ac4e4a0b-1de4-4a26-b9c5-8dad41b26690; ELEARNING_00999=yeg53wz3z0ccruecydjhiepi; ELEARNING_00008=7d0643fd-bde8-44fb-8acf-1e68a5e3510a; COOKIE_LANGAGES=zh; route=c99b015fa9d96077882278b00fcc67ec; isOpenDisasterMode=0; ELEARNING_00003=StudyMenuGroup; ELEARNING_00002=zhaoxiujun; ELEARNING_00017=7ddd16e3-a9ae-404f-9328-1bb39f50572e; loginType=Pwd; ELEARNING_00128=1; .ASPXAUTH=89E4821EDDCBFA872E6654ED37CCB8ED429AA5CA723B590D2CFC0430D2CC5A812E03D5CB62E9544E46866B7CA8D1037F7292BE2A47801F2A9D12A952002F19E91FA7C3D3311273215541965B5EC948281F2BF742AA6B38C6628DF1C4D249C0E07940940B4BC9F9D8A20E4E2F5030F265448EE14E1F8D68C233B8A4EE681D22CF0818C889175F0B60BFD0E125; ELEARNING_00006=D6257D6071CED8AF825F4DB283CEB84679179F1F807999830B278E60F4BC4B6F3837BBC748A93D5EF2E9668F844196F884A8927489FB9BE0168501190DE314D3A022F6949D351E01C917306FDBD92DCF15B29555DC8A1FC80FFA3B5E29C9E7772631B403BD6ACD0022A439139F6A09321CBD2E02028AFCCCAA8B2E8B9B93C1F130B55F73CC2300460CF93101B31FECEEC7E2F1F9A50897785D6DEF2F6024C3E53A3F3F3A84FAE8FD5DD6DABD31B32E5DB049DF6D18D51F34A396E773; ELEARNING_00018=98/+rucGM2N1Oq1KvNlU7dmV1YkPvF/uYlvjOc0uyzpciK0vZlZ++YCZGGHxOzDGYDhsYS9nsFORc8pko5/eb9pXqS6TRxGKMNl1ZgxH6hjdvOKV6zdvcRO9nMSAMMIjXwVABOPteDDucWuyXatinEyWNSROVeHGwVb+a/fkcXG7/fbeV9lV1G+iHpQ5vqmdE1TGofO+f0lZ/TkQB4kAJqFPF/xkWEyyqdK8CZVWwpY=; ELEARNING_00024=aliyun--cluster--AAAAAG_teaR8Q0AREijV23BSRgVJ482UTlJQYmglWLe_D96VjGDPvdz_79OVWhzY-qduruWjdy9ajopVL9A3cIhnxRjgU1uCHPCAIg4LcRVFpmkxxsu6tWpHr7rofl1O_gjXCuyb-IGgkUx-m3jwy_uHc1w'
        json1 = json.dumps({
            'UserExamID': "2dec3c5b-992c-4de1-8ff4-bf52385c415c",
            'arrangeId': "",
            'isAnonymous': "",
            'userExamMapId': "",
        })
        header = {
            'Authority': 'zhbr.yunxuetang.cn',
            'Method': 'POST',
            'Path': '/exam/Services/StyService.svc/getAnswerCard',
            'Scheme': 'https',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '104',
            'Content-Type': 'text/json',
            'Origin': 'https://zhbr.yunxuetang.cn',
            'Referer': 'https://zhbr.yunxuetang.cn//exam/Exams/Dialog/ViewAnswerCard.aspx?UserExamID=bf7b3247-f24e-4739-845f-2faa14692543',
            'Sec-Ch-Ua': '',
            'Cookie': cookiesStr,
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': 'Windows',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        url = 'https://zhbr.yunxuetang.cn/exam/Services/StyService.svc/getAnswerCard'
        re = requests.post(url=url, headers=header, data=json1)
        print(re)
        answerCard = json.loads(re.json())
        print(answerCard)
        examName = answerCard['examName']
        answerArray = []
        choiceItemsKey = {'Judge': 'JudgeItems', 'MultiChoice': 'ChoiceItems', 'SingleChoice': 'ChoiceItems',
                          'FillIn': 'FillInItems'}
        for answer in answerCard['combinedQuestions']:
            # 问题名称
            answerName = answer['QuestionContent']
            # 是否正确
            isFault = ""
            if choiceItemsKey[answer['QuestionType']] == 'FillInItems':
                isFault = "True"
            else:
                if answer['IsFault']:
                    isFault = "False"
                else:
                    isFault = "True"
            # 答案选项
            choiceItems = answer[choiceItemsKey[answer['QuestionType']]]
            answerStr = ''
            combinedQuestions = ''
            for choice in choiceItems:
                if choiceItemsKey[answer['QuestionType']] == 'FillInItems':
                    answerStr += choice['ItemAnswer'] + ";"
                elif choiceItemsKey[answer['QuestionType']] == 'JudgeItems':
                    if isFault == 'True' and choice['IsSelected']:
                        answerStr += choice['ItemContent'] + ";"
                    elif isFault == 'False' and not choice['IsSelected']:
                        answerStr += choice['ItemContent'] + ";"
                else:
                    if choice['IsSelected']:
                        answerStr += choice['ItemContent'] + ";"
                    combinedQuestions += choice['ItemContent'] + ";"

            if choiceItemsKey[answer['QuestionType']] == 'JudgeItems':
                isFault = "True"

            # 判断问题是否已经存在
            ire = self.checkInfo(answer['QuestionID'])
            # 数据库没有这个问题
            if len(ire) == 0:
                print("新题库" + str(answer['QuestionContent']))
            else:
                re1 = ire[0]
                # 数据库问题是错的
                if re1[1] == "False":
                    # 本次问题是对的
                    if isFault == 'True':
                        # 删除数据库的数据
                        self.deleteExam(answer['QuestionID'])
                        print("更新题库" + answer['QuestionID'])
                    else:
                        dbAnswerStr = str(re1[2])
                        # 合并两个错误的数据
                        if not dbAnswerStr.__contains__(answerStr):
                            answerStr = answerStr + "    " + re1[2]
                            self.deleteExam(answer['QuestionID'])
                            print("合并问题" + answerStr)
                        else:
                            print("问题已经存在切问题错误" + answer['QuestionID'])
                            continue
                else:
                    print("问题已经存在" + answer['QuestionID'])
                    continue
            an = [str(examName), str(answer['QuestionID']), str(answer['QuestionContent']), str(answer['QuestionType']),
                  str(answerStr), isFault, str(combinedQuestions)]
            answerArray.append(tuple(an))
        self.insertData(answerArray)

# 刷时常
def loadHeart(knowledgeId, masterId, packageId):
    cookiesStr = 'route=9567e8de46a634fb5565762484c6dc02; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174aebc2baa7a7-0a07331c50558c-333769-1327104-174aebc2babe82%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22174aebc2baa7a7-0a07331c50558c-333769-1327104-174aebc2babe82%22%7D; ELEARNING_00008=db34e3bf-bd1d-4dc8-ac98-afcd70bf4548; XXTOWN_COOKIE_00018=ac4e4a0b-1de4-4a26-b9c5-8dad41b26690; ELEARNING_00002=fuchunming; ELEARNING_00017=cefa08ef-7144-4a87-8889-1850a13c5f66; COOKIE_LANGAGES=zh; ELEARNING_00999=foyisilnjbrxtlsz2emyih05; route=99f02ffd59ded1d1cfe2b1142185c988; isOpenDisasterMode=0; ELEARNING_00003=StudyMenuGroup; .ASPXAUTH=BD7E2F58B6FD8420C6BBDEFACDAC01EB72928FBC17502F238925A9D4E2FE5E0782570C6C7A50F457AA18B9B94D806570AEA38305126A2338826C5BCB5883D604551EC136484CFA54DE7DA4BA294B8B101261E13F83504EC49B66B2ABE7C59433EECFD419FD10D83C93B6AFE10A37AABAB981BEB623D8404CF3766FFA48630E7E9C8160C7422051FF407EAF20; ELEARNING_00006=55164ED21504D5DE8A62FD80E844F3E0CE84C7844AB575359324E3724D1B7D1274F61983F24B6D3B74C6BCFCDBCA4BEA81916F5C029D0E7A656A5299D94EA98DCB6318752A28BA65BEB9A0FF32BE95B4E3DD21843F2B0828CA842FA78600C91E91DA0BDC1EBC3210227C388B2F31559A0C9590D1ED4C5EAEDDBFE05BBB8705D2B3F2BC553CBF032BA0E84BB58118536D0D0DBCDFF60CC8B946F6880FF375A13723C3C67C2F23B349359C3CAD36A9D7A4D754B817F5E60451A61A0FE6; ELEARNING_00018=98/+rucGM2N1Oq1KvNlU7SL7bOmTGDwDMTWMKQtWtto+vKjssPDANgek4xucgQ9qfjATzju7hHhRSGjgpZe/E43+nGhijEc41j97ZAIfuaL0zrxsAVo1ythTU5dvh0tnj03UrVZDupmnUXy9NE4dU8nCvre5LV+xJJotnr2H/QQcLq602glB5z2QogVXx8G3Y4KjrCPcfVKkI9A7MKvNJ7jFgGgpeKKi6/cy78KoGMM=; ELEARNING_00024=aliyun--cluster--AAAAACRDzbW-Ju0TAsn-8HEb3yJoEzopWQMlHIRX1MPGejGdhA_Fn67fv-hQ-4VW2zSGS_tawK_lyURokdI1GsmB7Q7W82-aZCtTuVJXNLi6cDXKyQnkZXPy9DfEHG_nGGcLhCBR7Wu50Q_ShvdQ6WKlQ3o; loginType=SMS'
    token = "aliyun--cluster--AAAAACRDzbW-Ju0TAsn-8HEb3yJoEzopWQMlHIRX1MPGejGdhA_Fn67fv-hQ-4VW2zSGS_tawK_lyURokdI1GsmB7Q7W82-aZCtTuVJXNLi6cDXKyQnkZXPy9DfEHG_nGGcLhCBR7Wu50Q_ShvdQ6WKlQ3o"
    header = {
        'Authority': 'zhbr.yunxuetang.cn',
        'Method': 'POST',
        'Path': '/exam/Services/StyService.svc/getAnswerCard',
        'Scheme': 'https',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        #'application/json, text/javascript, */*; q=0.01' ,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '104',
        'Content-Type': 'application/json',
        'Origin': 'https://zhbr.yunxuetang.cn',
        'Referer': 'https://zhbr.yunxuetang.cn',
        'Sec-Ch-Ua': '',
        'Cookie': cookiesStr,
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Source': '501',
        "Token": token,
        "dataType": "text"
    }
    for i in range(1):

        viewSchedule = 1 * 60
        url = "https://api-qidac1.yunxuetang.cn/v1//kng/knowledges/"+knowledgeId+"/heart";
        #for
        #RequestsUtil.requestPost(url, header, {});
        json1 = {
            "checkResult": True,
            "errorKey":"",
            "heartbeatTime":60,
            "knowledgeId":"",
            "knowledgeName":"",
            "source":"",
        }
        #RequestsUtil.requestGet(url, header, json1)
        json1 = json.dumps({
            "apiUrl": "study/submitpro  ,知识id："+knowledgeId+"  ,日志记录次数：1  ,定时器次数：30  ,标准学时：180  ,实际学时：0  ,视频进度位置：" + str(viewSchedule) + "",
            "context": json.dumps({
                "knowledgeId": knowledgeId,
                "masterId": masterId,
                "masterType": "Plan",
                "packageId": packageId,
                "pageSize": 1,
                "studySize": 1,
                "studyTime": 30,
                "offLine": False,
                "end": True,
                "deviceId": "",
                "studyChapterIds": "",
                "viewSchedule": viewSchedule
            }),
            "kngId": knowledgeId
        }, ensure_ascii=False).encode('utf-8')

        re = RequestsUtil.requestPost1("https://zhbr.yunxuetang.cn/kng/services/KngComService.svc/CreateSubmitLog", headers=header, payload=json1)
        re = getEncryptBody(json.dumps({
            "knowledgeId": knowledgeId,
            "masterId": masterId,
            "masterType": "Plan",
            "packageId":packageId,
            "pageSize":1,
            "studySize":1,
            "studyTime":30,
            "type":0,
            "offLine":False,
            "end":False,
            "care":True,
            "deviceId":"",
            "studyChapterIds":'',
            "viewSchedule":viewSchedule
        }))
        encryption = eval(re.json())['Data']
        print(encryption)
        json1 = {
            "care": True,
            "deviceId" : "",
            "encryption" : encryption,
            "end" : False,
            "knowledgeId" : knowledgeId,
            "masterId" : masterId,
            "masterType" : "Plan",
            "multiple" : 1,
            "offLine" : False,
            "packageId" : packageId,
            "pageSize" : 1,
            "realHour" : 30,
            "studyChapterIds" : "",
            "studySize" : 1,
            "studyTime" : 30,
            "type" : 0,
            "viewSchedule" : viewSchedule
        }
        RequestsUtil.requestPost("https://api-qidac1.yunxuetang.cn/v1/study/submitpro", header, json1)

def getEncryptBody(encryptRquest):
    encryptRquest = json.dumps(encryptRquest)
    arr = '{"body":' + encryptRquest + "}"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "371",
        "Content-Type": "text/json",
        #"Cookie": "route=9567e8de46a634fb5565762484c6dc02; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174aebc2baa7a7-0a07331c50558c-333769-1327104-174aebc2babe82%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22174aebc2baa7a7-0a07331c50558c-333769-1327104-174aebc2babe82%22%7D; ELEARNING_00008=db34e3bf-bd1d-4dc8-ac98-afcd70bf4548; XXTOWN_COOKIE_00018=ac4e4a0b-1de4-4a26-b9c5-8dad41b26690; ELEARNING_00002=fuchunming; ELEARNING_00017=cefa08ef-7144-4a87-8889-1850a13c5f66; COOKIE_LANGAGES=zh; ELEARNING_00999=foyisilnjbrxtlsz2emyih05; route=99f02ffd59ded1d1cfe2b1142185c988; isOpenDisasterMode=0; ELEARNING_00003=StudyMenuGroup; .ASPXAUTH=BD7E2F58B6FD8420C6BBDEFACDAC01EB72928FBC17502F238925A9D4E2FE5E0782570C6C7A50F457AA18B9B94D806570AEA38305126A2338826C5BCB5883D604551EC136484CFA54DE7DA4BA294B8B101261E13F83504EC49B66B2ABE7C59433EECFD419FD10D83C93B6AFE10A37AABAB981BEB623D8404CF3766FFA48630E7E9C8160C7422051FF407EAF20; ELEARNING_00006=55164ED21504D5DE8A62FD80E844F3E0CE84C7844AB575359324E3724D1B7D1274F61983F24B6D3B74C6BCFCDBCA4BEA81916F5C029D0E7A656A5299D94EA98DCB6318752A28BA65BEB9A0FF32BE95B4E3DD21843F2B0828CA842FA78600C91E91DA0BDC1EBC3210227C388B2F31559A0C9590D1ED4C5EAEDDBFE05BBB8705D2B3F2BC553CBF032BA0E84BB58118536D0D0DBCDFF60CC8B946F6880FF375A13723C3C67C2F23B349359C3CAD36A9D7A4D754B817F5E60451A61A0FE6; ELEARNING_00018=98/+rucGM2N1Oq1KvNlU7SL7bOmTGDwDMTWMKQtWtto+vKjssPDANgek4xucgQ9qfjATzju7hHhRSGjgpZe/E43+nGhijEc41j97ZAIfuaL0zrxsAVo1ythTU5dvh0tnj03UrVZDupmnUXy9NE4dU8nCvre5LV+xJJotnr2H/QQcLq602glB5z2QogVXx8G3Y4KjrCPcfVKkI9A7MKvNJ7jFgGgpeKKi6/cy78KoGMM=; ELEARNING_00024=aliyun--cluster--AAAAACRDzbW-Ju0TAsn-8HEb3yJoEzopWQMlHIRX1MPGejGdhA_Fn67fv-hQ-4VW2zSGS_tawK_lyURokdI1GsmB7Q7W82-aZCtTuVJXNLi6cDXKyQnkZXPy9DfEHG_nGGcLhCBR7Wu50Q_ShvdQ6WKlQ3o; loginType=SMS",
        "Host": "zhbr.yunxuetang.cn",
        "Origin": "http://zhbr.yunxuetang.cn",
        "Referer": "http://zhbr.yunxuetang.cn/kng/course/package/video/62230b2afb894a9c92d1d715b3e67ef6_08460ac7d7a44dbfbac286e6262041b2.html?MasterID=1e29e0e6-c1ec-4f3c-aa1b-2a910e6458b2&MasterType=Plan&uniqueid=1686099509438&uniqueid=638217251092897663",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    print(arr)
    response = requests.post("http://zhbr.yunxuetang.cn/kng/services/KngComService.svc/GetEncryptRequest", headers=headers, data=arr)
    return  response
        # commonHelper.logApiError("请求体md5加密失败", encryptRquest, response)

if __name__ == "__main__":
    # str = json.dumps({
    #     "knowledgeId": "08460ac7-d7a4-4dbf-bac2-86e6262041b2",
    #     "masterId": "1e29e0e6-c1ec-4f3c-aa1b-2a910e6458b2",
    #     "masterType": "Plan",
    #     "packageId":"62230b2a-fb89-4a9c-92d1-d715b3e67ef6",
    #     "pageSize":1,
    #     "studySize":1,
    #     "studyTime":30,
    #     "type":0,
    #     "offLine":False,
    #     "end":False,
    #     "care":True,
    #     "deviceId":'',
    #     "studyChapterIds":'',
    #     "viewSchedule": 569
    # })
    #getEncryptBody(str, None)
    torrent = Yunxuetang()
    torrent.getList()
    #return StudyRowClick('/package/video/62230b2afb894a9c92d1d715b3e67ef6_25bbecce042247aeb1f0b61bd26da13c.html?MasterID=1e29e0e6-c1ec-4f3c-aa1b-2a910e6458b2&MasterType=Plan','VideoKnowledge','','False', 'True','True','25bbecce-0422-47ae-b1f0-b61bd26da13c');
    #https://zhbr.yunxuetang.cn/exam/exampreview.htm?examID=5db3cbe0-13b6-4328-8db7-b0ea83ed75b9&examArrangeID=89b19844-8058-4d4d-8cb6-aadaa7e9d9a4&userExamMapID=6dbd537e-cb59-4368-9e2b-bee389238625
    #loadHeart("7d78020c-2d23-45e9-a089-930f1b59c137", "1e29e0e6-c1ec-4f3c-aa1b-2a910e6458b2", "62230b2a-fb89-4a9c-92d1-d715b3e67ef6")

