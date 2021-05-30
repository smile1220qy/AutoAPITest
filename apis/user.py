"""登录用户相关接口封装"""
import requests
import logging
from apis.baseApi import BaseApi

class User(BaseApi):
    def __init__(self,loginName, companyId, passWord):
        super.__init__(loginName, companyId, passWord)

    def add_user(self,**user):
        url = 'http://10.11.0.95:8891/ngbase/employee/update'  # 使用base_url报错了，后面在研究
        data = {"employeeName": user.get('employeeName',''),
                "idCard": user.get('idCard',''),
                "bankCard": user.get('bankCard',''),
                "phone": user.get('phone',''),
                "companyId": user.get('phone',''),
                "status": "00",
                "bankId": "866",
                "verifyFourFactor": 1
                }
        # res = requests.post(url, json=data, headers=header)
        res = self.post(url, json=data)
        logging.info(f'新增员工接口返回{res.json()}')
        return res.json()

    def get_uesr_list(self):
        url = 'http://10.11.0.95:8891/ngbase/employee/list'
        data = {"column": "createTime",
                "order": "desc",
                "field": "id,,employeeNo,employeeName,companyName,idCard,bankCard,phone,status,fourFactorStatus,action",
                "currentPage": "1",
                "pageSize": "10"}
        res = self.post(url, json=data)
        logging.debug(f'查询员工列表接口返回{res.text}')
        return res.json()

    def get_user_detail(self):
        url = 'http://10.11.0.95:8891/ngbase/company/list/notPage'
        res = self.post(url, json={})
        logging.debug(f'查询员工详情接口返回{res.text}')
        return res.json()

    def getUserId_byPhone(self,phone):
        url = 'http://10.11.0.95:8891/ngbase/employee/list'
        data = {"column":"createTime",
                "order":"desc",
                "field":"id,,employeeNo,employeeName,companyName,idCard,bankCard,phone,status,fourFactorStatus,action",
                "currentPage":"1",
                "pageSize":"10",
                "phone":phone}
        res = self.post(url,json=data)
        logging.debug(f'根据手机号码查询员工id接口返回{res.text}')
        employeeId = res.json()['data']['list']['employeeId']
        logging.debug(f'查询到的employeeId{employeeId}')
        return employeeId

    def deleteUser_byId(self,employeeId):
        url = 'http://10.11.0.95:8891/ngbase/employee/delete'
        data = {"idList":[employeeId]}
        res = self.post(url,json=data)
        logging.info(f'删除员工{employeeId}')
        return res

