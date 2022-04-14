from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.widget import MDWidget
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import os
global k 

class MyWidget(MDBoxLayout):

    def __init__(self,**kwds):
        super().__init__(**kwds)

    def decrease(self):
        global k

        print('decrease')
        if not int(self.ids.myvalue.text) <= 0 :
            self.ids.myvalue.text = str(int(self.ids.myvalue.text)-1)
        k = self.ids.myvalue.text

        return k    
    def increase(self):
        global k

        print('increase')
        self.ids.myvalue.text = str(int(self.ids.myvalue.text)+1)
        k = self.ids.myvalue.text

        return k

class BarcodeWidget(MDBoxLayout):
    pass

# class ini belum memberikan data yang akurat sehingga menyebabkan tulisan
# firt_data_item = self.items[0]
# IndexError: list index out of range

class DataTable(MDBoxLayout):
    # screenb=ObjectProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.load_table()
        # import pdb
        # pdb.set_trace()
        self.add_widget(self.load_table())
        # self.size_hint = (0.7,1)
        
        pass
    def load_table(self):
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            check=True,
            # name column, width column, sorting function column(optional)
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60)),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30), lambda *args: print("Sorted using Schedule")),
                ("Team Lead", dp(30)),
            ],)
        return self.data_tables

class PosKasir(MDScreen):
    myvalue=ObjectProperty()
    mygrid=ObjectProperty()
    scrollview=ObjectProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_leave(self):
        print('go out')
        imagelistmy = ["Sunsilk","Kapal Api","Minyak Goreng"]
        # Tulisan dengan Ukuran dibawahnya
        imagelistmy2 =  ["Kemasan Kecil","Sachet Kecil","1 Liter"]
        # source gambar
        # source_gmbr = os.listdir(os.getcwd()+'/images/product')

        source_gmbr = os.listdir('images/product')
        self.ids.mygrid.clear_widgets()
        # for ima in imagelistmy:
        #     myimage = SmartTileWithLabel(size_hint_y=None, height= "240dp",source=f"images/product/{source_gmbr[imagelistmy.index(ima)]}"\
        #     ,text= f"[size=20]{ima}[/size]\n[size=14]{imagelistmy2[imagelistmy.index(ima)]}[/size]")
        #     self.ids.mygrid.remove_widget(myimage)


    def on_enter(self):
        # Buttons = ["sdf","sadfsdaf","asdfsda"]
        # for text in Buttons:
        #     button = MDRaisedButton(text="text",id=)
        #     self.mygrid.add_widget(button)
        # import pdb
        # pdb.set_trace()

        # Memperlihatkan list gambar dari produk
        # Tulisan dengan Ukuran besar diatas
        imagelistmy = ["Sunsilk","Kapal Api","Minyak Goreng","Sunsilk","Kapal Api","Minyak Goreng"]
        # Tulisan dengan Ukuran dibawahnya
        imagelistmy2 =  ["Kemasan Kecil","Sachet Kecil","1 Liter","Kemasan Kecil","Sachet Kecil","1 Liter"]
        # source gambar
        # source_gmbr = os.listdir(os.getcwd()+'/images/product')

        source_gmbr = os.listdir('images/product')
        print(source_gmbr)
        # Disini harus ada database untuk panggil gambar
        # source_gmbr = ["cat.jpg","cat2.jpg","cat3.jpg"]

        for ima in imagelistmy:
            # self.mywidget = MyWidget()
            box = MDBoxLayout()
            box.orientation='vertical'
            box.adaptive_height=True
            # button=MDRaisedButton(text="mybutton",size_hint=(1,.3))
            myimage = SmartTileWithLabel()
            myimage.size_hint_y=None
            myimage.height= "240dp"
            myimage.source=f"images/product/{source_gmbr[imagelistmy.index(ima)]}"
            myimage.text = f"[size=20]{ima}[/size]\n[size=14]{imagelistmy2[imagelistmy.index(ima)]}[/size]"
            myimage.bind(on_press=self.pressed)
            box.add_widget(myimage)
            # box.add_widget(self.mywidget)
            self.ids.mygrid.add_widget(box)


        print(myimage)        
        # Buttons = ["sdf","sadfsdaf","asdfsda"]
        # for text in Buttons:
        #     button = MDRaisedButton(text=text,size_hint=(1,None))
        #     # self.button.id = text
        #     button.bind(on_press=self.pressed)
        #     self.ids.mygrid.add_widget(button)
        print('this is online when start')
    def change_quantity(self,t):
        print("nambah")
        pass

    def pressed(self,t):
        print(t.text)
        x = t.text.find("[size=20]")
        y = t.text.find("[/size]")
        x1 = t.text.find("[size=14]")
        y1 = t.text.rfind("[/size]")
        self.baca_item = t.text[9:y]
        self.baca_keterangan_item = t.text[x1+9:y1]
        print(self.baca_item)
        print(self.baca_keterangan_item)
        self.ids.screenmanagerproduct.current='itemcardproduct'
        # import pdb
        # pdb.set_trace()
        pass

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



    def selectitem(self,t,*args,**kwds):
        print('item selected')
        print(t.text)

 

class ItemCardShow(MDScreen):
    pass