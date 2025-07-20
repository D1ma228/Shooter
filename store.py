from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

from file_helper import read_file, save_file


def buy_item(price,image):
    data = read_file()
    if data["money"] >=price:
        data["skin"] = image
        data["money"] -= price
    save_file(data)

def store_window():
    window = QDialog()


    elements = [
        {
            "price": 100,
            "image": "normal.png",
        },
        {
            "price": 200,
            "image": "good.png",
        },
        {
            "price": 10,
            "image": "no.png"
        },
    ]
    main_line = QHBoxLayout()
    for element in elements:
        price_lbl = QLabel("Price" + str(element["price"]))
        img_lbl = QLabel()
        image = QPixmap(element["image"])
        image = image.scaledToWidth(100)
        img_lbl.setPixmap(image)
        buy_btn = QPushButton("Buy")
        ver = QVBoxLayout()
        ver.addWidget(price_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(buy_btn)
        buy_btn.clicked.connect(lambda
                                _, img=element["image"], price=element["price"]: buy_item(price, img))
        main_line.addLayout(ver)
    window.setLayout(main_line)
    window.show()
    window.exec()