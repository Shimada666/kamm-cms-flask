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
版本: v0.0.1 - 2019-12-08  
亮点: 使用了less, 同时也兼容css(只能存在其中一种), 改善(我认为的)了静态资源配置, 使html/css/js同处一个文件夹下, 易于开发

暂时是初版, 完成了最最最基础的功能

- [x] 登录
- [x] 统一异常处理
- [x] 模型管理
- [x] 后端数据校验器

TODO:
- [ ] 用户添加注册
- [x] 用户模型修改
- [ ] 生产环境静态文件打包优化
- [ ] 权限管理
- [ ] 日志
- [ ] 详细的文档
- [ ] 移动端简单适配
- [ ] 图片/文件上传
- [ ] 软删除
- [ ] 代码优化
- [ ] 分布式支持
- [ ] 其他更多功能...
