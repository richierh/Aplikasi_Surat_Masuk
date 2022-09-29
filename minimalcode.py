from calendar import c
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
    

KV = """
Box:
    orientation: 'vertical'
    padding: (0,0,0,100)

    MDLabel:
        size_hint:1,None
        text:'This Is The Table Example'
        halign : 'center'
    MDData:
        size_hint: 1, .6
        id:mddata
    MDRaisedButton:
        size_hint:.3,None
        # size:100,50
        text:'delete'
        on_release : mddata.delete()
        pos_hint: {'center_x': 0.5,'center_y': 0.5}

"""
data = [
    ["1","Asep Sudrajat","993493","Male","Soccer","Blue"],
    ["2","Egy","993493","Male","Soccer","Red"],
    ["3","Fuck Trump","6666","Demon","Soccer","Purple"],    
    ["4","Witan","993493","Male","Soccer","Yellow"],
    ["5","Nadeo","993493","Male","Soccer","Green"],
]

class Box(MDBoxLayout):
    pass


class MDData(Screen):
   
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.data = data
        self.run_table()
          
    def run_table(self):
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
        return True
    
    def on_row_press(self,instance_table,instance_row):
        # import pdb
        # pdb.set_trace()
        
        self.get_row = instance_row
        pass
    
    def on_check_press(self,index,row_data_list):
        self.a = row_data_list
        self.b = index
        self.k  = self.data_tables.get_row_checks()
        print (self.b)

        
        
    
    def delete(self):

        print('running')
        self.b.check = False
        self.b.get_row_checks()
        self.data_tables.get_row_checks()
        for data in self.b.get_row_checks():
            self.b.remove_row(data)
        # self.b.check = True
        # import pdb
        # pdb.set_trace()
        # Clock.schedule_once(self.on_check_press(self.b,self.a))

        pass

class MyApp(MDApp):
    def build(self):
        self.kv_run = Builder.load_string(KV)
        return self.kv_run

if __name__=="__main__":
    MyApp().run()