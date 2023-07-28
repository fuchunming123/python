import RequestsUtil

if __name__ == "__main__":
    header = {'Host': 'www.yikeliangzi.com',
    'Connection': 'keep-alive',
    'Content-Length': '147',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxODQ4MzIyODg1NyIsInBhdGhzIjpbXSwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sIm5hbWUiOiLnrKbnuq_mmI4iLCJpZCI6NDU2MDAsImV4cCI6MTcxMzE0NjY1NSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIl0sImp0aSI6ImE4NDljYzE2LWE0MWYtNDJjYy05M2UzLWNkMmU1MDZmMDFiZiIsIm1vZHVsZXMiOltdLCJjbGllbnRfaWQiOiJtb2JpbGUiLCJmaWx0ZXJQYXJraW5nSWRzIjpbXX0.TwkelmJsFXwECGS1npJulEDJ4vS6g5bBtgM05P8RWc-Z0htTi3cNdgcrmtRkZnDDZfsKO5qWxyoii3porlLsLca-z7b22Lh0iTPM_uIqiDEjWxA0CJTlQaIUSbluXYnQjPFW9sLSGszGkSuLx3paRBQfxe0xDCl2KWe8l1f-QWCkpQqRN33ex1yi2NafPBbTQHMbWyc-Qq1rBeF_o5A28r8ysvloxi8BkAOYblItsxypDedh_fBFzrcbEjzsvE75k-Cf2kpRKvI9id87ild7i3kPWR05y8c27KdavRT-K4kiAVekOCCdxTBsc_nadeda3S-oRwzLH9CZ3B5KTHbAPQ',
    'referer': 'https://servicewechat.com/wxd18458568746c32d/17/page-frame.html',
    'xweb_xhr': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh'}



    re3 = RequestsUtil.requestGet("https://www.yikeliangzi.com/gateway/api/v1/me/vehicle/40006", header,
                         {})
    # RequestsUtil.request("PUT", "https://www.yikeliangzi.com/gateway/api/v1/me/vehicle/40006", header,
    #                      {"id":'40006',"parkingId":'54',"ownerId":'45600',"comments":"uum",
    #                       "planetNumber":"Y8C7-KLJA-NZRG-4FWX","memberId":'45600',"type":'315',
    #                       'expireTime':'2023-04-15',
    #                       "unit":"2@2@2"})
    print(re3.json())