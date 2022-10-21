from multiprocessing.managers import ListProxy
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from models.sql_connection import create_connection,close_connection
from models.query import RemoveData, SelectAll,InsertData, SuratMasuk
from kivy.properties import ObjectProperty,ListProperty
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextFieldRect
from kivy.clock import Clock


class Profile(Screen):
    pass

class NoUrut(MDTextFieldRect):
    
    pass

class MyMDGridLayout(MDGridLayout):
    listinput = ListProperty()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # adding liststring
        self.AddQueue = MDData()
        self.Add = str(self.AddQueue.last_queue+1)
        self.listinput = [self.Add,'','','','']
     

class MDData(Screen):
    
    mddata = ObjectProperty()
    listdata=ObjectProperty(['','','','',''])
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.nama_file = 'core.db'
        self.connectdb = create_connection(self.nama_file)
        self.SuratMasuk = SuratMasuk(self.connectdb)
        self.last_queue = self.SuratMasuk.last_queue()
        self.run_table(self.SuratMasuk.select_all())
        self.closedb = close_connection(self.connectdb)
    
    def profile(self):
        # Disini diisi dengan data dari profil yang di click
        if len(self.data_tables.get_row_checks()) == 1:
            self.data_tables.get_row_checks()
            self.mainw.current='profile'
        
            
    def delete(self,*args):
        def deselect_rows(*args):
            self.data_tables.table_data.select_all("normal")

        # ini adalah fungsi delete yang ada di widget MDRaisedButton
        # print('berfungsi dengan sempurna')

        # print (self.data_tables.get_row_checks())
        # print (self.k)
        for data_del in self.data_tables.get_row_checks():
            data_del[0] = int(data_del[0])
            self.connectdb = create_connection(self.nama_file)
            self.SuratMasuk = SuratMasuk(self.connectdb)
            self.SuratMasuk.remove_data(data_del)
            self.closedb = close_connection(self.connectdb)
            self.data_tables.remove_row(data_del)
            # self.refresh()

        for textinput in args:
            textinput.text = ''
            if list(args).index(textinput) == 0:
                self.connectdb = create_connection(self.nama_file)
                self.SuratMasuk = SuratMasuk(self.connectdb)
                self.last_queue = self.SuratMasuk.last_queue()
                self.closedb = close_connection(self.connectdb)
                self.Add = int(self.last_queue)+1
                textinput.text = str(self.Add)




        Clock.schedule_once(deselect_rows)


                
    def refresh(self,*args):
        try:
            self.update=MDData()
            self.data_tables.update_row_data(self.update.data_tables,self.update.data_tables.row_data)

        except:
            pass

        for textinput in args:
            textinput.text = ''
            if list(args).index(textinput) == 0:
                self.connectdb = create_connection(self.nama_file)
                self.SuratMasuk = SuratMasuk(self.connectdb)
                self.last_queue = self.SuratMasuk.last_queue()
                self.closedb = close_connection(self.connectdb)
                self.Add = int(self.last_queue)+1
                textinput.text = str(self.Add)

        
        
        # def update_rowlast(*args):
        #     self.data= NoUrut()
        #     # import pdb
        #     # pdb.set_trace()
        #     pass
            
        # Clock.schedule_once(update_rowlast)

                
    def add(self,*args):
        self.list = []
        for textinput in args:
            self.list.append(textinput.text)
        data_add = self.list
        if data_add[0] != '' or data_add[1]!='':
            self.connectdb = create_connection(self.nama_file)
            self.SuratMasuk = SuratMasuk(self.connectdb)
            self.SuratMasuk.add_data(data_add)
            self.closedb = close_connection(self.connectdb)
            self.refresh()
            data_add[0]=''
            # self.gridlayout = MyMDGridLayout()
            for textinput in args:
                textinput.text = ''
                if list(args).index(textinput) == 0:
                    self.connectdb = create_connection(self.nama_file)
                    self.SuratMasuk = SuratMasuk(self.connectdb)
                    self.last_queue = self.SuratMasuk.last_queue()
                    self.closedb = close_connection(self.connectdb)
                    self.Add = int(self.last_queue)+1
                    textinput.text = str(self.Add)
              
        pass

    def run_table(self,data):
        # jenis data adalah list
        # [['','','','',''],['','','','',''],['','','','',''],['','','','','']] dst
        self.dataku = data
        self.data= []
        for data in self.dataku :
            data.pop(0)
            data.insert(0,self.dataku.index(data)+1)
            # print (data)
            # print('dssf')
            self.data.append(data)
        self.data_tables = MDDataTable(
            size_hint=(1,1),
            pos_hint = {'center_x': 0.5,'center_y': 0.5},
            use_pagination=True,
            check=True,
            # name column, width column, sorting function column(optional), custom tooltip
            column_data=[
                ("No", dp(30), None),
                ("No Urut.", dp(30), None, "Custom tooltip"),
                ("Alamat Pengirim", dp(30)),
                ("No Surat", dp(60)),
                ("Tanggal Surat", dp(30)),
                ("Perihal", dp(100)),
            ]
        )
        self.data_tables.row_data=self.data
        self.add_widget(self.data_tables)
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
    
    def on_row_press(self,instance_table,instance_row):
        pass
    
    def on_check_press(self,index,row_data_list):
        self.a = row_data_list
        self.b = index
        self.k  = self.data_tables.get_row_checks()
        # print (self.b)
        # print(self.a)
        # print(self.data_tables.get_row_checks())
        
        pass