import requests
import logging

#数据抽离
# data = {
#     'uesr':{'loginName':'17711090001',
#         'passWord':'62c8ad0a15d9d1ca38d5dee762a16e01',
#         'companyId':'011336229198234378242'
#         }
# }
def test_login_01(variables):
    url = 'http://10.11.0.95:8891/ngbase/sys/user/login'    #使用base_url报错了，后面在研究
    user = variables['login_user']
    data = {"loginName":user['loginName'],"companyId":user['companyId'],"loginModel":"1","passWord":user['passWord']}
    header = {"Content-Type":"application/json",
              "IDENTIFICATION":"c*V@cc7!8fiTM~0G^d>>FVx6K]2cpV=@"}
    res = requests.post(url,json=data,headers=header)
    logging.info(res.text)
    token = res.json()['data']['token']
    logging.info(token)
