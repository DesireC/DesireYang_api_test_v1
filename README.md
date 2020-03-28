# DesireYang_api_test_v1
接口自动化项目
## *Author：Desire*

### PO模式分层设计

- **common**：存放通用封装模块
  - ***DB_Handle.py**：操作数据库模块*
  - ***Excel_Handle.py**：操作Excel表格模块*
  - ***Logging_Handle.py**：操作日志模块*
  - ***Path.py**：操作项目路径模块*
  - ***Request_Handle.py**：操作接口请求模块*
  - ***Yaml_Handle.py**：操作yaml配置文件模块*

- **conf**：存放配置文件

- **data**：存放数据

- **logs**：存放日志文件

- **reports**：存放生成的测试报告

- **testcase**：存放测试用例类

- **run_test.py**：整个项目的入口
