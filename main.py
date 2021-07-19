from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '400')
from kivy.lang import Builder
Builder.load_file('WinForm.kv')
from kivy.core.window import Window
Window.clearcolor = (.92, .92, .96, 1)

class MyCaptcha(GridLayout):
    def press_button_attempt(self):
        pass

    def press_button_reset(self):
        pass

class MyApp(App):
    def build(self):
        return MyCaptcha()

if __name__ == '__main__':
    MyApp().run()