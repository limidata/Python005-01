#!/usr/bin/python3
import pymysql

db = pymysql.connect("localhost", "tech", "admin", "testdb")

try:
    with db.cursor() as cursor:
        sql = '''SELECT book_name FROM book'''
        cursor.execute(sql)
        books = cursor.fetchall()  # fetchone()
        for book in books:
            print(book)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
