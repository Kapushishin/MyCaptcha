import requests
from bs4 import BeautifulSoup


class Parser():
    def __init__(self, false_tag, true_tag):
        self.false_tag = false_tag
        self.true_tag = true_tag

    def find_false_links(self):
        search_link = "https://www.google.ru/search?q="+self.false_tag+"&newwindow=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiE-8D2wOzxAhUql4sKHZTDDisQ_AUoAXoECAIQAw&biw=1920&bih=964"
        response = requests.get(search_link)
        soup = BeautifulSoup(response.content, "html.parser")
        img_elements = soup.find_all('img', class_="t0fcAb")
        imgs = [element.get('src') for element in img_elements]
        return [img for img in imgs if imgs.index(img) < 3]

    def find_true_links(self):
        search_link = "https://www.google.ru/search?q="+self.true_tag+"&newwindow=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiE-8D2wOzxAhUql4sKHZTDDisQ_AUoAXoECAIQAw&biw=1920&bih=964"
        response = requests.get(search_link)
        soup = BeautifulSoup(response.content, "html.parser")
        img_elements = soup.find_all('img', class_="t0fcAb")
        return [element.get('src') for element in img_elements][0]

