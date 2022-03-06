# Django



- [ ] python -m
- [ ] 

---

pip OSError :  Missing dependencies for SOCKS support.

- 通过取消设置环境变量http_proxy、https_proxy，可以解决
- http_proxy作用：程序可以根据配置的代理地址进行代理
- 推测
  - 我形成了循环代理？
- 我把http_proxy环境变量删了，看看会发生什么