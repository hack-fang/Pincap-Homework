# 灰阶图像生成

## 效果图

![1](https://github.com/hack-fang/Pincap-Homework/blob/master/grayScale/result.png)

![2](https://github.com/hack-fang/Pincap-Homework/blob/master/grayScale/result2.png)

## 思路
将灰度图转换成矩阵数据，每分钟写入一列数据，如第1分钟写入(0,0)、(0,2)、...(0,99)共100个像素点，即往表 test100、test99...test1中各写如对应量的数据，具体如下

1. 将灰度图处理成得到矩阵数据 matrix，并对每个位置的灰度值进行写入数据量的转换后存入新的矩阵array 中
2. 遍历array,并对每列写入时间进行限时1分钟，不足一分钟，则等待至一分钟结束，每列写入规则按照一个像素点对应一个表格方式进行
3. 循环写入，等待足够长的时间即可。

## 实现

### 环境要求
1. Python >= **3.6**
2. TiUP 安装
3. Mysql 管理软件(如 Navicat)

### 依赖安装
```bash
pip3 install pillow pymysql
```

### 运行

1. 运行 `tiup playground v4.0.2`
2. 连接tidb并在 `test` 数据库中导入 `test.sql`
3. 运行 `python3 run.py` 
4. 登录 Dashboard,进入`流量可视化选项`进行观测
5. 等待足够长的时间


### 不足之处

1. 由于写入的数据是分时写入而非并发写入，因此会出现数据段的偏移情况
2. 只针对了100*100图片进行输出，其他高分辨率图片需要增加更多的table和修改系统的运行参数。