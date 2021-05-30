#接口测试框架
```mermaid
gragh TD
A[用例层]-->B[接口层]
B-->C[实用方法层]
```
## 框架说明
```
apis/  接口封装
data/  数据文件目录
reports/  测试报告和日志文件
testcases/  用例目录
  conftest.py   用例公用测试准备/清理方法
utils/    实用方法库
conftest.py   全局钩子方法
pytest.ini    测试配置
requirement.txt   项目依赖
```
## 解决方案
- 配置文件：pytest.ini
- 用例标记： pytest  mark
- 数据分离： [pytest-varaibles[yaml]](https://pypi.org/project/pytest-variables/)
- 用例等级：[allure-pytest](https://docs.qameta.io/allure/#_pytest)  @servity/ [pytest-level](https://pypi.org/project/pytest-level/)
- 环境切换：[pytest-base-url](https://pypi.org/project/pytest-base-url/)
- 失败自动重跑：[pytest-rerunfailures](https://pypi.org/project/pytest-rerunfailures/)
- 用例并发：[pytest-xdist](https://pypi.org/project/pytest-xdist/)
- 测试报告：[allure-pytest](https://docs.qameta.io/allure/#_pytest) / [pytest-html](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
- 复合断言：[pytest-check](https://pypi.org/project/pytest-check/)

## 依赖
参考 requirement.txt
pip install pytest requests pytest-level pytest-base-url pytest-rerunfailures pytest-xdist pytest-html pytest-check pytest-variables[yaml]

pip freeze > requrement.txt   #执行完pip安装后，控制台输入此命令，冻结当前版本，将依赖包输出到requrement.txt文件
## 使用方法
1. cd到项目目录,安装依赖
```
pip install -r requirements.txt
```