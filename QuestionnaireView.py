from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.lang import Builder

class QuestionnaireView(BoxLayout):
    def __init__(self, **kwargs):
        super(QuestionnaireView, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20

        self.answer1 = TextInput(hint_text="Answer to question 1")
        self.answer2 = TextInput(hint_text="Answer to question 2")
        self.navigateToInitialScreening = False

        titleLabel1 = Label(text="Question #1: Have you experienced a traumatic event?", font_size='16sp', color=(0, 0, 0, 1))
        titleLabel2 = Label(text="Question #2: Do you regularly relive or re-experience the event?", font_size='16sp', color=(0, 0, 0, 1))

        nextButton = Button(text="Next")
        nextButton.background_normal = ''
        nextButton.background_color = (0, 0, 1, 1)
        nextButton.color = (1, 1, 1, 1)
        nextButton.size_hint = (None, None)
        nextButton.size = (200, 50)
        nextButton.bind(on_release=self.handle_answer)

        self.add_widget(titleLabel1)
        self.add_widget(self.answer1)
        self.add_widget(titleLabel2)
        self.add_widget(self.answer2)
        self.add_widget(nextButton)

    def handle_answer(self, instance):
        if self.answer1.text.lower() == "no" and self.answer2.text.lower() == "no":
            self.navigateToInitialScreening = False  # Add your navigation logic here

class InitialScreeningView(BoxLayout):
    def __init__(self, **kwargs):
        super(InitialScreeningView, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Initial Screening", font_size='24sp', color=(0, 0, 0, 1)))

class MainApp(App):
    def build(self):
        return QuestionnaireView()

if __name__ == '__main__':
    MainApp().run()
