#!/usr/bin/python3
import pymysql

db = pymysql.connect("localhost", "tech", "admin", "testdb")

try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'INSERT INTO book (book_id, type_id, book_name) VALUES (%s, %s, %s)'
        values = (
            (1004, 1, "百年孤独"),
            (1005, 2, "飘"),
        )
        cursor.executemany(sql, values)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
