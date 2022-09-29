from models.sql_connection import create_connection,close_connection
from models.query import SelectAll,InsertData



if __name__ == '__main__':
    nama_file = 'core.db'
    connectdb = create_connection(nama_file)
    # masukkandata= InsertData(connectdb,['3','SSSDF','34','',''])
    lihat_data = SelectAll(connectdb)
    print(lihat_data)
    closedb = close_connection(connectdb)