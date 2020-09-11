from kivy.lang import Builder

from kivymd.app import MDApp


KV ='''
ScrollView:

    MDList:

        OneLineAvatarIconListItem:
            on_release: print("Click!")

            IconLeftWidget:
                icon: "github"

        OneLineAvatarIconListItem:
            on_release: print("Click 2!")

            IconLeftWidget:
                icon: "gitlab"
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()