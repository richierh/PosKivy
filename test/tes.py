from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
kv = '''
BoxLayout:
    orientation:"vertical"
    # column_data:column_data
    MDDataTable:
        column_data:[("head",dp(20)),("Number",dp(30))]
    # MDLabel:
    #     text:"berhasil"

'''


class RunningApp(MDApp):
    column_data = ListProperty([{"col 1":"row 11","col 2":"row 21"},{"col 1":"row 12","col 2":"row 22"}],allownone=True)

    def build(self):
        return Builder.load_string(kv)

RunningApp().run()