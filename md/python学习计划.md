# python学习计划

## 目标

- 掌握爬虫
- 掌握web框架
- 掌握数据分析

## 行动

- 搭建数据库
- 爬取雪球数据
- 编写前端页面
- 完成web
- 数据编辑分析

## 疑问

- mysql 的 information_schema是什么, collactions是什么


## 记忆点

- scrapy
  - 安装，依赖openSSL
  - 调度器，url管理器，下载器，解析器，记忆化
  - 爬虫实践方向：1、获取html进行分析提取。2、分析api进行调用提取
  - HttpResponse
- win命令 tree -A 
- xpath  
  - 基础语法
  - //a[contains(text(),'aaa')]
  - css提取
- 准备git环境
  - pycharm 使用account进行git的认证 
  - ssh的重绑定，旧的似乎过期了
- python 文件操作
  - os.listdir() # 文件目录
  - os.getcwd() # get current working directory
- pycharm中文指南.pdf 下载
- python，动态语言的优缺点
  - 优点，快速原型、灵活
  - 缺点，维护重构、可读性差
- pip 指定版本，添加参数

----------------------------------
2020.10.30

- xpath finder（chrome插件）
- python
  - yield
    - 返回一个可迭代序列
    - 序列的值为yield表达式，依次执行的结果
    - 错误：x = yield i*i，该语句不能用于赋值, 此处x为None
    - yield生成的序列是懒生成的，每次执行iter.next()时运行一次生成程序
    - yield的运行原理：生成完本次结果后中断，下次生成时从断点处继续执行直到再次中断

  ```python
  def generate_square(n):
    i = 0
    while i < n:
        yield i * i
        i += 1
  result = generate_square(10)
  print(list(result))
  ```

  - 迭代器iter
    - 迭代器初始指向序列头，是虚拟头
    - 第一次iter.next()为第一个元素值
    - 当iter.next() == Null 时，序列遍历结束

- mysql
  - 字符编码 & 排序规则
    - 库有默认字符编码，查看命令:SELECT * FROM information_schema.SCHEMATA
    - 应该使用utf8mb4编码，它是utf8的升级版，扩充了特殊字符的支持，最常见应用就是表情
    - 查看表细节：show create table 表名称;
    - 排序规则应该与字符编码对应，utf8mb4编码应该使用utf8mb4系列的排序规则
  - 什么是Innodb
  - 事务
    - 原子性
    - 一致性
    - 隔离性
    - 持久性


## scrapy

- 是什么
  python爬虫明星框架。功能：异步的数据下载，高性能数据解析，高性能的持久化存储，分布式

- 环境搭建
  - pip install scrapy
  测试:控制台输入scrapy无报错
  - 创建工程：scrapy startproject xxxPro
  - cd xxxPro
  - 在子文件夹spiders中创建一个爬虫文件
    - scrapy genspider spiderName www.xxx.com
  - 执行工程
    - scrapy crawl spiderName
  - pycharm使用scrapy
    - scrapy crawl spiderName本质是通过cmdline.py脚本启动的，
    - pycharm可以通过编辑配置启动环境进入debug
      - Script path: cmdline.py(脚本文件地址)
      - Parameters: crawl spiderName(爬虫名字)

- hello_world
  - 网站爬取 & 解析
    ```
    test
    ```
  - 关键配置
    - userAgent = ''
    - ROBOTSTXT = False
    - LOG_LEVEL = 'ERROR'

- 持久化
  - 基于终端指令
    - 要求：只能将parse方法的返回值进行存储
    - 注意：只支持这些格式：'json','jsonlines','jl','csv','xml','pickle'
    - 指令：scrapy crawl spiderName -o filePath
      - eg:scrapy crawl qiubai -o ./qiubai.csv
    - 好处：简洁高效
    - 缺点：局限性比较强

  - 基于管道
    - 编码流程
      - 数据解析
      - 在item类中定义相关属性
      - 将解析的数据封装存储到item类型的对象中
      - 将item类型的对象提交给管道yield
      - 在管道类中对受到的item对象中存储的数据进行持久化操作
      - 在配置文件中开启通道
    - 管道值越小，优先级越高
    - 爬虫通过yield item将数据传给第一个管道，第一个管道处理结束后的返回值如return item，会递交给下一个管道作为其参数继续执行

- 细节
  - 在spider.parse方法中，可以yield Item/Request，但程序对这两者的处理方式不同
    - 参考scrapy.core.Scraper._process_spidermv_out方法
    - yield Item , 会将item数据交给管道处理
    - yield Request,将会交给调度器处理进行新页面的爬取

- 中间件
  - 下载中间件
  - 爬虫中间件



## 选择器selector

- css selector

## xpath
  - 使用路径表达式对XML文档进行导航
  - XML文档是一棵树
  - 树上的节点分为7种，统一称为selector
    - 文档节点（根节点） ```<bookstore>```
    - 元素  ``` <author>J K. Rowling</author> ```
    - 属性 ```lang="en"```
    - 文本 ```J K. Rowling```
    - 命名空间
    - 处理指令
    - 注释
  - 语法
    - 选取节点
      |表达式|描述|
      |:---|:---|
      |nodename|选取此节点的所有子节点。|
      |/|从根节点选取（取子节点）。|
      |//|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置（取子孙节点）。|
      |.|	选取当前节点。|
      |..|选取当前节点的父节点。|
      |@| 选取属性。|
    - 谓语
      - 谓语用来查找某个特定的节点或者包含某个指定的值的节点。
      - 在 [ ] 中
      - 第一个 [1]
      - 最后一个[last()]
    - 函数
      - XPath、XQury、XSLT等自支持的函数，
        参考https://www.runoob.com/xpath/xpath-functions.html




![image.png](http://tva1.sinaimg.cn/large/006fuBezgy1gwetrgu56cj30wm0dkn4e.jpg)




## todo

- [ ] maggodb & innoDB & mysql

- 英语
  - 目的：快速获取知识
  - 学习方法：
    - 在工作中，需要的时候去查
      - 知识要通过 语言关 & 知识体系 ，两层转化
      - 效率低，理解差
    - 在平时，进行阅读
      - 不感兴趣，没有驱动，难以坚持
      - 怎么样进入心流？
  - 一些关键点
    - 阅读需要总结中文阅读技巧
      - 怎么样快速定位关键内容，通用技巧
      - 怎么样快速判定内容的有效性
        - 知识体系


- 爬虫
  - 招聘爬虫
  - 股票爬虫
  - 王者荣耀皮肤图片  
  - 音乐下载
    - 酷我
    - 网易
    - 百度
    - qq
    - 虾米
  - 淘宝
  - 电影
  - 小说
  - 房价、租金
  - ip池
  - ua池
  - 动态加载
  - 正则
  - 爬虫项目

- Django


