import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem


kv = '''
Root:
    BoxLayout:
        orientation:'vertical'
        Button:
            text : "hit me"
            on_release:app.test()
'''

kv2 ='''
<Run>:
    text:["Oops! Something seems to have gone wrong!",]
    radius:[20, 7, 20, 7],
'''


class Root(FloatLayout):
    pass


class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class Run(MDDialog):
    pass


class MainWindow(MDApp):
    def build(self):
        Builder.load_string(kv2)
        return  Builder.load_string(kv)
    def test(self):
        print ("you hit me")
        P = Run()
        
        P.open()
        

if __name__=="__main__":
    MainWindow().run()