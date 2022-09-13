import sys
from random import randrange
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

w: QWidget = QWidget()

# Create a Qt widget, which will be our window.
window: QWidget = QWidget()

window.setFixedSize(1100, 600)
window.setWindowTitle("Hangman")
window.setStyleSheet("background-color:rgb(175,238,238)")
letters = [["a", "b", "c", "d", "e", "f", "g"],
           ["h", "i", "j", "k", "l", "m", "n"],
           ["o", "p", "q", "r", "s", "t", "u"],
           ["v", "w", "x", "y", "z"]]
bad = ["Amateur.", "Lame!", "Yikes...", "Hurry before the stick \nman's gone!"]
random = ["book", "boot", "belt", "pack", "tank", "rink", "easy", "peek", "feet",
          "meow", "seed", "wing", "surf", "said", "guys", "save", "mint", "same"
           "snow", "lord", "lamb", "lazy", "text", "goat", "pole", "reef", "need"]

s_word = random[randrange(26)]
wording = ['_', '_', '_', '_']
count = 0


def find(string, char):
    for u, c in enumerate(string):
        if c == char:
            yield u

def image(win, move_x, move_y, scale_w, scale_h, op, name):
    pic = QLabel(win)
    pic.setPixmap(QPixmap(name).scaled(scale_w, scale_h, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    pic.move(move_x, move_y)

    if op:
        pic.opacity_effect = QGraphicsOpacityEffect()
        pic.opacity_effect.setOpacity(0.85)
        pic.setGraphicsEffect(pic.opacity_effect)
    pic.show()


def text_edits():
    text_edit = QtWidgets.QTextEdit(window)
    text_edit.setPlaceholderText("Guess a letter")
    text_edit.setFontPointSize(20)
    text_edit.resize(150, 40)
    text_edit.setStyleSheet("background-color: white")
    text_edit.move(680, 180)
    return text_edit


def buttons():
    button = QtWidgets.QPushButton(window)
    button.setText("Enter")
    button.move(840, 180)
    button.resize(50, 40)
    button.setStyleSheet("background-color: pink")
    return button


def message(text, typo):
    number = randrange(4)
    if typo:
        say = bad[number] + " Incorrect Entry"
    else:
        say = text + "\nThe word was: " + s_word
    msg = QMessageBox()
    msg.setWindowTitle("Try Again")
    msg.setText(say)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setFont(QFont('Times', 20))
    msg.setStyleSheet("background-color: pink")
    msg.exec_()


def show_t(word, guess):
    x = 450
    var = "letters/" + word + ".png"
    # print("MEOW", guess)
    for p in range(len(guess)):
        for j in range(guess[p] + 1):
            x = x + 100

        image(window, x, 50, 200, 100, False, var)
        x = 450


def show_man(nums):
    number = "% s" % nums
    title = "man/man" + number + ".png"
    x_axis = [0, 80, 115, 120, 320, 270, 315, 260, 332, 260, 332]
    y_axis = [0, 500, 106, 106, 106, 150, 250, 250, 250, 390, 390]
    scale_x = [0, 250, 500, 200, 200, 200, 100, 100, 100, 100, 100]
    scale_y = [0, 400, 400, 500, 50, 100, 150, 60, 60, 60, 60]

    image(window, x_axis[nums], y_axis[nums], scale_x[nums], scale_y[nums], False, title)


image(window, 20, 0, 450, 450, False, "hangman.png")
image(window, 500, 230, 550, 550, False, "alpha.png")
num = 550
for i in range(4):
    image(window, num, 150, 200, 20, False, "line.png")
    num = num + 100
text_edit = text_edits()
button = buttons()


def clicks():
    global count
    x = 500
    y = 240
    exist = False

    word = text_edit.toPlainText()

    turn = 7
    for i in range(4):
        if i == 3:
            turn = 5
        for j in range(turn):

            # the word exists
            if word == letters[i][j]:
                letters[i][j] = "&taken&"
                exist = True

                if i == 3:
                    for k in range(j + 1):
                        x = x + 78
                    y = 492
                if i != 3:
                    for k in range(j):
                        x = x + 78
                    for p in range(i):
                        y = y + 84
                image(window, x, y, 400, 80, True, "box1.jpg")
                guess = list(find(s_word, word))
                if guess:
                    for q in range(len(guess)):
                        wording[guess[q]] = word
                    show_t(word, guess)
                else:
                    count = count + 1
                    show_man(count)

                    if count >= 10:
                        button.setEnabled(False)
                        message("YOU LOST!!!", False)
                        window.close()

    checker = list(find(wording, '_'))

    if not checker:
        button.setEnabled(False)
        message("YOU WON!!!!!!!", False)
        window.close()

    if not exist and button.isEnabled():
        message("", True)


button.clicked.connect(clicks)


def open():
    window.show()
    w.close()


w.setFixedSize(1100, 600)
w.setWindowTitle("Welcome to Hangman")
w.setStyleSheet("background-color:rgb(250,128,114)")

b = QtWidgets.QPushButton(w)
b.setText("Start")
b.setFont(QFont('Comic Sans', 40))
b.move(460, 380)
b.resize(200, 80)
b.setStyleSheet("background-color:rgb(224,255,255)")

image(w, 220, 120, 650, 550, False, "first_w.png")
image(w, 80, 320, 650, 250, False, "men1.png")
image(w, 750, 320, 650, 250, False, "men2.png")
b.clicked.connect(open)

w.show()

# window.show()
app.exec()
