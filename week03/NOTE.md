# 学习笔记

## 1. MySQL安装

企业级 MySQL 部署在 Linux 操作系统上，需要注意的重点：

- 注意操作系统的平台（32位、64位）
- 注意安装 MySQL 的版本（MySQL 企业版、社区版、MariaDB）
- 注意安装后避免 yum 自动更新
- 注意数据库的安全性

```sql
show variables like 'validate_password%';

set global validate_password_policy=0;

alert user 'root'@'localhost' identified by 'new_password';
```



## 2. 正确使用MySQL字符集

```sql
-- 查看字符集
show variables like '%character%';
```

| Variable_name            | Value                          | -                                  |
| ------------------------ | ------------------------------ | ---------------------------------- |
| character_set_client     | utf8mb4                        | 从客户端发送语句的字符集           |
| character_set_connection | utf8mb4                        | 服务器将语句转换为处理的内容字符集 |
| character_set_database   | utf8mb4                        | 当前选中数据库的默认字符集         |
| character_set_filesystem | binary                         | filesystem文件系统                 |
| character_set_results    | utf8mb4                        | 响应结果字符集                     |
| character_set_server     | utf8mb4                        | 服务器内部操作字符集               |
| character_set_system     | utf8                           | 系统元数据字符集                   |
| character_set_dir        | /usr/share/mysql-8.0/charsets/ |                                    |

使用 create database 语句创建数据库时，如果未指定字符集，默认使用 character_set_server

创建表 继承 数据库字符集，字段 继承 表字符集。



```sql
-- 查看校对规则
show variables like 'collation_%';
```

| Variable_name        | Value              |
| -------------------- | ------------------ |
| collation_connection | utf8mb4_unicode_ci |
| collation_database   | utf8mb4_unicode_ci |
| collation_server     | utf8mb4_unicode_ci |

注意：MySQL 中的 utf8 不是 UTF-8 字符集

- 在 MySQL 中 utf8 使用3个字节，而常用的UTF-8字符集使用4个字节。如果需要使用4个字节存储，需要修改为 utf8mb4 。

- `_ci` 大小写不敏感；`_cs` 大小写敏感



```shell
vim /etc/my.cnf
```

```config
[client]
default-character-set=utf8mb4


[mysql]
default-character-set=utf8mb4

[mysqld]
# 针对交互式连接超时时间
interactive_timeout=28800
# 针对非交互式连接超时时间
wait_timeout=28800
# MySQL的最大连接数
max_connections=1000
# MySQL字符集设置
character-set-server=utf8mb4
# 服务器为每个连接的客户端执行的字符串
init_connect='SET NAMES utf8mb4'
character-set-client-handshake=FALSE
collation-server=utf8mb4_unicode_ci

# 事务隔离级别
# 串行化 SERIALIZABLE
# 重复度 REPEATABLE-READ
# 读提交  READ-COMMITTED
# 读未提交 READ-UNCOMMITTED
# transaction-isolation = READ-COMMITTED

# 动态调整刷新脏页的数量
# 动态调整 SET GLOBAL innodb_io_capacity = 2000;
innodb_io_capacity = 1000
```







## 3. 多种方式连接MySQL数据集

MySQLdb 是 Python2 的包，适用于 MySQL5.5 和 Python2.7。

Python3 安装的 MySQLdb 包叫做 mysqlclient，加载的依然是 MySQLdb

```shell
pip install mysqlclient
import MySQLdb
```

其他 DB-API

```shell
pip install pymysql # 流行度最高
pip install mysql-connector-python # MySQL官方
pip install sqlalchemy # 使用ORM
```

参考代码

- pymysql_db_conn.py
- sqlalchemy_core_conn.py
- sqlalchemy_orm_conn.py



## 4. 必要的SQL知识

### SQL语言功能划分

DQL：Data Query Language，数据库查询语言，开发工程师学习的重点。
DDL：Data Definition Language，数据库定义语言，操作库和表结构。
DML：Data Manipulation Language，数据操作语言，操作表中记录。
DCL：Data Control Language，数据控制语言，安全和访问权限控制。

### SQL执行顺序

