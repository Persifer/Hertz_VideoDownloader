from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from MenuBarHandler import CompleteGui
import sys

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win = CompleteGui()
    win.show()
    sys.exit(app.exec_())

    # TODO:
    #   1) Trovare il modo di fare comunicare front-end e back-end
    #   2) Iniziare a fare in modo di poter scaricare il file
    #   3) Fare in modo di poter scegliere la cartella

