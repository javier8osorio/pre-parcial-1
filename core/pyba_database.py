import pymysql


class PybaDatabase:
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "12345"
        self.database = "progra"
        self.connection = self.createConnection()
        self.cursor = self.createCursor()

    def createConnection(self):
        con = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            database=self.database,
            charset="utf8mb4",
            cursorClass=pymysql.cursors.DictCursor,
        )
        return con

    def createCursor(self):
        con = self.connection
        cursor = None
        if con is not None:
            cursor = con.cursor()
        else:
            print("no esta conectado a la base de datos")

        return cursor

    def executeQuery(self, sql):
        cursor = self.cursor
        result = None
        if cursor is not None:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result

    def executeNonQueryBool(self, sql):
        cursor = self.cursor
        con = self.connection
        sucess = False
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                sucess = True

        return sucess

    def executeNonQueryRows(self, sql):
        cursor = self.cursor
        con = self.connection
        sucess = False
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount

        return rows
