from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from MenuBarHandler import CompleteGui
import sys

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win = CompleteGui()
    win.show()
    sys.exit(app.exec_())

