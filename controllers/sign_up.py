from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class SignUpScreen(Screen):
    signup=ObjectProperty(None)
    pass

   
    def create(self):
        print ("you just create account")

    def left(self):
        print("back screen")
        self.parent.screen_manager.current="login_m"