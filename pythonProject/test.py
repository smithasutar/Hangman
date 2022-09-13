# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # width of window
        self.w_width = 500

        # height of window
        self.w_height = 500

        # setting geometry
        self.setGeometry(100, 100, self.w_width, self.w_height)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # speed variable
        self.speed = 15

    # method for components
    def UiComponents(self):

        # creating a label
        self.label = QLabel(self)

        # label width
        self.l_width = 40

        # label height
        self.l_height = 40

        # setting geometry to the label
        self.label.setGeometry(200, 200, self.l_width, self.l_height)

        # setting stylesheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid darkgreen;"
                                 "background : lightgreen;"
                                 "}")

    # override the key press event
    def keyPressEvent(self, event):

        # get the current co-ordinates of the label
        # X Co-ordinate
        x = self.label.x()

        # Y Co-ordinate
        y = self.label.y()

        # if up arrow key is pressed
        if event.key() == Qt.Key_Up:

            # if top position is attained
            if y > 0:
                self.label.move(x, y - self.speed)

        # if down arrow key is pressed
        elif event.key() == Qt.Key_Down:

            # if bottom position is attained
            # for bottom point, bottom co-ordinate will be
            # height of window - height of label
            if y < self.w_height - self.l_height:
                self.label.move(x, y + self.speed)

        # if left arrow key is pressed
        elif event.key() == Qt.Key_Left:

            # if left end position is attained
            if x > 0:
                self.label.move(x - self.speed, y)

        # if down arrow key is pressed
        elif event.key() == Qt.Key_Right:

            # if right end position is attained
            # for right end point, right co-ordinate will be
            # width of window - width of label
            if x < self.w_width - self.l_width:
                self.label.move(x + self.speed, y)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())