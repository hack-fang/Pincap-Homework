# 三角波生成

## 效果图

![1](https://github.com/hack-fang/Pincap-Homework/blob/master/triangleWave/result.png)

![2](https://github.com/hack-fang/Pincap-Homework/blob/master/triangleWave/result2.png)

## 思路
根据三角波的特点，从上升到下降，实则为一维信号，很容易得出其数学表达式。

1. table作为Y轴数据，每分钟写入一张表格
2. 上升写入方向为 test1 --> test20
3. 下降写入方向为 test19 --> test2
4. 循环2、3步

## 实现

### 环境要求
1. Python >= **3.6**
2. TiUP 安装
3. Mysql 管理软件(如 Navicat)

### 依赖安装
```bash
pip3 install pymysql
```

### 运行

1. 运行 `tiup playground v4.0.2`
2. 连接tidb并在 `test` 数据库中导入 `test.sql`
3. 运行 `python3 run.py` 
4. 登录 Dashboard,进入`流量可视化选项`进行观测
5. 等待足够长的时间