import psycopg2

class Connection:
    def __init__(self):
        self._user = 'postgres'
        self._password = 'postgres'
        self._host = '127.0.0.1'
        self._port = '5432'
        self._database = 'dw-initial-db'

        self.connection = None
        self.cursor = None

    def __init__(self, db):
        self._user = 'postgres'
        self._password = 'postgres'
        self._host = '127.0.0.1'
        self._port = '5432'
        self._database = db

        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(user = self._user, password = self._password, host = self._host, port = self._port, database = self._database)

        return self.connection

    def cursor(self):
        if self.connection:
            self.cursor = self.connection.cursor()

        return self.cursor

    def close(self):
        self.connection.close()
