from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import NavigationLayout

class PosScreen(Screen):
    pos_m=ObjectProperty(None)
    # popup=ObjectProperty(None)
    nav_drawer=ObjectProperty(None)
    pass

    def hello(self):
        print("aaaaa")

    def popup(self):
        print("test here")

class MDToolbarKu(MDToolbar):

    pass
    def popup(self):
        print("test from toolbar here")

class Navigation(NavigationLayout):
    nav = ObjectProperty(None)
    pass