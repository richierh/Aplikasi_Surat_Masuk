class InsertData():
    query = '''
    INSERT INTO [Surat Masuk]
    ([No Urut],[Surat Dari],[Nomor Surat],[Tanggal Surat],[Perihal])
    VALUES (?,?,?,?,?)
    '''

    def __init__(self,conn,*args,**kwargs):
        self.conn = conn
        self.data_insert = list(args)[0]
        self.cur = self.conn.cursor()
        self.query = getattr(InsertData,'query')
        self.cur.execute(self.query,self.data_insert)
        self.conn.commit()
             
    
    def __str__(self):
        return str('Masuukan data sukses')


class SelectAll():
    query = '''
    SELECT * FROM [Surat Masuk]
    '''
    
    query2 = '''
    SELECT MAX([No Urut]) FROM [Surat Masuk]
    '''

    def __init__(self,conn,*args,**kwargs):
        self.conn = conn
         
        self.cur = self.conn.cursor()
        self.query = getattr(SelectAll,'query')
        self.cur.execute(self.query)
        self.get_data = self.cur.fetchall() 
 
        self.cur= self.conn.cursor()
        self.query = getattr(SelectAll,'query')
        self.cur.execute(self.query2)
        self.data_num  = list(self.cur.fetchone())[0]
 
        self.get_datalist =[]
        for data in self.get_data:
            self.get_datalist.append(list(data))
            
        self.data_akhir=[]
        for data2 in self.get_datalist:
            self.get_datalist2 = [str(x) for x in data2]
            self.data_akhir.append(self.get_datalist2) 
        
    def last_num(self):
        # print (self.data_num)
        try:
            self.result = int(self.data_num)
        except:
            self.result=0
        return self.result
              
    def get(self):
        
        return self.data_akhir 
               
    
    def __str__(self):
        
        return str(self.data_akhir)


class RemoveData():
    query = '''
    DELETE FROM [Surat Masuk] WHERE [No Urut]=?    
    '''

    def __init__(self,conn,*args,**kwargs):
        self.conn = conn
        self.delete_data= list(args[0])[1]
        self.cur = self.conn.cursor()
        self.query = getattr(RemoveData,'query')
        self.cur.execute(self.query,[self.delete_data,])
        self.conn.commit()

            
    def del_data(self):
        self.result = 'sukses'
        return self.result
               
    
    def __str__(self):
        
        return str(self.data_akhir)

class AddingData():
    query='''
    INSERT INTO [Surat Masuk]([No Urut],[Surat dari],[Nomor Surat]
    ,[Tanggal Surat],[Perihal]) VALUES (?,?,?,?,?)
    
    '''
    
    def __init__(self,conn,*args,**kwargs):
        self.conn = conn
        self.adding_data= list(args)[0]
        # print(self.adding_data)
        # import pdb
        # pdb.set_trace()
        self.cur = self.conn.cursor()
        self.query = getattr(AddingData,'query')
        # print (self.query)
        self.cur.execute(self.query,self.adding_data)
        self.conn.commit()
        # print ('apa yang keluar dari sini')
        pass
    def add(self):
        pass
    
class SuratMasuk():
    
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        
    def last_queue(self):
        self.last_queue = SelectAll(self.parent)
        self.result = self.last_queue.last_num()
        return self.result
    
    def select_all(self):
        self.Select = SelectAll(self.parent)
        self.result = self.Select.get()
        return self.result
    
    def remove_data(self,*args):
        self.delete=list(args[0])
        self.Remove = RemoveData(self.parent,self.delete)
        self.result = self.Remove.del_data()
        return self.result
    
    def add_data(self,*args):
        self.add= list(args[0])
        # import pdb
        # pdb.set_trace()
        self.Adding = AddingData(self.parent,self.add)
        self.result = self.Adding.add()
        return self.result

if __name__=='__main__':
    nama_file = 'core.db'
    connectdb = create_connection(nama_file)
    # masukkandata= InsertData(connectdb,['3','SSSDF','34','',''])
    # print(masukkandata)
    selectdata = SelectAll(connectdb)
    # print(selectdata)
    closedb= close_connection(connectdb)
 