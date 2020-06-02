import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name"))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="E-Mail: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=22)
        self.submit.bind(on_press=self.sub)
        self.add_widget(self.submit)

    def sub(self, instance):
        fn = self.name.text
        ln = self.lname.text
        em = self.email.text

        print("First Name: ",fn,"\nLast Name: ",ln,"\nE-mail: ",em)
        f = open("Detail.txt",'w')
        f.write(fn)
        f.write("\n")
        f.write(ln)
        f.write("\n")
        f.write(em)
        f.write("\n")
        f.close()
        self.name.text =""
        self.lname.text = ""
        self.email.text = ""


class Form(App):
    def build(self):
        return MyGrid()


if __name__=="__main__":
    Form().run()