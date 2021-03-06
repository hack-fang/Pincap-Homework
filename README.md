![TiDB](https://img.shields.io/badge/tidb-4.0.2-green)
![Python](https://img.shields.io/badge/python-3.6%2C3.7-green)
![License](https://img.shields.io/badge/license-GPL-blue)
 ##  为TiDB设计一个可观测的负载
 作业描述：编写一个程序，语言任意，程序连接 TiDB 运行一段时间后，能在 TiDB Dashboard 的 Keyvisualizer  面板上显示出明亮图案（以下图案选其一即可）
 - 一条正弦曲线
 - 任找一个灰阶图像
 
 ## 计划安排
 
 - step1 : 查看官方文档，并搭建集群试用DashBoard
 - step2 : 编写脚本测试数据库导入导出，并观测结果
 - step3 : 测试三角形
 - step4 : 测试灰度图
 - step5 : 完善文档
 
 
## 搭建集群

1. 安装 `TiUP`并声明环境变量

```bash
curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
# zsh
source ~/.zshrc
```

2. 运行 

```bash
tiup playground v4.0.2
```

3. 清理环境

```bash
tiup clean -all
```

## 使用DashBoard

本地打开 http://127.0.0.1:2379/dashboard 无需输入密码即可

## 探索
1. 官方文档提供的`Region`概念较为重要
2. Dashboard 中`流量可视化`图表中的Y轴是各数据库组成的table，最上面的块为最晚创建的table
3. Dashboard 中`流量可视化`图表中的X轴的单位为`min`，注意写入量为 xx / min,要注意写入频率和数据量
4. python 写入速率 2000条/秒 比较恰当
5. 生成大量表使用 `python3 gen_sql $filename num`

## [三角波](https://github.com/hack-fang/Pincap-Homework/tree/master/triangleWave)
一维信号，每分钟写入一张表，按照顺序1-100写入，后从99-2写入，保持循环即可。

效果图

![1](https://github.com/hack-fang/Pincap-Homework/blob/master/triangleWave/result.png)

![2](https://github.com/hack-fang/Pincap-Homework/blob/master/triangleWave/result2.png)


## [灰阶图像](https://github.com/hack-fang/Pincap-Homework/tree/master/grayScale)

灰阶图像为二维信号，视作矩阵，每个像素点的值为1-255，1为黑色，255为白色，需要对不同的值进行分类，分成五档。

每档写入的数据量也不同，比如值为255时每分钟写入量为 2000条/秒，其余数值根据 x * 2000 / 255换算即可
考虑到 写入数据库速率比较快 且 dashboard 按照 分钟计算写入，因此可以采用分时写入错开即可。

效果图

![1](https://github.com/hack-fang/Pincap-Homework/blob/master/grayScale/result.png)

![2](https://github.com/hack-fang/Pincap-Homework/blob/master/grayScale/result2.png)

 
 
 ## 文件说明

- README.md    项目说明
- gen_sql.py   生成sql测试文件
- triangleWave/
   - README.md    三角波说明文件
   - result.png   结果文件
   - result2.png  结果文件2
   - run.py       运行程序
   - test.sql     测试sql文件
 - grayScale/
    - README.md    灰值图说明文件
    - result.png   结果文件
    - result2.png  结果文件2
    - run.py       运行程序
    - sample.jpg   样例图片
    - test.sql     测试sql文件
 
 ## 参考资料
 - [三角波](https://zh.wikipedia.org/zh-hans/%E4%B8%89%E8%A7%92%E6%B3%A2)
 - [灰度图像](https://zh.wikipedia.org/zh/%E7%81%B0%E5%BA%A6%E5%9B%BE%E5%83%8F)
 - [mysql 驱动](https://pymysql.readthedocs.io/en/latest/)
 - [python pillow doc](https://pillow.readthedocs.io/en/stable/)
 - [TiUP 安装集群](https://pingcap.com/docs-cn/stable/quick-start-with-tidb/#%E7%AC%AC%E4%B8%80%E7%A7%8D%E4%BD%BF%E7%94%A8-tiup-playground-%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2%E6%9C%AC%E5%9C%B0%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83)
 - [分布式系统的可观性](https://mp.weixin.qq.com/s/X3dodzwRhF4QX7fiL9yUTg)
 - [流量可视化](https://pingcap.com/docs-cn/stable/dashboard/dashboard-key-visualizer/)
 - [本地快速部署 TiDB 集群](https://pingcap.com/docs-cn/stable/tiup/tiup-playground/#playground-%E7%BB%84%E4%BB%B6%E4%BB%8B%E7%BB%8D)