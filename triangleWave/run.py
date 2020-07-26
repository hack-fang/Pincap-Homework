import pymysql
import time

# 连接数据库
db = pymysql.connect(host='localhost', port=4000, user="root", db="test")


def triangleWrite(cursor, tables, data, times=100, interval=0.1):
    for table in tables:
        write(cursor, table, data, 500, 0.1)
        print(f"write {table} done.")
        time.sleep(1)


# 按照一定频率写入指定秒数
def write(cursor, table, data, times=100, interval=0.1):
    for i in range(times):
        write_data(cursor, table, data)
        time.sleep(interval)


# 写入大量数据到指定的表中
def write_data(cursor, table, data):
    sql = f"INSERT INTO {table}(name,address) VALUES (%s,%s)"
    try:
        cursor.executemany(sql, data)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"write to {table} not ok !")
        print(e)


if __name__ == "__main__":
    cursor = db.cursor()
    # 测试的写入数据
    val = [("alex", "china")] * 40
    # 组合序列
    seq1 = [f"test{i}" for i in range(1, 101)]
    seq2 = [f"test{i}" for i in range(2, 100)]
    seq2.reverse()
    seq1.extend(seq2)
    # 循环写入
    while True:
        triangleWrite(cursor, seq1, data=val)
