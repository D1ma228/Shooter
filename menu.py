from PyQt6.QtWidgets import *

from Shooter import start_game
from store import store_window

app = QApplication([])


window = QWidget()
window.resize(500,500)

start_button = QPushButton("Start")
shop_button = QPushButton("Store")


main_line = QVBoxLayout()
main_line.addWidget(start_button)
main_line.addWidget(shop_button)

start_button.clicked.connect(start_game)
shop_button.clicked.connect(store_window)
window.setLayout(main_line)
window.show()
app.exec()