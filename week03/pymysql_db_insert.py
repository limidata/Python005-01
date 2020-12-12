#!/usr/bin/python3
import pymysql

db = pymysql.connect("localhost", "tech", "admin", "testdb")

try:
    with db.cursor() as cursor:
        sql = 'INSERT INTO book (book_id, type_id, book_name) VALUES (%s, %s, %s)'  # %s是占位符
        value = (1002, 1, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close
    print(cursor.rowcount)
