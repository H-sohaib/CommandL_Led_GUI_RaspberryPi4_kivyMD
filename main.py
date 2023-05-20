from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.lang import Builder
#  480*320
#            width  height
Window.size = (480, 320)


class CustomCard(MDCard):
    def toggle_light(self):
        print("Led Turned On")
    def turn_off(self):
        print("Led Turned Off")

class MainApp(MDApp):
    def card_pressed(self , on) :
        print("presssed")
    def build(self):
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('./design.kv')
    

MainApp().run()
