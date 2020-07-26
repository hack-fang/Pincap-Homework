import sys


def gen(filename, num):
    with open(filename, "a+") as f:
        f.flush()
        for i in range(1, num + 1):
            table_name = f"test{i}"
            sql = f'''
DROP TABLE IF EXISTS `{table_name}`;

CREATE TABLE `{table_name}` (
`name` varchar(255) ,
`address` varchar(255)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

'''
            f.write(sql)


if __name__ == "__main__":
    filename = sys.argv[1]
    num = sys.argv[2]
    gen(filename, int(num))
