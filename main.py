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
        self.result=[]
        self.position = 0


    def newq(self):
        """add a new question."""
        self.position = self.position + 1
        return self.position

    def prev(self):
        """detemrine logic to go back to previous screen."""
        if (self.position <= 1):
            self.position = self.position - 1
            return 'Intro' # for back to main menu
        else:
            self.position = self.position - 1
            return 'Add Question' + str(self.position) # go to prev question

    def next(self):
        """detemrine logic to go back to next screen."""
        if (self.position==len(self.result)):
            self.newq()
        else:
            self.position = self.position + 1
        return 'Add Question' + str(self.position) # go to next question

    def newest(self):
        """quick check if newest for screen management."""
        return (self.position==len(self.result))

    def res_add(self, instr):
        """ find place for and add result to total"""
        if len(self.result) <= self.position:
            self.result.append(instr)
        else:
            self.result[self.position] = instr

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
        self.nextBtn = Button(text='Next')
        self.nextBtn.bind(on_press=self.nextBtnPress)
        self.add_widget(self.nextBtn)
        #change canvas options
        with self.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def nextBtnPress(self,btn):
        introstr = "--- !" +  self.title.text
        introstr = introstr + "title: " + self.title.text + "\n"
        introstr = introstr + ("owner: " + self.owner.text) + "\n"
        introstr = introstr + ("behavior: ") + "\n"
        introstr = introstr + ("    intro-message: " + self.intro.text) + "\n"
        introstr = introstr + ("    outro-message: " + self.outro.text) + "\n"
        introstr = introstr + ("questions: ") + "\n"
        qtrack.res_add(introstr)
        destination = qtrack.next()
        if qtrack.newest():
            sm.add_widget(AddQuestionScreen(name=destination))
        sm.current = destination


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
        self.nextBtn = Button(text='Next (add/edit next question)')
        self.nextBtn.bind(on_press=self.nextBtnPress)
        self.add_widget(self.nextBtn)
        self.backBtn = Button(text='Back')
        self.backBtn.bind(on_press=self.backBtnPress)
        self.add_widget(self.backBtn)
        self.finBtn = Button(text='Finish')
        self.finBtn.bind(on_press=self.finBtnPress)
        self.add_widget(self.finBtn)
        #change canvas options
        with self.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def nextBtnPress(self,btn):
        qstr = ("  - title: " + self.title.text ) + "\n"
        qstr = qstr + ("    type: " + self.qtype.text ) + "\n"
        if self.validation.text:
            qstr = qstr + ("    validation: " + self.validation.text ) + "\n"
        qtrack.res_add(qstr)
        destination = qtrack.next()
        if qtrack.newest():
            sm.add_widget(AddQuestionScreen(name=destination))
        sm.current = destination

    def finBtnPress(self,btn):
        qstr = ("  - title: " + self.title.text ) + "\n"
        qstr = qstr + ("    type: " + self.qtype.text ) + "\n"
        if self.validation.text:
            qstr = qstr + ("    validation: " + self.validation.text ) + "\n"
        qtrack.res_add(qstr)

        print ("\nDONE")
        print ("".join(qtrack.result))

    def backBtnPress(self,btn):
        qstr = ("  - title: " + self.title.text )
        qstr = qstr + ("    type: " + self.qtype.text )
        if self.validation.text:
            qstr = qstr + ("    validation: " + self.validation.text )
        qtrack.res_add(qstr)
        sm.current = qtrack.prev()
        pass


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
