from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# def main_window():
#
#     app = QApplication(sys.argv)
#     win = QtWidgets.QWidget()
#     #give at win the meausere of the windows
#
#     label = QtWidgets.QLabel("Ehi, i'm still alive") # creation of a label (some random text)
#     button = QtWidgets.QPushButton("Download")
#
#     v_box = QtWidgets.QVBoxLayout()
#     v_box.addWidget(button)
#     v_box.addWidget(label)
#
#     win.setLayout(v_box)
#
#     win.setWindowTitle("Hertz VideoDownloader")
#     win.show()
#     sys.exit(app.exec_()) #esce dalla finestra quando premi x

class windowHandler(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        #crea una textbox in cui poter inserire del testo
        self.le = QtWidgets.QLineEdit()
        self.bClear = QtWidgets.QPushButton("Clear")
        self.bPrint = QtWidgets.QPushButton("Print")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.bClear)
        v_box.addWidget(self.bPrint)

        self.setLayout(v_box)

        #richiama la funzione che si occupa di gestire le azioni che si dovranno svolgere quando si preme il pulsante
        self.bClear.clicked.connect(self.btn_click)
        self.bPrint.clicked.connect(self.btn_click)

        self.setWindowTitle("Hert VideoDonwloader")
        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == "Print":
            print(self.le.text())
        else:
            self.le.clear()


def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win= windowHandler()
    win.show()
    sys.exit(app.exec_())
