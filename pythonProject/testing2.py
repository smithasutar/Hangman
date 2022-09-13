import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 320, 200)
        self.setWindowTitle("PyQT show image")
        self.show()

        self.im = QPixmap("./alpha.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)


App = QApplication(sys.argv)
ex = Example()

sys.exit(App.exec())
