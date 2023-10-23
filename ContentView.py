from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import LinearGradient, Rectangle

class ContentView(BoxLayout):
    def __init__(self, **kwargs):
        super(ContentView, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20

        # Create the background gradient
        with self.canvas.before:
            self.background_gradient = LinearGradient(gradient= [(0, 0, 0, 1), (0, 0, 0, 0)],
                                                      angle=0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.rect.source = self.background_gradient

        titleLabel = Label(text="Welcome to EMDR Therapy App", font_size='24sp', bold=True, color=(1, 1, 1, 1))
        titleLabel.shadow_color = (0, 0, 0, 1)
        titleLabel.shadow_x = 2
        titleLabel.shadow_y = 2
        titleLabel.halign = 'center'
        self.add_widget(titleLabel)

        descriptionLabel = Label(text="Brief description of what this app does.", font_size='16sp', color=(1, 1, 1, 1))
        descriptionLabel.shadow_color = (0, 0, 0, 1)
        descriptionLabel.shadow_x = 1
        descriptionLabel.shadow_y = 1
        descriptionLabel.halign = 'center'
        self.add_widget(descriptionLabel)

        beginButton = Button(text="Begin Questionnaire")
        beginButton.background_normal = ''
        with beginButton.canvas.before:
            beginButton.background_gradient = LinearGradient(gradient=[(0, 0, 1, 1), (0, 0, 0.5, 1)], angle=0)
            beginButton.background_rect = Rectangle(size=beginButton.size, pos=beginButton.pos)
            beginButton.background_rect.source = beginButton.background_gradient

        beginButton.color = (0, 0, 1, 1)
        beginButton.size_hint = (None, None)
        beginButton.size = (200, 50)
        beginButton.bind(on_release=self.navigate_questionnaire)
        self.add_widget(beginButton)

    def navigate_questionnaire(self, instance):
        # Add your navigation logic here

class MainApp(App):
    def build(self):
        return ContentView()

if __name__ == '__main__':
    MainApp().run()
