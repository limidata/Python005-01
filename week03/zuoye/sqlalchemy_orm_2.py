#!/usr/bin/python3

import pymysql
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, Enum, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

db = pymysql.connect("localhost", "tech", "admin", "testdb")

Base = declarative_base()

class Student_table(Base):
    __tablename__ = 'student'

    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(Boolean(), nullable=False)
    edu = Column(Enum("中学", "专科", "本科", "硕士", "博士"))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)

    def __repr__(self):
        return f'id={self.id}, name={self.name}, age={self.age}, ' \
               f'birthday={self.birthday}, sex={self.sex}, edu={self.edu}, ' \
               f'create_on={self.create_on}, update_on={self.update_on}'


# 实例一个引擎
def create_table():
    dburl = "mysql+pymysql://tech:admin@localhost:3306/testdb?charset=utf8mb4"
    engine = create_engine(dburl, echo=True, encoding="utf-8")

    Base.metadata.create_all(engine)


def insert_many():
    SQL = """INSERT INTO student (name, age, birthday, sex, edu, create_on, update_on)
    values (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        ('荀彧', '25', datetime(1000, 3, 15), 1, '本科', datetime.now(), datetime.now()),
        ('郭嘉', '28', datetime(1000, 3, 15), 0, '硕士', datetime.now(), datetime.now()),
        ('曹操', '30', datetime(1000, 3, 15), 0, '博士', datetime.now(), datetime.now())
    )
    with db.cursor() as cursor:
        cursor.executemany(SQL, values)
    db.commit()

def read():
    SQL = """SELECT * FROM student WHERE name=%s"""
    with db.cursor() as cursor:
        cursor.execute(SQL, '曹操')
        result = cursor.fetchall()
        print(result)
    db.commit()


# create_table()
# insert_many()
read()
