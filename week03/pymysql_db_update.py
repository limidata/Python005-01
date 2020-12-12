#!/usr/bin/python3
import pymysql

db = pymysql.connect("localhost", "tech", "admin", "testdb")

try:
    with db.cursor() as cursor:
        sql = 'UPDATE book SET book_id = %s WHERE book_name = %s'
        value = (1003, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
