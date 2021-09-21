import sqlite3
import os.path

class connection():

    def conect(self):
        # if(os.path.exists('../ficeliza.db')):
        conn = sqlite3.connect('../ficeliza.db')
        return conn
        # return False

    def cursor(self, conn):
        cursor = conn.cursor()
        return cursor

    def execute(self, cursor, instrucao):
        result = cursor.execute(instrucao)
        return result

    def conection_commit(self, conn):
        conn.commit()

    def conection_close(self, conn):
        conn.close()

    def get_all(self, response):
        return  response.fetchall()

    def get_one(self, response):
        return  response.fetchone()

