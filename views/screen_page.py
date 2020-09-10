from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.button import Button
from kivymd.uix.navigationdrawer import MDNavigationDrawer

kv_main = """
ScreenManager:
    LoginScreen:

    PosScreen:
        name:"pos_m"

"""

kv_screen1 = """
<LoginScreen@Screen>:
    BoxLayout: 
        orientation:"horizontal"
        AnchorLayout:
            anchor_x:'right'
            anchor_y:'center' 
            padding : 10
            MDRectangleFlatButton:
                text: "Sign In"
                text_color: 0, 0, 1, 1
                md_bg_color: 1, 1, 0, 1
                size: 75, 50
                # pos_hint :{"center_x":.5,"center_y":.5}
                on_release:app.root.current = 'pos_m'
        
        AnchorLayout:
            anchor_x:'left'
            anchor_y:'center' 
            padding: 10
            MDRectangleFlatButton:
                text: "Sign Up"
                text_color: 0, 0, 1, 1
                md_bg_color: 1, 1, 0, 1
                size: 75, 50
                # pos_hint :{"center_x":.5,"center_y":.5}
                on_release:app.root.current = 'pos_m'
    
"""
kv_screen2 = """
<PosScreen@Screen>:
    Navi:
"""

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Button2(Button):
    pass

class PosScreen(Screen):
    pass
class LoginScreen(Screen ):
    pass

class ScreenM(ScreenManager):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        s1 = ScreenManager()
        s1.add_widget(PosScreen())
        s1.add_widget(LoginScreen())


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

    def on_start(self):
            icons_item = {
                "folder": "My files",
                "account-multiple": "Shared with me",
                "star": "Starred",
                "history": "Recent",
                "checkbox-marked": "Shared with me",
                "upload": "Upload",
            }
            for icon_name in icons_item.keys():
                self.root.ids.content_drawer.ids.md_list.add_widget(
                    ItemDrawer(icon=icon_name, text=icons_item[icon_name])
                )


class ScreenManagerApp(MDApp):

    def build(self):
        # Builder.load_file("views/coba.kv")
        Builder.load_file("views/navi.kv")
        Builder.load_string(kv_screen1)
        Builder.load_string(kv_screen2)
        Window.size =  (400,600)
        self.title = "Point Of sales - Kivy"
        return Builder.load_string(kv_main)

def main():
    ScreenManagerApp().run()


if __name__ == '__main__':
    main()