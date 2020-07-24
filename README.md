

![Go](https://img.shields.io/badge/Go-1.13.4%2B-blue)

 ##  为TiDB设计一个可观测的负载
 作业描述：编写一个程序，语言任意，程序连接 TiDB 运行一段时间后，能在 TiDB Dashboard 的 Keyvisualizer  面板上显示出明亮图案（以下图案选其一即可）
 - 一条正弦曲线
 - 任找一个灰阶图像
 
 ## 计划安排
 - day1 : 查看官方文档，并搭建集群试用DashBoard
 - day2 : 编写脚本测试数据库导入导出，并观测结果


## 搭建集群

1. 安装 `TiUP`并声明环境变量

```bash
curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
# zsh
source ~/.zshrc
```

2. 运行 

```bash
tiup playground
```

3. 清理环境

```bash
tiup clean -all
```

## 使用DashBoard

本地打开 http://127.0.0.1:2379/dashboard 无需输入密码即可

 
 ## 参考资料
 - [TiUP 安装集群](https://pingcap.com/docs-cn/stable/quick-start-with-tidb/#%E7%AC%AC%E4%B8%80%E7%A7%8D%E4%BD%BF%E7%94%A8-tiup-playground-%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2%E6%9C%AC%E5%9C%B0%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83)
 - [分布式系统的可观性](https://mp.weixin.qq.com/s/X3dodzwRhF4QX7fiL9yUTg)
 - [流量可视化](https://pingcap.com/docs-cn/stable/dashboard/dashboard-key-visualizer/)
 - [本地快速部署 TiDB 集群](https://pingcap.com/docs-cn/stable/tiup/tiup-playground/#playground-%E7%BB%84%E4%BB%B6%E4%BB%8B%E7%BB%8D)