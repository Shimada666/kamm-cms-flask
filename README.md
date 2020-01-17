# kamm - 一个简单的flask cms框架
demo地址 [http://r1.cqupt.icu:5000](http://r1.cqupt.icu:5000)
## 安装使用
确保您安装了pipenv, 以及python解释器版本为3.6以上  


```shell script
# 创建python
pipenv --three
pipenv install

# 在根目录下创建.env文件 填入db_url=${你的URL}
# 如db_url='mysql+cymysql://root:root@localhost/kamm?charset=utf8mb4'
# 然后在mysql创建下数据库, 在app/config/secure.py下配置数据库连接, 或修改配置选用sqlite3

# 创建表
flask initdb
# 创建管理员账户: admin admin
flask admin
# 运行服务器
flask run
# 或
python wsgi.py
```
## 介绍
版本: v0.0.1 - 2020-01-18  
亮点: 使用了less简便开发同时保持对css的兼容, 良好的目录结构, 使html/css/js同处一个文件夹下, 易于开发

已完成功能：

- [x] 登录
- [x] 统一异常处理
- [x] 模型管理
- [x] 后端数据校验器
- [x] 用户添加注册
- [x] 用户模型修改
- [ ] 生产环境静态文件打包优化
- [x] 权限管理
- [ ] 日志
- [ ] 详细的文档
- [x] 移动端简单适配
- [ ] 图片/文件上传
- [ ] 软删除
- [ ] 分布式支持
- [ ] 其他更多功能...

## 目录结构
    .
    ├── app 程序主文件夹
    │   ├── blueprints                      蓝图
    │   │   ├── cms                         cms模块
    │   │   │   ├── error.py
    │   │   │   ├── __init__.py
    │   │   │   ├── system.py
    │   │   │   ├── auth.py
    │   │   │   └── user.py
    │   │   ├── demo                        demo模块
    │   │   │   ├── articles.py
    │   │   │   ├── friend_links.py
    │   │   │   └── __init__.py
    │   │   ├── home.py
    │   │   └── __init__.py
    │   ├── config                          配置文件
    │   │   ├── log.py                      日志的配置文件，暂无用，后期加入
    │   │   ├── secure.py                   敏感信息配置文件
    │   │   └── setting.py                  普通配置文件
    │   ├── exceptions                      统一异常类，处理ajax json请求的
    │   │   ├── base.py
    │   │   └── __init__.py
    │   ├── extensions.py                   flask扩展文件夹
    │   ├── fakes                           做假数据的脚本
    │   │   ├── articles.py
    │   │   └── friend_links.py
    │   ├── __init__.py                     程序工厂文件
    │   ├── libs 一些工具类
    │   │   ├── Helper.py
    │   │   ├── redprints.py
    │   │   ├── UrlManager.py
    │   │   └── utils.py
    │   ├── models                          存放数据模型的文件夹
    │   │   ├── articles.py
    │   │   ├── friend_links.py
    │   │   └── user.py
    │   ├── templates
    │   │   ├── favicon.ico                 网站图标
    │   │   ├── layout                      布局模版 css，js，html同一文件夹
    │   │   │   ├── index.css 
    │   │   │   ├── index.html
    │   │   │   └── index.js
    │   │   ├── page                        css，js，html同一文件夹
    │   │   │   └── index
    │   │   │       ├── index.css
    │   │   │       ├── index.html
    │   │   │       └── index.js
    │   │   └── static
    │   │       ├── css
    │   │       │   └──                     一些公共css，将来会优化合并
    │   │       ├── images
    │   │       │   └──                     静态图片
    │   │       ├── js
    │   │       │   └──                     一些公共js，将来会优化合并
    │   │       ├── json
    │   │       │   └──                     静态数据，将来会删除
    │   │       └── layui
    │   │           └──                     layui的静态文件
    │   └── validtors
    │       └── forms.py                    验证表单，之后加的都在这个文件夹下
    ├── Pipfile                             pipenv的包管理
    ├── Pipfile.lock                        同上
    ├── .env                                敏感信息的环境变量文件
    ├── .flaskenv                           普通环境变量文件
    ├── README.md                           readme
    └── wsgi.py                             程序启动文件
## 感谢
* [lin-cms-flask](https://github.com/TaleLin/lin-cms-flask) 我在这个cms框架中学到许多
* [greyli](https://github.com/greyli) greyli老师的一些思想
* [BrotherMa](https://github.com/BrotherMa/layuiCMS) 提供的前端页面  

感谢以上朋友的项目，让我参考借鉴了许多，才得以完成kamm这个cms框架。