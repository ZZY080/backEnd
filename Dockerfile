FROM python:3.10-slim
COPY ./ /app

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& dpkg-reconfigure -f noninteractive tzdata \
# 配置pip国内源
&& pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
# 安装依赖
&& pip --no-cache-dir install --upgrade pip \
&& pip --no-cache-dir install wheel \
&& cd /app \
&& pip --no-cache-dir install -r ./requirements.txt \
# 清理缓存
&& rm -rf ~/.cache/pip

EXPOSE 13094
ARG CP_SERVER_HOST
ARG CP_SERVER_PORT
ARG CP_MYSQL_HOST
ARG CP_MYSQL_PORT
ARG CP_MYSQL_USERNAME
ARG CP_MYSQL_PASSWORD
ARG CP_MYSQL_DATABASE

WORKDIR /app/src
CMD ["python", "./main.py", "--debug"]
