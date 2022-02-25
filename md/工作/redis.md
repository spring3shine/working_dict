# redis

- [ ] 能够说出redis的常⽤数据类型
- [ ] 能够使⽤redis的操作命令
- [ ] 能够使⽤jedis操作Redis.
- [ ] 能够理解Redis持久化

## 解决问题

- 缓存持久化
- 原子操作
- 分布式 跨机跨进程通信
- 提供便捷的数据结构
- 提供便捷的驱逐策略
- keys支持模糊查询







## 操作

- 原子操作的加减incr/decr，避免了分布式的并发问题
- 这个概念通常适用于每个 Redis 数据结构：您不会先创建键，然后再向其中添加内容，但您可以直接使用命令来添加新元素。作为副作用，如果密钥不存在，则将创建密钥。同样，在执行某些命令后会导致为空的键将自动从键空间中删除。
- 仅当我们知道用于存储它的确切key时，才能稍后检索此数据value



| key-vale  string         |              |                                                              |                                                              |      |
| ------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
|                          | set          | set server:name "fido"<br /><br /><br />SET resource:lock "Redis Demo 3" EX 5  <br />TTL resource:lock => 5 |                                                              |      |
| 永久存在                 | persist      | SET resource:lock "Redis Demo 3" EX 5<br/>PERSIST resource:lock<br/>TTL resource:lock => -1 |                                                              |      |
|                          | get          | get server:name  => "fido"                                   |                                                              |      |
|                          | exists       | exists server:name => 1<br />exisits server:blabla => 0      |                                                              |      |
| 删除键值对               | del          | set connections 10<br />del connections<br />incr connections => 1 |                                                              |      |
| 值+1                     | incr         | set connections 10<br />incr connections => 11               |                                                              |      |
| 值+k                     | incrby       | INCRBY connections 100 => 101                                |                                                              |      |
| 值-1                     | decr         |                                                              |                                                              |      |
| 值-k                     | decrby       |                                                              |                                                              |      |
| 到期时间（秒）           | expire 、TTL | SET resource:lock "Redis Demo"<br/>EXPIRE resource:lock 120 <br /><br /><br />TTL resource:lock => 113     <br />// after 113s     <br />TTL resource:lock => -2 | TTL  -2表示密钥不再存在<br />TTL  -1表示永不过期<br />set 时，ttl将被重置 |      |
|                          |              |                                                              |                                                              |      |
|                          |              |                                                              |                                                              |      |
| **列表list**（双向链表） |              |                                                              |                                                              |      |
|                          | RPUSH        | RPUSH friends "Alice"    <br /> RPUSH friends "Bob"          | 可变参数，可以同时添加多个元素                               |      |
|                          | LPUSH        | LPUSH friends "Sam"                                          | 可变参数，可以同时添加多个元素                               |      |
|                          | LRange       | LRANGE friends 0 -1 =>  ...遍历列表                          | id : 0,1,2.... -2,-1                                         |      |
|                          | LLEN         | 列表长度                                                     |                                                              |      |
|                          |              |                                                              |                                                              |      |
| **集合set**              |              |                                                              |                                                              |      |
|                          | Sadd         | SADD superpowers "flight" "x-ray vision" "reflexes"          | 可变参数，可以同时添加多个元素<br />返回k，元素不存在，执行了k次操作<br />返回0，元素已存在，不用执行 |      |
| remove                   | Srem         | SREM superpowers "reflexes" => 1     <br />SREM superpowers "making pizza" => 0 |                                                              |      |
| 测试值是否存在           | Sismember    | SISMEMBER superpowers "flight" => 1     <br />SISMEMBER superpowers "reflexes" => 0 |                                                              |      |
| 返回集合遍历             | Smembers     | SMEMBERS superpowers => 1) "flight", 2) "x-ray vision"       |                                                              |      |
| 集合加法set + set        | Sunion       |                                                              |                                                              |      |
| 随机返回一个元素         | Spop         | SPOP letters 2 => 1) "c" 2) "a"                              | 可以pop k个元素                                              |      |
| 同pop,但不弹栈           | Srandmembers | Srandmembers letters 2                                       | 参数同pop,但如果是负数，则返回值可重复                       |      |
|                          |              |                                                              |                                                              |      |
|                          |              |                                                              |                                                              |      |
| **Sorted Sets** （跳表） |              |                                                              | dict + 一个skiplist<br />dict : 分数和值的映射<br />skiplist：建立分数的排序<br />节点层级是通过randomLevel的，概率学 |      |
|                          | Zadd         | ZADD hackers 1940 "Alan Kay"                                 |                                                              |      |
|                          | Zrange       | ZRANGE hackers 2 4                                           |                                                              |      |
|                          |              |                                                              |                                                              |      |
| **Hashes**               |              |                                                              | Hashes 不允许单个字段过期                                    |      |
|                          | Hset         | HSET user:1000 name "John Smith"                             |                                                              |      |
|                          | HgetAll      | HGETALL user:1000                                            |                                                              |      |
|                          | Hget         | HGET user:1001 name                                          |                                                              |      |
|                          |              |                                                              |                                                              |      |
|                          |              |                                                              |                                                              |      |
|                          |              |                                                              |                                                              |      |
|                          |              |                                                              |                                                              |      |

