import win32com.client

import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.cols = 2
        self.rows = 2
        self.btnQuiero = Button(text='Yo quiero')
        self.btnQuiero.bind(on_press=self.callback)
        self.btnNo = Button(text='Yo no quiero')
        self.btnNo.bind(on_press=self.callback)
        self.btnComer = Button(text='Comer')
        self.btnComer.bind(on_press=self.callback)
        self.btnBaniarme = Button(text='Bañarme')
        self.btnBaniarme.bind(on_press = self.callback)
        self.add_widget(self.btnQuiero)
        self.add_widget(self.btnNo)
        self.add_widget(self.btnComer)
        self.add_widget(self.btnBaniarme)

    def callback(self, args):
        #help(args)
        self.speaker.Speak(args.text)
class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()