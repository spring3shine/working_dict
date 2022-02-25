# Flask框架

依赖

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
- [Jinja](https://palletsprojects.com/p/jinja/) 用于渲染页面的模板语言。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- [Click](https://palletsprojects.com/p/click/) 是一个命令行应用的框架。用于提供 `flask` 命令，并允许添加自定义 管理命令。

可选依赖

- [Blinker](https://pythonhosted.org/blinker/) 为 [信号](https://dormousehole.readthedocs.io/en/latest/signals.html) 提供支持。
- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 当运行 `flask` 命令时为 [通过 dotenv 设置环境变量](https://dormousehole.readthedocs.io/en/latest/cli.html#dotenv) 提供支持。
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供快速高效的重载。





## Q

1. 线程局部变量是什么？
   什么意思```Flask 内部使用线程局部的对象，这样你不必在请求内的函数间传递对象来保证线程安全。这个方法很方便，但为了实现依赖注入，或尝试重用含有与请求挂钩的值的代码之时，需要一个有效的请求环境（Request Context）。```
2. 开发流程是怎样的？
   安装，环境配置，程序编写，测试，部署，运维
3. 编码流程：
   1. 创建蓝图
   2. 将蓝图注册到app
   3. 为蓝图编写功能代码，并提交给模板 render_template('')
   4. 编写模板代码
4. 工厂类是什么？
   只生成一个商品，把这个商品给所有人用，而不是有人需要就生产(会冗余不易管理)
5. 



---

## keys记忆点：

1. 怎样启动一个flask_app

2. url_for() 是什么？有什么作用？有什么效果？，生成一个url路径

3. app.test_request_context()

4. @route('/home') 和@route('/home/')有什么区别？

5. 静态文件自动创建路由，只要在static文件夹下用户就能有权限访问

6. [`Markup`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Markup) 用于html转义，但我不知道作用领域，用到的时候再说吧

7. ```
   唯一的 URL / 重定向行为
   
   @app.route('/projects/')
   def projects():
       return 'The project page'
   
   @app.route('/about')
   def about():
       return 'The about page'
   
   1. \是转义符，所以用/
   2. 必须以/打头
   3. `projects` 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件 夹。访问一个没有斜杠结尾的 URL （ `/projects` ）时 Flask 会自动进行重 定向，帮您在尾部加上一个斜杠（ `/projects/` ）。
   4. about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这 个 URL 时添加了尾部斜杠（`` /about/ `` ）就会得到一个 404 “未找到” 错 误。这样可以保持 URL 唯一，并有助于搜索引擎重复索引同一页面。
   ```

8. 

