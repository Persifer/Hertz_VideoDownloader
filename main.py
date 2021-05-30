from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from MenuBarHandler import CompleteGui
import sys

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    win = CompleteGui()
    win.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main_window()

#TODO
# 1) Trasformare il videodownloader da funzioni a classi
# 2) Aggiungere la gestione delle playlist