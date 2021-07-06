import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3

        self.inside = GridLayout()
        self.inside.cols = 2

        # name
        self.name = Label(text='name')
        self.inside.add_widget(self.name)
        self.user_name = TextInput(multiline=False)
        self.inside.add_widget(self.user_name)
        # pass
        self.inside.add_widget(Label(text="Password: "))
        self.user_pass = TextInput(multiline=False)
        self.inside.add_widget(self.user_pass)

        self.add_widget(self.inside)

        # button
        self.button = Button(text="Submit", font_size=40)
        self.button.bind(on_press=self.pressed)
        self.add_widget(self.button)

    def pressed(self, instance):
        print(self.user_name)
        print(type(self.user_name))

        print(self.user_name.text)
        print(type(self.user_name.text))

        self.name.text += '\na'
        print(self.name.text)
        self.add_widget(Label(text=self.user_name.text))
        self.user_name.text = ""

        print('Pressed')


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()