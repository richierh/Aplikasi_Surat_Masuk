from multiprocessing.util import close_all_fds_except
import sqlite3
from sqlite3 import Error

def close_connection(conn=None):
    # print("close connection successful")
    conn.close()
    

def create_connection(db_file=None,closedb = None):
    """ create a database connection to a SQLite database """
    conn = None
    if db_file :
        try:
            # print('connecting')
            conn = sqlite3.connect(db_file)
            # print(sqlite3.version)
            # print('connecting')
        except Error as e:
            # print(e)
            pass
        finally:
            if closedb :
                if conn:
                    conn.close()
    else:
        try:
            # print(sqlite3.version)
            pass
        except Error as e:
            print(e)        
        finally:
            if closedb :
                if conn:
                    conn.close()
    return conn

if __name__== "__main__":
    nama_file = 'core.db'
    connectdb = create_connection(nama_file)
    # print (connectdb)
    close_connection(connectdb)
    