from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

class HealifyApp(App):
    def build(self):
        return ContentView()

class ContentView(BoxLayout):
    def __init__(self, **kwargs):
        super(ContentView, self).__init__(**kwargs)
        # Add your content here, similar to the SwiftUI ContentView

if __name__ == '__main__':
    HealifyApp().run()
