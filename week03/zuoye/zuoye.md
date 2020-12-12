1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

- 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交

  修改配置项

  ```shell
  vim /etc/my.cnf
  ```

  ```sql
  [client]
  default-character-set=utf8mb4
  
  [mysql]
  default-character-set=utf8mb4
  
  [mysqld]
  # MySQL字符集设置
  character-set-server=utf8mb4
  # 服务器为每个连接的客户端执行的字符串
  init_connect='SET NAMES utf8mb4'
  character-set-client-handshake=FALSE
  collation-server=utf8mb4_unicode_ci
  ```

  验证字符集

  ```sql
  -- 查看字符集
  show variables like '%character%';
  -- 查看校对规则
  show variables like 'collation_%';
  ```

  

- 将增加远程用户的 SQL 语句作为作业内容提交

  ```sql
  CREATE USER 'tech'@'%' IDENTIFIED WITH mysql_native_password BY 'admin';
  GRANT ALL PRIVILEGES ON *.* TO 'tech'@'%';
  ```



2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

- 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间

- 将 ORM、插入、查询语句作为作业内容提交

  

  > 代码： [sqlalchemy_orm_2.py](./sqlalchemy_orm_2.py)



3. 为以下 sql 语句标注执行顺序：

   ```sql
   SELECT DISTINCT player_id, player_name, count(*) as num  #5
   FROM player JOIN team ON player.team_id = team.team_id   #1
   WHERE height > 1.80                                      #2
   GROUP BY player.team_id                                  #3
   HAVING num > 2                                           #4
   ORDER BY num DESC                                        #6
   LIMIT 2                                                  #7
   ```

   

4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

    **Table1**

    | id   | name          |
    | ---- | ------------- |
    | 1    | table1_table2 |
    | 2    | table1        |

    **Table2**

    | id   | name          |
    | ---- | ------------- |
    | 1    | table1_table2 |
    | 3    | table2        |



- INNER JOIN

    ```sql
    SELECT Table1.id, Table1.name, Table2.id, Table2.name
    FROM Table1
    INNER JOIN Table2
    ON Table1.id = Table2.id;
    ```

    | id   | name          | id   | name          |
    | ---- | ------------- | ---- | ------------- |
    | 1    | table1_table2 | 1    | table1_table2 |

    

- LEFT JOIN

    ```sql
    SELECT Table1.id, Table1.name, Table2.id, Table2.name
    FROM Table1
    LEFT JOIN Table2
    ON Table1.id = Table2.id;
    ```

    | id   | name          | id   | name          |
    | ---- | ------------- | ---- | ------------- |
    | 1    | table1_table2 | 1    | table1_table2 |
    | 2    | table1        | NULL | NULL          |



- RIGHT JOIN

    ```sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
    FROM Table1
    RIGHT JOIN Table2
    ON Table1.id = Table2.id;
    ```

    | id   | name          | id   | name          |
    | ---- | ------------- | ---- | ------------- |
    | 1    | table1_table2 | 1    | table1_table2 |
    | NULL | NULL          | 3    | table2        |



5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。



6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

- 请合理设计三张表的字段类型和表结构；
- 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。