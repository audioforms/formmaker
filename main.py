from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen

# question counters
class QuestionTracker(object):
    def __init__(self):
        self.number = 0
        self.position = 0

    def newq(self):
        self.number = self.number + 1
        self.position = self.number
        return self.number

qtrack = QuestionTracker()

class InfoLayout(GridLayout):
    """Take basic input for form."""
    def __init__(self, **kwargs):
        super(InfoLayout, self).__init__(**kwargs)
        # title input
        self.cols = 2
        self.add_widget(Label(text='Title'))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)
        # owner input
        self.add_widget(Label(text='Owner'))
        self.owner = TextInput(multiline=False)
        self.add_widget(self.owner)
        # behavior -> intro message input
        self.add_widget(Label(text='Intro Message'))
        self.intro = TextInput(multiline=True)
        self.add_widget(self.intro)
        # behavior -> outro message input
        self.add_widget(Label(text='Outro Message'))
        self.outro = TextInput(multiline=True)
        self.add_widget(self.outro)
        # repeat behavior checkbox
        self.add_widget(Label(text='Repeat?'))
        self.repeat = CheckBox()
        self.add_widget(self.repeat)
        # submit button for the section (button 1)
        self.button1 = Button(text='Add Questions')
        self.button1.bind(on_press=self.button1Press)
        self.add_widget(self.button1)
        #change canvas options
        with self.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def button1Press(self,btn):
        print ("--- !" +  self.title.text)
        print ("title: " + self.title.text)
        print ("owner: " + self.owner.text)
        print ("behavior: ")
        print ("    intro-message: " + self.intro.text)
        print ("    outro-message: " + self.outro.text)
        print ("questions: ")
        sm.switch_to(AddQuestionScreen(name='Add Question' +
                                       str(qtrack.newq())))


class AddQuestionLayout(GridLayout):
    """Add a question."""
    def __init__(self, **kwargs):
        super(AddQuestionLayout, self).__init__(**kwargs)
        # question title input
        self.cols = 2
        self.add_widget(Label(text='Title'))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)
        # quesiton type
        self.add_widget(Label(text='Type'))
        self.qtype = TextInput(multiline=False)
        self.add_widget(self.qtype)
        # validation rules (TODO fix this to have select types)
        self.add_widget(Label(text='Validation'))
        self.validation = TextInput(multiline=True)
        self.add_widget(self.validation)
        # add this question
        self.button1 = Button(text='Save and add another')
        self.button1.bind(on_press=self.button1Press)
        self.add_widget(self.button1)
        self.button2 = Button(text='Finish')
        self.button2.bind(on_press=self.button2Press)
        self.add_widget(self.button2)
        #change canvas options
        with self.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def button1Press(self,btn):
        print ("  - title: " + self.title.text )
        print ("    type: " + self.qtype.text )
        if self.validation.text:
            print ("    validation: " + self.validation.text )
        sm.switch_to(AddQuestionScreen(name='Add Question' +
                                       str(qtrack.newq())))

    def button2Press(self,btn):
        print ("\nDONE")

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
        self.add_widget(InfoLayout(padding=[20,20,20,20]))

class AddQuestionScreen(Screen):
    def __init__(self, **kwargs):
        super(AddQuestionScreen, self).__init__(**kwargs)
        self.add_widget(AddQuestionLayout(padding=[20,20,20,20]))

# manage screens
sm = ScreenManager()
sm.add_widget(InfoScreen(name='Intro'))



class formMaker(App):
    """Generate everything and run the application"""
    def build(self):
        self.icon = 'icon.png'
        return sm


if __name__ == '__main__':
    formMaker().run()
