from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
import kivymd
from os.path import join, dirname
import os

from kivy.core.window import Window
Window.size = (800, 600)
# from py.main_screen import MainScreen
from py import main_screen,login_screen,navigation_main,register_screen,pos_kasir,\
    main_menu,product
from kivy.utils import platform

if platform == "android":
    from android.permissions import request_permissions, Permission 
    request_permissions([Permission.INTERNET,\
        Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class RunApplication(MDApp):
    # directory kivyddd
    # kv_directory = join(dirname(__file__), 'kv')

    def build(self):
        mylistkv = os.listdir('kv')
        for kv_list in mylistkv :
            print(kv_list)
            Builder.load_file("kv/{}".format(kv_list))
        self.load_kv = Builder.load_file('kv/mainscreen.kv')
        return self.load_kv
    # def on_start(self):
    #     icons_item = {
    #         "folder": "My files",
    #         "account-multiple": "Shared with me",
    #         "star": "Starred",
    #         "history": "Recent",
    #         "checkbox-marked": "Shared with me",
    #         "upload": "Upload",
    #     }
    #     # import pdb
    #     # pdb.set_trace()

    #     for icon_name in icons_item.keys():
    #         self.root.ids.content_drawer.ids.md_list.add_widget(
    #             ItemDrawer(icon=icon_name, text=icons_item[icon_name])
    #         )

if __name__=="__main__":
    RunApplication().run()
