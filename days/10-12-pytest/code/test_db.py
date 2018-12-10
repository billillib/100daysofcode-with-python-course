from db_object import MyDB
import psycopg2

import pytest


@pytest.fixture(scope='module')
def cur():
    print("creating connection")
    db = MyDB()
    db.conn = psycopg2.connect("host=localhost dbname=test user=postgres "
                               "password=docker")
    cur = db.conn.cursor()
    yield cur
    cur.close()
    db.conn.close()
    print("closing db")


def test_table_count(cur):
    cur.execute("SELECT COUNT(*) FROM test_table")
    result = cur.fetchone()

    assert int(result[0]) == 1


def test_table_value(cur):
    cur.execute("SELECT * FROM test_table")
    result = cur.fetchone()

    assert result == (1, 'a')
