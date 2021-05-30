from apis.user import User
import pytest

@pytest.fixture(scope='session')
def user_api(variables):
    loginName = variables['login_user']['loginName']
    companyId = variables['login_user']['companyId']
    passWord = variables['login_user']['passWord']
    return User(loginName, companyId, passWord)