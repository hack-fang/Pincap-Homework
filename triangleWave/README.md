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

python 实现较为简单