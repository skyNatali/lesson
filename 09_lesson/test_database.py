from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import Generator


db_connection_string = "postgresql://postgres@localhost:5432/QA"

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'users'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from users").fetchall()
    row1 = rows[0]
    
    assert row1["user_id"] == 42568
    assert row1["user_email"] == "igorpetrov@mail.ru"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from users where user_id = :user_id")

    rows = db.execute(sql_statement, {"user_id": 42568}).fetchall()

    assert len(rows) == 1
    assert rows[0]["user_email"] == "igorpetrov@mail.ru"

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO users(user_email) VALUES (:new_user_email)")

    rows = db.execute(sql, {"new_user_email": "nana123@mail.ru", "new_subject_id": 1})
    assert rows.rowcount == 1

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set subject_id = :descr where user_email = :user_email")
    
    db.execute(sql, descr='1', user_email="nana123@mail.ru")

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users WHERE user_email = :user_email")
    
    db.execute(sql, user_email = 'nana123@mail.ru')
    







# engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @contextmanager
# def get_db() -> Generator[Session, None, None]:
#     """Генератор сессий для работы с БД"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# # Для psycopg2 (наверно нужно создать файл):
# import psycopg2
# conn = psycopg2.connect(
#     host="localhost",
#     port=5432,
#     database="QA",
#     user="postgres",
#     password=""  # пустой пароль
# )