# Program to Show how to create a switch  
# import kivy module     
import kivy   
       
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
     
# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0') 
  
# Builder is used when .kv file is 
# to be used in .py file 
from kivy.lang import Builder 
  
# The screen manager is a widget 
# dedicated to managing multiple screens for your application. 
from kivy.uix.screenmanager import ScreenManager, Screen 
   
# You can create your kv code in the Python file 
Builder.load_string(""" 
<ScreenOne>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 2" 
            background_color : 0, 0, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_two' 
   
<ScreenTwo>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 3" 
            background_color : 1, 1, 0, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_three' 
  
<ScreenThree>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 4" 
            background_color : 1, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_four' 
  
<ScreenFour>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 5" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'screen_five' 
  
<ScreenFive>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 1" 
            background_color : 1, 0, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_one' 
  
  
""") 
   
# # Create a class for all screens in which you can include 
# # helpful methods specific to that screen 
# class ScreenOne(Screen): 
#     pass
   
# class ScreenTwo(Screen): 
#     pass
  
# class ScreenThree(Screen): 
#     pass
  
# class ScreenFour(Screen): 
#     pass
  
# class ScreenFive(Screen): 
#     pass
   
   
# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two")) 
screen_manager.add_widget(ScreenThree(name ="screen_three")) 
screen_manager.add_widget(ScreenFour(name ="screen_four")) 
screen_manager.add_widget(ScreenFive(name ="screen_five")) 
  
# Create the App class 
class ScreenApp(App): 
    def build(self): 
        return screen_manager 
  
# run the app  
sample_app = ScreenApp() 
sample_app.run() 