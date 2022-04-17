from kivy.app import App
# from Second import Label2
from kivy.lang import Builder
from MDTable import Table

from kivy.properties import ObjectProperty

class First2App(App):
    presentate=ObjectProperty(None)

    def build(self):
        Builder.load_file('label2.kv')
        return Builder.load_file('first.kv')
    
    def change(self):
        print ("you are done")
    

First2App().run()