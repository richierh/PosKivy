from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty

class RegisterScreen(MDScreen):
    # successscreen = ObjectProperty()

    def go_back_mainscreen(self):
        print("go back")
        self.mainscreen.current='login_screen'
        # import pdb
        # pdb.set_trace()

    def go_forward(self):

        print("go forward")

        self.myscreenmanager.current='myscreen'
        pass

    def continue_login(self):
        print('horee yay')
        self.manager.current = 'navigationmain'

class FirstScreen(MDScreen):

    pass

class Success(MDScreen):
    
    pass