from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button


class InfoScreen(GridLayout):
    """Take basic input for form."""
    def __init__(self, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
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

    def button1Press(self,btn):
        print ("title: " + self.title.text + "\n" + "and so on")



class formMaker(App):
    """Generate everything and run the application"""
    def build(self):
        self.icon = 'icon.png'
        inf = InfoScreen(padding=[20,20,20,20])
        return inf


if __name__ == '__main__':
    formMaker().run()
