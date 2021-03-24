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

        h_box_path = self.setPathLineEdit()
        h_box_url = self.setUrlLineEdit()
        h_box_button = self.setButtonHBox()
        h_box_checkBox = self.setCheckBoxHbox()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_path)
        v_box.addLayout(h_box_url)
        v_box.addLayout(h_box_checkBox)
        v_box.addLayout(h_box_button)


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
            #pulisce l'input della casella di testo
            self.le.clear()

    def setPathLineEdit(self):
        grid_layout = QtWidgets.QGridLayout()
        self.labelPath = QtWidgets.QLabel("Insert the where the file will be saved")
        self.lePath = QtWidgets.QLineEdit()

        grid_layout.addWidget(self.labelPath)
        grid_layout.addWidget(self.lePath)

        return grid_layout

    def setUrlLineEdit(self):
        grid_layout = QtWidgets.QGridLayout()
        self.labelUrl = QtWidgets.QLabel("Insert the video url")
        self.leUrl = QtWidgets.QLineEdit()

        grid_layout.addWidget(self.labelUrl)
        grid_layout.addWidget(self.leUrl)

        return grid_layout

    def setButtonHBox(self):
        h_box_button = QtWidgets.QHBoxLayout()
        self.bClear = QtWidgets.QPushButton("Clear")
        self.bPrint = QtWidgets.QPushButton("Print")
        h_box_button.addWidget(self.bPrint)
        h_box_button.addWidget(self.bClear)

        return h_box_button

    def setCheckBoxHbox(self):
        h_box_checkBox = QtWidgets.QHBoxLayout()
        self.labelCheck = QtWidgets.QLabel("What type of format you want to download?")
        self.mp4CeckBox = QtWidgets.QCheckBox("Mp4")
        self.mp3CeckBox = QtWidgets.QCheckBox("Mp3")
        h_box_checkBox.addWidget(self.labelCheck)
        h_box_checkBox.addWidget(self.mp3CeckBox)
        h_box_checkBox.addWidget(self.mp4CeckBox)

        return h_box_checkBox

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win= windowHandler()
    win.show()
    sys.exit(app.exec_())

