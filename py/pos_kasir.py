from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivymd.uix.imagelist import SmartTileWithLabel
import os

class PosKasir(MDScreen):
    mygrid=ObjectProperty()
    scrollview=ObjectProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        # Buttons = ["sdf","sadfsdaf","asdfsda"]
        # for text in Buttons:
        #     button = MDRaisedButton(text="text",id=)
        #     self.mygrid.add_widget(button)
        # import pdb
        # pdb.set_trace()

        # Memperlihatkan list gambar dari produk
        # Tulisan dengan Ukuran besar diatas
        imagelistmy = ["Sunsilk","Kapal Api","Minyak Goreng"]
        # Tulisan dengan Ukuran dibawahnya
        imagelistmy2 =  ["Kemasan Kecil","Sachet Kecil","1 Liter"]
        # source gambar
        # source_gmbr = os.listdir(os.getcwd()+'/images/product')

        source_gmbr = os.listdir('images/product')

        # source_gmbr = ["cat.jpg","cat2.jpg","cat3.jpg"]

        for ima in imagelistmy:
            myimage = SmartTileWithLabel(size_hint_y=None, height= "240dp",source=f"images/product/{source_gmbr[imagelistmy.index(ima)]}"\
            ,text= f"[size=20]{ima}[/size]\n[size=14]{imagelistmy2[imagelistmy.index(ima)]}[/size]")
            self.ids.mygrid.add_widget(myimage)
        
        # Buttons = ["sdf","sadfsdaf","asdfsda"]
        # for text in Buttons:
        #     button = MDRaisedButton(text=text,size_hint=(1,None))
        #     # self.button.id = text
        #     button.bind(on_press=self.pressed)
        #     self.ids.mygrid.add_widget(button)
 
        print('this is online when start')
    def pressed(self,t):
        print(t.text)


    def on_kv_post(self, test):
        # import pdb
        # pdb.set_trace()
        # self.parent = test
        # Buttons = ["sdf","sadfsdaf","asdfsda"]
        # for text in Buttons:
        #     self.button = MDRaisedButton(text=text)
        #     self.ids.mygrid.add_widget(self.button)
        pass
 
    def back_mainmenu(self):
        # kembali ke screen mainmenu
        self.screenmanager.current='screen1'
        # import pdb
        # pdb.set_trace()



