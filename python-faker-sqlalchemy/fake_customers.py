import time
import sqlite3

from faker import Faker

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,  create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    ipv4_private = Column(String(255))
    date_time = Column(String(255))
    credit_card_number = Column(String(255))
    free_email = Column(String(255))


def init_sqlalchemy(dbname='sqlite:///sqlalchemy.db'):
    global engine
    engine = create_engine(dbname, echo=False)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def test_sqlalchemy_orm(n: int, fake: Faker) -> None:
    init_sqlalchemy()
    t0 = time.time()
    for i in range(n):
        customer = Customer()
        customer.name = fake.name()
        customer.address = fake.address()
        customer.ipv4_private = fake.ipv4_private()
        customer.date_time = fake.date_time()
        customer.credit_card_number = fake.credit_card_number()
        customer.free_email = fake.free_email()
        DBSession.add(customer)
        if i % 1000 == 0:
            DBSession.flush()
    DBSession.commit()
    print(
        "SQLAlchemy ORM: Total time for " + str(n) +
        " records " + str(time.time() - t0) + " secs")


def test_sqlalchemy_orm_pk_given(n: int, fake: Faker) -> None:
    init_sqlalchemy()
    t0 = time.time()
    for i in range(n):
        customer = Customer(
            id=i+1,
            name=fake.name(),
            address=fake.address(),
            ipv4_private=fake.ipv4_private(),
            date_time=fake.date_time(),
            credit_card_number=fake.credit_card_number(),
            free_email=fake.free_email()
        )
        DBSession.add(customer)
        if i % 1000 == 0:
            DBSession.flush()
    DBSession.commit()
    print(
        "SQLAlchemy ORM pk given: Total time for " + str(n) +
        " records " + str(time.time() - t0) + " secs")


def test_sqlalchemy_orm_bulk_insert(n: int, fake: Faker) -> None:
    init_sqlalchemy()
    t0 = time.time()
    n1 = n
    while n1 > 0:
        n1 = n1 - 10000
        DBSession.bulk_insert_mappings(
            Customer,
            [
                dict(
                        name=fake.name(),
                        address=fake.address(),
                        ipv4_private=fake.ipv4_private(),
                        date_time=fake.date_time(),
                        credit_card_number=fake.credit_card_number(),
                        free_email=fake.free_email()
                     )
                for i in range(min(10000, n1))
            ]
        )
    DBSession.commit()
    print(
        "SQLAlchemy ORM bulk_save_objects(): Total time for " + str(n) +
        " records " + str(time.time() - t0) + " secs")


def test_sqlalchemy_core(n: int, fake: Faker) -> None:
    init_sqlalchemy()
    t0 = time.time()
    with engine.connect() as conn:
        conn.execute(
            Customer.__table__.insert(),
            [{"name": fake.name(),
                "address": fake.address(),
                "ipv4_private": fake.ipv4_private(),
                "date_time": fake.date_time(),
                "credit_card_number": fake.credit_card_number(),
                "free_email": fake.free_email()
              } for i in range(n)]
        )
    print(
        "SQLAlchemy Core: Total time for " + str(n) +
        " records " + str(time.time() - t0) + " secs")


def init_sqlite3(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS customer")
    c.execute(
        """CREATE TABLE customer (
                id INTEGER NOT NULL, 
                name VARCHAR(255),
                address VARCHAR(255),
                ipv4_private VARCHAR(255),
                date_time VARCHAR(255),
                credit_card_number VARCHAR(255),
                free_email VARCHAR(255),
                PRIMARY KEY(id)
            )"""

    )
    conn.commit()
    return conn


def test_sqlite3(n: int, fake: Faker, dbname: str ='sqlite3.db') -> None:
    conn = init_sqlite3(dbname)
    c = conn.cursor()
    t0 = time.time()
    for i in range(n):
        row = (
                fake.name(),
                fake.address(),
                fake.ipv4_private(),
                fake.date_time(),
                fake.credit_card_number(),
                fake.free_email(),
        )
        c.execute("""INSERT INTO customer (
                        name, 
                        address,
                        ipv4_private,
                        date_time,
                        credit_card_number,
                        free_email
                    ) 
                    VALUES (?, ?, ?, ?, ?, ?)""", row)
    conn.commit()
    print(
        "sqlite3: Total time for " + str(n) +
        " records " + str(time.time() - t0) + " sec")

if __name__ == '__main__':
    fake = Faker(['en_US'])
    n = 100_000
    test_sqlalchemy_orm(n, fake)
    test_sqlalchemy_orm_pk_given(n, fake)
    test_sqlalchemy_orm_bulk_insert(n, fake)
    test_sqlalchemy_core(n, fake)
    test_sqlite3(n, fake)
