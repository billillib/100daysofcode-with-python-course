import psycopg2


class MyDB:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect("host=localhost dbname=test user=postgres "
                                     "password=docker")
        self.conn.autocommit = True

    def __exit__(self, *args):
        if self.conn:
            self.conn.close()
            self.conn = None
