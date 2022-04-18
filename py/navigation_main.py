from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.list import OneLineIconListItem,MDList
from kivymd.theming import ThemableBehavior
from kivy.uix.scrollview import ScrollView


class NavigationMain(MDScreen):
    screenmanager=ObjectProperty()
    navigationtoolbar=ObjectProperty()
    Navigationmain=ObjectProperty()
    screen2=ObjectProperty()
    def toggle_nav_drawer(self):
        pass


class ContentNavigationDrawer(MDBoxLayout):
    navigationmain=ObjectProperty()
    screenmanager = ObjectProperty()
    nav_drawer = ObjectProperty()
    screen1 = ObjectProperty()
    navigationtoolbar = ObjectProperty()

    def toggle_nav_drawer(self):
        pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    pass


class DrawerList(ThemableBehavior, MDList):
    md_list = ObjectProperty()

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
            
    def penjualan(self):
        print ('hhh')
        # import pdb
        # pdb.set_trace()
        self.nav_drawer.set_state('close')
        self.screenmanager.current='screen2'
        self.navigationtoolbar.title="Cash Register"
        # self.parent.parent.parent.parent.parent.manager.current='screen2'    
        # /self.ids.manager.current
    
    def product(self):
        self.nav_drawer.set_state('close')
        self.screenmanager.current='product'
        self.navigationtoolbar.title="Produk"

    def logout(self):
        print("logout")
        self.mainscreen.current="login_screen"