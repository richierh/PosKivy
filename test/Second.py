from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Label2(BoxLayout):
    pass

    def change(self):
        print("okay you are done")


if __name__=="__main__":
    Label2().run()