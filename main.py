from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from GoogleParser import Parser
import random
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '400')
from kivy.lang import Builder
Builder.load_file('WinForm.kv')
from kivy.core.window import Window
Window.clearcolor = (.92, .92, .96, 1)

class MyCaptcha(GridLayout):
    def random_link(self):
        img_links = Parser('Котик', 'Кефир')
        imgs = img_links.find_false_links() + [img_links.find_true_links()]
        self.true_link = img_links.find_true_links()
        link = imgs[random.randint(0,3)]
        imgs.remove(link)
        return link

    def click_holder(self):
        pass

    def press_button_attempt(self):
        if self.image1.source == self.true_link:
            return print('123')

    def press_button_reset(self):
        pass

class MyApp(App):
    def build(self):
        return MyCaptcha()

if __name__ == '__main__':
    MyApp().run()