```sql
CREATE TABLE `book` (
    `book_id` int(11) NOT NULL AUTO_INCREMENT,
    `type_id` int(11) NOT NULL,
    `book_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    PRIMARY KEY (`book_id`) USING BTREE
) ENGINE=InnoDB CHARACTER SET=utf8 COLLATE=utf8_general_ci;
```

```sql
SELECT DISTINCT book_id, book_name, count(*) as number   # 5
FROM book JOIN author ON book.sn_id = author.sn_id       # 1
WHERE pages > 500       # 2
GROUP BY book.book_id   # 3
HAVING number > 10      # 4
ORDER BY number         # 6
LIMIT 5                 # 7
```



## 5. 使用聚合函数汇总数据

- SQL函数有哪些？
  算术函数、字符串函数、日期函数、转换函数、聚合函数。

  
  
- 聚合函数

  COUNT() 行数
  MAX()   最大值
  MIN()   最小值
  SUM()   求和
  AVG()   平均值

> 聚合函数会忽略空行。



## 6. 子查询和join关键字解析

### 什么是子查询？

需要从查询结果集中再次进行查询，才能得到想要的结果。



### 子查询需要关注的问题？

关联子查询与非关联子查询的区别？

关联子查询何时使用IN，何时使用EXISTS

- 非关联子查询
```sql
select count(*), n_star from t1 group by n_star having n_star > 3 order by n_star desc;
```

```sql
select count(*), n_star from t1 group by n_star having n_star > (select avg(n_star) from t1) order by n_star desc;
```

- 关联子查询：何时使用IN，何时使用EXISTS
  - 小表驱动大表

in：B小于A

```sql
select * from table_a where condition in (select condition from table_b);
```

exists：A小于B

```sql
select * from table_a where exist (select condition from table_b where table_b.condition = table_a.condition)
```



### 常见的连接（JOIN）

(连接)[https://zh.wikipedia.org/wiki/%E8%BF%9E%E6%8E%A5]

- 自然连接
- ON 连接
- USING 连接
- 外连接
  - 左外连接
  - 右外连接
  - 全外连接（MySQL不支持，可使用UNION）



![img](assets/sql-join.png)



## 7. 事务的特性和隔离级别

### 什么事事务？

要么全执行，要么不执行。



### 事务的特性 ACID

| -           | -      | -    |
| ----------- | ------ | ---- |
| Atomicity   | 原子性 |      |
| Consistency | 一致性 |      |
| Isolation   | 隔离性 |      |
| Durability  | 持久性 |      |



```sql
show variables like 'autocommit';
set autocommit=0; -- 设置手动提交

begin -- 开启事务
commit -- 手动提交
rollback -- 回滚
```



### 事务的隔离级别

| -        | -                                                  |
| -------- | -------------------------------------------------- |
| 读未提交 | 允许读到未提交的数据                               |
| 读已提交 | 只能读到已经提交的内容                             |
| 可重复度 | 同一事务在相同查询条件下两次查询得到的数据结果一致 |
| 可串行化 | 事务进行串行化，但是牺牲了并发性能                 |

隔离级别越高，资源共享程度越低。






## 8. PyMySQL的增删改查操作演示

参考代码

- pymysql_db_delete.py
- pymysql_db_insert.py
- pymysql_db_insertmany.py
- pymysql_db_query.py
- pymysql_db_update.py



## 9. 如何设计一个良好的数据库连接配置文件

配置参考代码

- config.ini

```ini
[mysql]
host = localhost
database = testdb
user = tech
password = admin
```

读取和连接参考代码

- db_config.py
- pymysql_db_config_conn.py

```python
from dbconfig import read_db_config

dbserver = read_db_config

# `**dbserver` 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
db = pymysql.connect(**dbserver)
```



## 10. 使用SQLAlchemy

参考代码

- sqlalchemy_orm_conn.py
- sqlalchemy_orm_insert_select.py
- sqlalchemy_orm_update_delete.py



## 11. 使用连接池优化

参考代码

- db_conn_pool.py



## 12. 优化数据库使用的基本原则

- 阅读《阿里Java开发手册》数据库相关内容