---

## 多数据库性

redis默认是16个数据库, 编号是从0~15. 【默认是0号库】 

- select index:切换库 
- move key index: 把key移动到⼏号库(index是库的编号) 
- flushdb:清空当前数据库 
- flushall:清空当前实例下所有的数据库

## 发布订阅

1. Redis 发布订阅(pub/sub)是进程间⼀种消息通信模式, ⼯作⾥⾯⼀般使⽤MQ

## 事务

- [MULTI](https://redis.io/commands/multi)、[EXEC](https://redis.io/commands/exec)、[DISCARD](https://redis.io/commands/discard)和[WATCH](https://redis.io/commands/watch) 是 Redis 中事务的基础
- redis事务保证隔离，官方文档上说是限制了客户端行为，看起来粒度非常粗啊
- exec执行前，客户端断连，则不执行
- exec执行事务流中，如果redis崩溃或硬杀，则可能只执行了部分操作，redis重启时会检测出来，并强制退出，要求使用专门的工具修复
- redis事务不支持回滚
  - 错了就是编程的问题（语法、使用错误类型），这些错误不会上生产就应该会被检测出来
  - 它要服务高并发高速

## 集群

- redis全数据通过分片的方式保存在a,b,c机器上
- 为了保护数据不丢失，B存在其从节点B1,B2,B3...
- 数据更新流程（异步复制）
  - 客户端向主节点 B 发送一条写命令。
  - 主节点 B 执行写命令，并向客户端返回命令回复。
  - 主节点 B 将刚刚执行的写命令复制给它的从节点 B1 、 B2 和 B3 。
- 如果B还没有将写命令复制给从节点就挂掉的话，那么这条写命令就会丢失了，即**不保证数据的强一致性**
- 如果B主节点挂了，那么将在从节点中进行选举
  - 怎么判断节点挂了
    - 对于大多数一方来说， 如果一个主节点未能在节点超时时间所设定的时限内重新联系上集群， 那么集群会将这个主节点视为下线， 并使用从节点来代替这个主节点继续工作。
    - 对于少数一方， 如果一个主节点未能在节点超时时间所设定的时限内重新联系上集群， 那么它将停止处理写命令， 并向客户端报告错误。
  - 怎样选举：哨兵机制
    - 每个哨兵监控主节点状态
    - 主节点下线后，各哨兵检测到情况，并进行交流
    - 如果多数哨兵认同，那么就指定一个哨兵执行故障转移，选择主节点

## Zset 跳表

我的感想：

- 随机性算法真是天才，做工程9999满足是可以的
- 有些人反对随机跳表退化到O(n)，但redis缓存本身是快速抛弃的数据，就算偶尔构建出极端退化跳表，在定时刷新之类的影响下也不会产生特别恶劣的情况
- 跳表具有高于红黑树的并发性（红黑树要对根节点加锁，但跳表锁掉的节点更少）
- 跳表对序列数据请求支持更好
- 红黑树在维护颜色的节点时，要花费更多的空间，更麻烦的操作
- 但红黑树保证最坏情况，由此mysql使用的mtree可以沿用此思想，使得在大数据表现下保证下限，对数据库系统的稳定性很重要



## 应用场景

- 缓存（数据查询、短连接、新闻内容、商品内容等等） 
- 任务队列。（秒杀、抢购、12306等等） 
- 数据过期处理（可以精确到毫秒, 短信验证码)  
- 分布式集群架构中的session分离 session 服务器⾥⾯ 
- 聊天室的在线好友列表 
- 应⽤排⾏榜 
- ⽹站访问统计



**String**

1. 缓存功能：字符串最经典的使⽤场景，redis作为缓存层，Mysql作为储存层，绝⼤部分请求数据都是在redis 中操作，由于redis具有⽀撑⾼并发特性，所以缓存通常能起到加速读写和降低 后端压⼒的作⽤。 
2. 计数器功能：⽐如视频播放次数，点赞次数。 
3. ID递增

**Hash**

- ⽤⼀个对象来存储⽤户信息，商品信息，订单信息等等。

**List**

- 好友列表，
- 粉丝列表，
- 消息队列，
- 最新消息排⾏等。

**Set**

- 投票记录

- 共同好友
- 共同兴趣
- 分类标签

**Sort-Set**

- 排⾏榜



## 问题

- redis 单线程：
  - redis的瓶颈不在cpu而在网络和内存
  - 数据分片可以减缓问题
  - 数据分片除了可以用多机实现外，单机多redis进程也可以做

