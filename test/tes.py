from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<Test>:
    TabbedPanelHeader
        color: (0,0,1,1)
        text:'blaaaaaaa'
        background_color: (0, 0, 1, 1)
        background_normal: ''
''')
class Test(BoxLayout):pass
runTouchApp(Test())