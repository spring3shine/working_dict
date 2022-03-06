# Spring



AOP 

- 切面编程
- 代理模式



IOC 

- 控制反转
- 工厂模式



## Spring 怎样处理循环引用

Spring 使用三级缓存来解决循环依赖的问题，三级缓存分别是：

- **singletonObjects：** 一级缓存，存储单例对象，Bean 已经实例化，初始化完成。

- **earlySingletonObjects：** 二级缓存，存储 singletonObject，这个 Bean 实例化了，还没有初始化。

- **singletonFactories：** 三级缓存，存储 singletonFactory。

  

![img](https://segmentfault.com/img/remote/1460000039091694)



## 反射





## 加载机制