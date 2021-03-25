from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import inputWidgetHandler
import sys

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win = inputWidgetHandler.InputWidget()
    win.show()
    sys.exit(app.exec_())

