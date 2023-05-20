from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

kv = '''
<MDScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        CustomGridLayout:
            id: custom_grid

<CustomGridLayout>:
    cols: 2
    padding: [dp(15), dp(15), dp(15), dp(35)]
    spacing: dp(15)

    MDCard:
        id: on
        md_bg_color: 69/255, 55/255, 86/255, 1
        padding: dp(15)
        spacing: dp(15)
        radius: dp(25)
        ripple_behavior: True
        orientation: 'vertical'

        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                id: card_label
                halign: "center"
                text: 'Turn ON'
                font_style: "H6"

    MDCard:
        id: off
        md_bg_color: 69/255, 55/255, 86/255, 1
        padding: dp(15)
        spacing: dp(15)
        radius: dp(25)
        ripple_behavior: True
        orientation: 'vertical'

        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                halign: "center"
                text: 'Turn OFF'
                font_style: "H6"
'''

class MDScreen(Screen):
    def on_card_press(self, instance):
        card_label = instance.ids.card_label
        card_label.text = "Card Pressed"

class CustomGridLayout(GridLayout):
    def card_pressed(self, instance):
        screen = self.parent.parent  # Access MDScreen instance
        screen.on_card_press(instance)

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    MainApp().run()




