# Вставка парсера
#from GoogleParser import Parser
#img_links = Parser('Молоко','Кефир')
#print(img_links.find_true_links())

# KV кнопкокапча
""""
GridLayout:
    cols: 2
    rows: 2
    padding: 10
    spacing: 2
    Button:
        id: button1
        size_hint: .9, .9
        pos_hint: {'center_x': 0.5}
        on_press: root.verify_image() (image1.color=[0.4,0.4,0.4,1])
        border: (2,2,2,2)
        Image:
            id: image1
            source: imgs[random.randrange(3)]
            center_x: self.parent.center_x
            center_y: self.parent.center_y
            allow_stretch: True
"""

