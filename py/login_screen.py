from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):

    def login(self):
        self.manager.current = "navigationmain"

        print("hh")
    def sign_up(self):
        self.manager.current = "signup"
        print("go to sign up screen")