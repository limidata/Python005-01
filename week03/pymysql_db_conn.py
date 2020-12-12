#!/usr/bin/python3
# PyMYSQL 连接 MySQL 数据库
# pip3 install PyMySQL
# conda install pymysql
import pymysql

# 创建数据库
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'tech'@'%' IDENTIFIED BY 'admin';

db = pymysql.connect("localhost", "tech", "admin", "testdb")

try:
    # 使用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute() 方法执行 SQL 查询
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()
except Exception as e:
    print(f"fetch error {e}")
finally:
    # 关闭数据库连接
    db.close

print(f"Database version : {result}")
