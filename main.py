from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_file('WinForm.kv')

class MyCaptcha(GridLayout):
    pass

class MyApp(App):
    def build(self):
        return MyCaptcha()


if __name__ == '__main__':
    MyApp().run()