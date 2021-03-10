# PostgreSQL과 연결하기 위한 설정 및 부모 클래스

import psycopg2
import os

# password = os.environ.get('postgresql_password')

class Databases():
    def __init__(self): # password 변경 필요
        self.db = psycopg2.connect(host='localhost', 
                                   dbname='t',
                                   user='postgres',
                                   password='1234',
                                   port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()            
        return row

    def commit(self):
        self.db.commit()

