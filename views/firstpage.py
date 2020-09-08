
from kivymd.app import MDApp
# from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivymd.uix.button import MDTextButton,MDRectangleFlatButton

kv = """
AnchorLayout :
    orientation : 'vertical'
    MDRectangleFlatButton:
        text :"hello"
        custom_color : 1,0,0,1
        anchor_x : 'center'
        anchor_y : 'center'
        size_hint : .15,.15
        
"""

# class LayoutFirst(BoxLayout):

#     pass


class MainWindow(MDApp):

    def build(self):
    
        theme_cls = ThemeManager()

        layout = Builder.load_string(kv)
        # self.boxl = LayoutFirst()
        return layout


    
if __name__=="__main__":
    MainWindow().run()