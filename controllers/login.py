from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
class LoginScreen(Screen):
    login_m = ObjectProperty(None)

    pass

    def sign_in(self):
        self.parent.screen_manager.current="pos_m"            
        print("Sign_in Succeeded")

        try:
            self.parent.Start_Screen.current="pos_m"            
            print("Sign_in Succeeded")

        except :

            print("Sign in failed , ")
