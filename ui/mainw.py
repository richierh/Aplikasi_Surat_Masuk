from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.utils import platform
import os.path
from pathlib import Path, PurePosixPath
from kivy.clock import Clock


class Screen2(Screen):
    pass

class Screen12(Screen):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def on_pre_enter(self):
        Clock.schedule_once(self.switch_screen)

    def switch_screen(self,*args):
        if platform == 'linux':
            if folderlinux():
                self.parent.current='screen2'

        print ('sdfdsf')
        
        
class MainW(ScreenManager):
    mainw=ObjectProperty()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    
    def verifikasi(self,*args):
        self.text_input = list(args)[0]
        if platform == 'linux':
            if self.text_input == 'tessaja':
                self.current='screen2'
            else:
                print ('not matching')

            mypath = '/home/richie/'
            save_path = str(Path(mypath))

            # name_of_file = input("What is the name of the file: ")
            name_of_file = 'txvfenk'
            completeName = os.path.join(save_path, name_of_file+".txt")   

           
            with open(os.path.join(save_path,completeName), "w") as file1:
                toFile = 'saving important verification'
                file1.write(toFile)            
            file1.close()

        elif platform == 'android':
            print('this is android')
            
        elif platform == 'win':
            print('this is window')


            if self.text_input == 'tessaja':
                self.current='screen2'
            else:
                pass
        if self.text_input == 'tessaja':
            self.current='screen2'
        else:
            print ('not matching')

def folderwindow():
    try:
        mypath = "C:\\Users\\"
        save_path = str(Path(mypath))
        name_of_file = 'txvfenk'
        completeName = os.path.join(save_path, name_of_file+".txt")   
        # import pdb
        # pdb.set_trace()
        with open(os.path.join(save_path,completeName), "r") as file1:
            # toFile = 'saving important verification'
            dataread = file1.read()     
        file1.close()
    except:
        dataread = False
    return True

def folderlinux():
    try:
        mypath = '/home/richie/'
        save_path = str(Path(mypath))

        # name_of_file = input("What is the name of the file: ")
        name_of_file = 'txvfenk'
        completeName = os.path.join(save_path, name_of_file+".txt")   
        # import pdb
        # pdb.set_trace()
        with open(os.path.join(save_path,completeName), "r") as file1:
            # toFile = 'saving important verification'
            dataread = file1.read()     
        file1.close()
        print('keluardonk')
        a = True
    except:
        a =False
    return a