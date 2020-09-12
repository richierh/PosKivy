from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.button import Button
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton
from views.OpenDialog import OpenDialog

class MainWindow(ScreenManager):
    pass

# class OpenDialog(BoxLayout):
#     pass


class ScreenManagerApp(MDApp):

    dialog=None

    def build(self):
        # Builder.load_file("views/coba.kv")
        Builder.load_file("views/navi.kv")  
        Builder.load_file("views/popups.kv")
        S = Builder.load_file("views/main.kv")
        Builder.load_file("views/login.kv")
        Builder.load_file("views/posscreen.kv")

        # Builder.load_string(kv_screen1)
        # Builder.load_string(kv_screen2)
        Window.size =  (400,600)
        self.title = "Point Of sales - Kivy"
        return MainWindow()


    def popup(self):
        print ("success")

        if not self.dialog:
            self.dialog=MDDialog(
            type="custom",
            size_hint=(.7, .6),
            content_cls=OpenDialog(),               
            )
        self.dialog.open()
        return 


def main():
    ScreenManagerApp().run()


if __name__ == '__main__':
    main()




# from views.Navi import Navi

# kv_main = """
# ScreenManager:
#     LoginScreen:

#     PosScreen:
#         name:"pos_m"

# """

# kv_screen1 = """
# <LoginScreen@Screen>:
#     BoxLayout: 
#         orientation:"horizontal"
#         AnchorLayout:
#             anchor_x:'right'
#             anchor_y:'center' 
#             padding : 10
#             MDRectangleFlatIconButton:
#                 text: "Sign In"
#                 icon: "login"
#                 # text_color: 0, 0, 1, 1
#                 # md_bg_color: 1, 1, 0, 1
#                 size: 130, 50
#                 # pos_hint :{"center_x":.5,"center_y":.5}
#                 on_release:app.root.current = 'pos_m'
        
#         AnchorLayout:
#             anchor_x:'left'
#             anchor_y:'center' 
#             padding: 10
#             MDRectangleFlatIconButton:
#                 text: "Sign Up"
#                 # text_color: 0, 0, 1, 1
#                 # md_bg_color: 1, 1, 0, 1
#                 size: 125, 50
#                 pos_hint :{"center_x":.5,"center_y":.5}
#                 on_release:app.root.current = 'pos_m'
    
# """
# kv_screen2 = """
# <PosScreen@Screen>:
#     Navi:
# """
