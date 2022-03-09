import sys
import os
from os.path import exists

# to make append directory of different folder so it makes easier to import python module
# print(os.pardir())
# print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
# print(os.getcwd())

sys.path.append(os.getcwd())
from databases.db_connection import *


import sqlite3
# print (sys.path.append(os.getcwd()))

name='main.db'

def exist_data():
    if exists(f'databases/{name}') :
        print('this file is exists')
        connection = sqlite3.connect(f'databases/{name}')
    return connection


class CreateTable():

    def __init__(self):
        self.conn = exist_data()
        self.executecursor = self.conn.cursor()
        self.executecursor.execute(self.__sql_command())
        self.conn.commit()
        self.conn.close()

        pass
    def __sql_command(self):
        self.sql_cmd = '''
        CREATE TABLE IF NOT EXISTS Login (
        username data_type PRIMARY KEY,
        password data_type NOT NULL,
        value data_type DEFAULT 0,
        table_constraints
        );
        '''
        return self.sql_cmd

if __name__=="__main__":
    run_app = CreateTable()
    # t = run_app.sql_command()
    # print(t)