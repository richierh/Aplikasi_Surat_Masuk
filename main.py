from kivy.lang import Builder
from kivymd.app import MDApp
from ui.view import MDData
# from kivy.core.window import Window
import os
from ui import view,mainw
# Window.size = (400, 700)
# Window.maximize()
from ui.theming import *
from kivy.utils import platform

class MainRun(MDApp):
    def build(self):
        # self.theme_cls.colors = colors
        # self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.primary_hue='100'
        # self.theme_cls.accent_palette = "Teal"
        # self.theme_cls.accent_hue='50'
        # self.color=self.theme_cls.primary_color

        mylistkv = []
        # this loop for list file with extension .kv only
        for file in os.listdir("ui"):
            if file.endswith(".kv"):
                print(os.path.join("/ui", file))
                mylistkv.append(os.path.join("", file))

        # this loop is for generating kv files to be read by python
        for kv_list in mylistkv :
            print(kv_list)
            Builder.load_file("ui/{}".format(kv_list))
            
            
  
        
        if platform == 'linux':
            if mainw.folderlinux():
                self.current = 'screen2'              
                print('kkkss')          
                
            else:
                pass
        self.load_kv = Builder.load_file("ui/mainw.kv")              

        return self.load_kv 

MainRun().run()