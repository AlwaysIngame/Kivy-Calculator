import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.write()


class CalcGridLayout(GridLayout):

    done = False

    def calculate(self, calculation):
        try:
            self.display.text = str(eval(calculation))
        except:
            self.display.text = "Error"
        else:
            self.display.text = str(eval(calculation))
        self.done = True

    def ask_done(dt):
        if dt.done == True:
            dt.display.text = ""
            dt.done = False

    def ask_empty(self):
        if self.display.text == "0":
            self.display.text = ""

    def backspace(self):
        self.display.text = self.display.text[:-1]
        self.done = False


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
