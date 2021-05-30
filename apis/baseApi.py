"""登录用户相关接口封装"""
import requests
import logging

class BaseApi(object):
    def __init__(self,loginName, companyId, passWord):
        self.loginName = loginName
        self.companyId = companyId
        self.passWord = passWord
        token = self.login()
        self.session = requests.session()
        self.session.headers = {"Authorization":token,
                                "Content-Type":"application/json",
                                "IDENTIFICATION":"c*V@cc7!8fiTM~0G^d>>FVx6K]2cpV=@"
                                }

    def get(self,url,**kwargs):
        #通过session自动带token令牌
        logging.info(f'发送get请求{url}{kwargs}')
        res = self.session.get(url,**kwargs)
        logging.info(f'响应数据{res.text}')
        return res

    def post(self,url,**kwargs):
        logging.info(f'发送post请求{url}{kwargs}')
        res = self.session.post(url,**kwargs)
        logging.info(f'响应数据{res.text}')
        return res

    def login(self):
        """登录并获取token"""
        url = 'http://10.11.0.95:8891/ngbase/sys/user/login'  # 使用base_url报错了，后面在研究
        data = {"loginName": self.loginName, "companyId": self.companyId, "loginModel": "1", "passWord": self.passWord}
        header = {"Content-Type": "application/json",
                  "IDENTIFICATION": "c*V@cc7!8fiTM~0G^d>>FVx6K]2cpV=@"}
        res = requests.post(url, json=data, headers=header)
        logging.info(res.text)
        token = res.json()['data']['token']
        logging.info(token)
        return token


