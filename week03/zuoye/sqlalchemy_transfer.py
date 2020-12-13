#!/usr/bin/python3

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, create_engine, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User_table(Base):
    __tablename__ = 'user'
    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True, unique=True)


class Cash_table(Base):
    __tablename__ = 'cash'
    uid = Column(Integer(), primary_key=True, nullable=True)
    amount = Column(DECIMAL(19, 4), nullable=True)


class Record_tabl(Base):
    __tablename__ = 'record'
    user_id = Column(Integer(), primary_key=True)
    payee_id = Column(Integer(), primary_key=True)
    amount = Column(DECIMAL(19, 4), nullable=True)
    create_date = Column(DateTime(), nullable=True)


def init_data(session):
    user = User_table(name='曹操')
    payee = User_table(name='郭嘉')
    session.add(user)
    session.add(payee)
    session.commit()

    user_id = session.query(User_table.uid).filter(User_table.name=='曹操').one()[0]
    payee_id = session.query(User_table.uid).filter(User_table.name=='郭嘉').one()[0]
    print(f"user_id: {user_id} to payee_id: {payee_id}")

    c1 = Cash_table(uid=user_id, amount=100)
    c2 = Cash_table(uid=payee_id, amount=100)
    session.add(c1)
    session.add(c2)
    session.commit()


def transfer(user, payee, amount, session):
    user_id = session.query(User_table.uid).filter(
        User_table.name == user).one()[0]
    payee_id = session.query(User_table.uid).filter(
        User_table.name == payee).one()[0]

    user_amount = session.query(Cash_table.amount).filter(
        Cash_table.uid == user_id, Cash_table.amount >= amount).one()[0]
    payee_amount = session.query(Cash_table.amount).filter(
        Cash_table.uid == payee_id).one()[0]

    user_amount -= amount
    payee_amount += amount

    session.query(Cash_table.amount).filter(Cash_table.uid ==
                                            user_id).update({Cash_table.amount: user_amount})
    session.query(Cash_table.amount).filter(Cash_table.uid ==
                                            payee_id).update({Cash_table.amount: payee_amount})

    record = Record_tabl(user_id=user_id,
                         payee_id=payee_id,
                         create_date=datetime.now(),
                         amount=amount)
    session.add(record)


if __name__ == '__main__':
    dburl = "mysql+pymysql://tech:admin@localhost:3306/testdb?charset=utf8mb4"
    engine = create_engine(dburl, echo=True, encoding='utf-8')
    
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    Base.metadata.create_all(engine)

    # init_data(session)

    try:
        transfer('曹操', '郭嘉', 100, session)
    except Exception as e:
        print(f"transfer error {e}")
        session.rollback()
    finally:
        session.commit()
