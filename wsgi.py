import os
from dotenv import load_dotenv

# 用来存普通环境变量
common_dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(common_dotenv_path):
    load_dotenv(common_dotenv_path)

# 敏感环境变量, 如帐号密码等
secure_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(secure_dotenv_path):
    load_dotenv(secure_dotenv_path)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
