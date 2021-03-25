from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from inputWidgetHandler import InputWidget
import sys


class CompleteGui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.widget = InputWidget()
        self.setCentralWidget(self.widget)

        self.init_ui()

    def init_ui(self):

        self.PrintMenuBar()

        self.setWindowTitle("Hert VideoDonwloader")

    def PrintMenuBar(self):
        menu_bar = self.menuBar()
        menuOption = menu_bar.addMenu("File")

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        
        menuOption.addAction(exitAction)
