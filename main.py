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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generate_imgs()

    def generate_imgs(self):
        self.theme = self.themes()
        object_of_parser = Parser(self.theme)
        self.true_link = object_of_parser.find_true_links()
        self.imgs = object_of_parser.find_false_links() + [object_of_parser.find_true_links()]
        random.shuffle(self.imgs)
        self.input_images()

    def input_images(self):
        self.image1.source = self.imgs[0]
        self.image2.source = self.imgs[1]
        self.image3.source = self.imgs[2]
        self.image4.source = self.imgs[3]

    def themes(self):
        epic_list_of_themes = [["Молоко", "Кефир"],
                               ["Курица", "Индейка"],
                               ["Кошкодевочка", "Джоджо"],
                               ["Водичка", "Аква"]]
        random.shuffle(epic_list_of_themes)
        return epic_list_of_themes[0]

    def click_holder(self, button):
        self.button1.background_color = [1, 1, 1, 1]
        self.button2.background_color = [1, 1, 1, 1]
        self.button3.background_color = [1, 1, 1, 1]
        self.button4.background_color = [1, 1, 1, 1]
        button.background_color = [.51, .88, .67, 1]
        return button

    def press_button_attempt(self):
        if self.image1.source == self.true_link:
            return print('Дя')
        else:
            return print('Неть')

    def press_button_reset(self):
        pass


class MyApp(App):
    def build(self):
        return MyCaptcha()


if __name__ == '__main__':
    MyApp().run()