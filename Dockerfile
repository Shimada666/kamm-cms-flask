FROM ccr.ccs.tencentyun.com/corgi/python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple
CMD ["flask", "run", "-h", "0.0.0.0"]