# CreativePay Backend

![Python Version](https://img.shields.io/badge/python-3.10.7-blue)
![License](https://img.shields.io/github/license/AkagiYui/CreativePayBackend)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AkagiYui/CreativePayBackend)
![lines](https://img.shields.io/tokei/lines/github/AkagiYui/CreativePayBackend)

The Backend of CreativePay

CreativePay 后端服务

## Quick Start 快速开始

## TODO 待办

- [ ] Auto Deploy 自动部署
- [x] Code Lint 代码检查

## Development 开发相关

- 操作系统：[Windows 10 19044.1586](https://www.microsoft.com/zh-cn/windows)
- 系统架构：amd64

### Technology Stack 使用技术

- Python: [3.10.7](https://www.python.org/) [下载地址](https://www.python.org/downloads/release/python-3107/)
- 依赖表生成工具: [pip-tools 6.8.0](https://github.com/jazzband/pip-tools/)
- 导入排序工具: [isort 5.10.1](https://pycqa.github.io/isort/)
- 代码格式化工具: [flake8 5.0.4](https://flake8.readthedocs.io/en/latest/) [mypy 0.982](https://mypy.readthedocs.io/en/latest/)
- 数据库: [MySQL](https://www.mysql.com/)

### Runtime Python Package 运行时Python包  

- [rich 12.5.1](https://github.com/Textualize/rich/blob/master/README.cn.md) 控制台美化
- [distro 1.7.0](https://github.com/python-distro/distro) 系统平台信息获取
- [psutil 5.9.1](https://github.com/giampaolo/psutil) 系统信息获取
- [ruamel.yaml 0.17.21](https://yaml.readthedocs.io/en/latest/) Yaml解析
- [peewee 3.15.1](https://github.com/coleifer/peewee/) ORM工具
- [fastapi 0.85.0](https://fastapi.tiangolo.com/zh/) HTTP/Websocket服务器
- [uvicorn 0.18.2](https://www.uvicorn.org/) ASGI web 服务器
- [requests 2.28.1](https://requests.readthedocs.io/en/latest/) HTTP客户端

### Code Lint 代码检查

```shell
python -m pip install -r ./requirements-dev.txt
python ./code_lint.py
```
