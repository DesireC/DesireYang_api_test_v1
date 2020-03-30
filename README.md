# DesireYang_api_test_v1
### ===>>接口自动化项目
## *Author：Desire*

### 环境：

- **python3.8**：项目环境
- **PyCharm**：项目工具
- **Typora**：Markdown编辑器
- **GitHub**：代码托管

### 项目中所用到的模块（pip install 库名）：

- **PyMySQL**：MySQL数据库所需库
- **PyYAML**：YAML配置文件所需库
- **pymongo**：MongoDB数据库所需库
- **pytest**：Pytest测试框架所需库
- **requests**：发送http请求所需库
- **suds-jurko**：发送webservice请求所需库
- **pytest-html** ：pytest生成HTML测试报告所需库
- **allure-pytest** ：pytest集成allure测试报告所需库

### PO模式分层设计

- **[common](common)**：存放通用封装模块
  - ***[DB_Handle.py](common/DB_Handle.py)**：操作数据库模块*
  - ***[Excel_Handle.py](common/Excel_Handle.py)**：操作Excel表格模块*
  - ***[Logging_Handle.py](common/Logging_Handle.py)**：操作日志模块*
  - ***[Path.py](common/Path.py)**：操作项目路径模块*
  - ***[Request_Handle.py](common/Request_Handle.py)**：操作接口请求模块*
  - ***[Yaml_Handle.py](common/Yaml_Handle.py)**：操作yaml配置文件模块*
- **[conf](conf)**：存放配置文件
- **[data](data)**：存放数据
- **[logs](logs)**：存放日志文件
- **[reports](reports)**：存放生成的测试报告
  - ***[allure](reports/allure)*：存放allure生成的测试报告**
  - ***[allure-plus](reports/allure-plus)*：存放allure升级版的测试报告（查看更加的方便，在PyCharm中可直接查看）**
- **[testcase](testcase)**：存放测试用例类
- **[pytest.ini](pytest.ini)**：pytest的配置文件(里面不要出现中文，否则有时候运行会报编码错误)
- **[run_test.py](run_test.py)**：整个项目的入口

