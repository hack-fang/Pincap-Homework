from PIL import Image
import pymysql
import time

# 连接数据库
db = pymysql.connect(host='localhost', port=4000, user="root", db="test")
cursor = db.cursor()
# 数据
val = [("alex", "china")]


# 写入大量数据到指定的表中
def write_data(cursor, table, data):
    sql = f"INSERT INTO {table}(name,address) VALUES (%s,%s)"
    try:
        cursor.executemany(sql, data)
        db.commit()
    except Exception as f:
        db.rollback()
        print(f"write to {table} not ok !")
        print(f)


def read_img(file):
    # 载入图像，并获得其二维数组
    img = Image.open(file)
    img_array = img.load()
    print("load ok!")
    # 存放所有像素坐标
    array = []
    for i in range(0, 100):
        res1 = []
        for j in range(0, 100):
            # 1-255,1表示黑，写入数据量最小
            res1.append(img_array[i, j] * 2000 / 256)
        array.append(res1)
    print("convert ok!")
    # 遍历写入
    for i in range(0, 100):
        # 遍历列数据，并统计写入总时间，不满足一分钟则等待至一分钟
        start = time.time()
        for j in range(0, 100):
            table = f"test{100 - j}"
            # 打印列数据
            data = int(array[i][j]) * val
            write_data(cursor, table, data)
        end = time.time()
        print(f"finished {i} col in {end - start} s")
        # 等待至时间达到60s
        time.sleep(60 - (end - start))


if __name__ == "__main__":
    read_img("sample.jpg")
