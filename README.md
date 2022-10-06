# CreativePay Backend

![Python Version](https://img.shields.io/badge/python-3.10.7-blue)
![License](https://img.shields.io/github/license/AkagiYui/CreativePayBackend)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AkagiYui/CreativePayBackend)
![lines](https://img.shields.io/tokei/lines/github/AkagiYui/CreativePayBackend)

The Backend of CreativePay

CreativePay 后端服务

## Quick Start 快速开始

### Docker 使用 Docker 部署

```shell
git clone https://github.com/AkagiYui/CreativePayBackend
cd ./CreativePayBackend
docker compose up -d --build
```

### Manual Deploy 手动部署

Make sure you have installed **Python 3.10.7**.

请确保你的机器有 **Python 3.10.7** 的环境，其他版本未经测试。

#### Install Dependencies 安装依赖

##### Windows 10 PowerShell

```ps
git clone https://github.com/AkagiYui/CreativePayBackend
cd ./CreativePayBackend
python -m venv venv
./venv/Scripts/activate
python -m pip install -r ./requirements.txt
cd ./src
```

##### Linux Debian 11

```shell
git clone https://github.com/AkagiYui/CreativePayBackend
cd ./CreativePayBackend
python3 -m venv venv
source ./venv/bin/activate
python -m pip install -r ./requirements.txt
cd ./src
```

#### Edit Configuration 修改配置文件

```ps
cp config.yaml.bak config.yaml
```

你也可以使用环境变量

#### Start Server 启动服务

```ps
python ./main.py --debug
```

## TODO 待办

- [ ] Auto Deploy 自动部署
- [x] Code Lint 代码检查
- [x] CORS Support 跨域支持
- [x] User Register 用户注册
- [x] User Login 用户登录

## Development 开发相关

- OS 操作系统：[Windows 10 19044.1586](https://www.microsoft.com/zh-cn/windows)
- Arch 系统架构：amd64

### Technology Stack 使用技术

- Python: [3.10.7](https://www.python.org/) [Download 下载地址](https://www.python.org/downloads/release/python-3107/)
- requirements.txt Creator 依赖表生成工具: [pip-tools 6.8.0](https://github.com/jazzband/pip-tools/)
- Import Sort 导入排序工具: [isort 5.10.1](https://pycqa.github.io/isort/)
- Code Lint 代码格式化工具: [flake8 5.0.4](https://flake8.readthedocs.io/en/latest/) [mypy 0.982](https://mypy.readthedocs.io/en/latest/)
- Database 数据库: [MySQL](https://www.mysql.com/)

### Runtime Python Package 运行时Python包  

- [rich 12.5.1](https://github.com/Textualize/rich/blob/master/README.cn.md) 控制台美化
- [distro 1.7.0](https://github.com/python-distro/distro) 系统平台信息获取
- [psutil 5.9.1](https://github.com/giampaolo/psutil) 系统信息获取
- [ruamel.yaml 0.17.21](https://yaml.readthedocs.io/en/latest/) Yaml解析
- [peewee 3.15.1](https://github.com/coleifer/peewee/) ORM工具
- [fastapi 0.85.0](https://fastapi.tiangolo.com/zh/) HTTP/Websocket服务器
- [uvicorn 0.18.2](https://www.uvicorn.org/) ASGI web 服务器
- [PyMySQL 1.0.2](https://pymysql.readthedocs.io/) MySQL客户端
- [python-jose 3.3.0](https://python-jose.readthedocs.io/en/latest/) JWT工具
- [cryptography 38.0.1](https://cryptography.io/en/latest/) 加密工具

### Code Lint 代码检查

```shell
python -m pip install -r ./requirements-dev.txt
python ./code_lint.py
```
