from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main_window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #give at win the meausere of the windows
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("HeartzVideoDownloader")

    # beautify the gui with some stuff
    label = QtWidgets.QLabel(win) #creation of a label (some random text)
    label.setText("Ehi, i'm still alive")
    label.move(200, 250)
    #hi
    # permette di visualizzare la finestra
    win.show()
    sys.exit(app.exec_())

