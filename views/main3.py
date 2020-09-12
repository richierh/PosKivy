'''
Application built from a  .kv file
==================================

This shows how to implicitly use a .kv file for your application. You
should see a full screen button labelled "Hello from test.kv".

After Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is
TestApp, which implies that kivy should try to load "test.kv". That file
contains a root Widget.
'''

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder 

Builder.load_file('views/button.kv')

class main_kv(GridLayout):

    pass


class MainApp(App):

    def build(self):


        return main_kv()

    pass


if __name__ == '__main__':
    # import os
    # p = os.path.abspath('..')
    MainApp().run()


