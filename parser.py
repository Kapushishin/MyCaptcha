import requests
from bs4 import BeautifulSoup

CaptchaSet = ['молоко', 'кефир']
search_url = 'https://www.google.ru/search?q='+CaptchaSet[0]+'&newwindow=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwif5e2RjOrxAhWHz4sKHeytBUEQ_AUoAXoECAIQAw&biw=1920&bih=964'
def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text

def get_img(html):
    soup = BeautifulSoup(html, 'lxml')
    img = soup.find('div', id='section-content').find_all('img', class_="t0fcAb")
    imgs = []
    for i in img:
        imgs.append(i.string)
    return imgs

print(get_img(get_html(search_url)))
