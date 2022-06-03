import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('2.1.0')

#

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        #sets a random number as the label's text
        self.randomLabel.text = str(random.randint(0, 1000))

class AppDiProva(App):

    def build(self):
        return MyRoot()

prova = AppDiProva()
prova.run()