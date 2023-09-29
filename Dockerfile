# 使用官方 Python 镜像
FROM python:3.9

# 设置工作目录
WORKDIR /usr/src/app

# 安装依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录下的所有文件到容器的工作目录。
COPY . .

# 设置环境变量
ENV PORT=8000

# 对外暴露端口
EXPOSE 8000

# 启动 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
