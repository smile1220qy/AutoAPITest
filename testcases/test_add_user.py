from apis.user import User
from utils.data import load_yaml
import pytest

@pytest.mark.smok
def test_add_user_01(variables,user_api):
    user = variables['user']
    res = user_api.add_user(**user)

    assert res['code'] == '200'
    assert res['message'] == '处理成功!'
    #查询新增的员工
    employeeId = User.getUserId_byPhone(variables['user']['phone'])
    #删除新增的员工
    User.deleteUser_byId(employeeId)

users = load_yaml('test.yaml').get('users')
@pytest.mark.parametrize('item',users)
def test_add_user_02(variables,user_api):
    res = user_api.add_user(**users)
    assert res['code'] == '200'
    assert res['message'] == '处理成功!'
    #查询新增的员工
    employeeId = User.getUserId_byPhone(variables['user']['phone'])
    #删除新增的员工
    User.deleteUser_byId(employeeId)
