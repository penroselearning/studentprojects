from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage

class FormScreen(GridLayout):

    def submission(self):
        print("Submitted")
        print(self.username.text)
        print(self.password.text)
        print(self.mainbutton.text)

    def __init__(self, **kwargs):
        super(FormScreen, self).__init__(**kwargs)
        self.cols = 2

        self.image = AsyncImage(source='https://www.logolynx.com/images/logolynx/ad/ad0eb0cfc1afa21d427b5bae775fe536.jpeg')
        self.add_widget(self.image)
        self.add_widget(Label(text='Registration Form'))

        # Label and Text Entry
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Label and Password Entry
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        # Label and Dropdown
        self.add_widget(Label(text='Select Option'))
        self.dropdown = DropDown()

        options = ['One', 'Two', 'Three']

        self.mainbutton = Button(text="One")
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release=self.dropdown.open)

        ## Assigns the selected option
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))


        for option in options:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            self.btn = Button(text=option, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            self.btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

            # then add the button inside the dropdown
            self.dropdown.add_widget(self.btn)

        # Submit Button
        self.submitbtn = Button(text="Submit")
        self.add_widget(self.submitbtn)
        self.submitbtn.bind(on_release=lambda x:self.submission())


class MyApp(App):

    def build(self):
        return FormScreen()


if __name__ == '__main__':
    MyApp().run()