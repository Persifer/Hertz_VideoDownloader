import os
import time

from PyQt5 import QtWidgets, Qt, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from videoDownloadHandlers.videoDownloadHandler import StreamsVideo, getYouTubeRef, downloadVideoByUrl
import beepy

class InputWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.path = ""
        self.url = ""
        self.res = ""
        self.audio = False
        self.init_ui()

    def init_ui(self):
        #crea una textbox in cui poter inserire del testo

        grid_combo = self.setResComboBox()
        h_box_path = self.setPathLineEdit()
        h_box_url = self.setUrlLineEdit()
        h_box_button = self.setButtonHBox()
        #h_box_checkBox = self.radio_button()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_path)
        v_box.addLayout(h_box_url)
        v_box.addLayout(grid_combo)
        #v_box.addLayout(h_box_checkBox)
        v_box.addLayout(h_box_button)

        self.setLayout(v_box)

    def radio_button(self):
        grid = QtWidgets.QGridLayout()
        labelRadio = QtWidgets.QLabel("Insert the where the file will be saved")
        self.btnMp4 = QtWidgets.QRadioButton("Mp4")
        self.btnMp3 = QtWidgets.QRadioButton("Mp3")

        self.btnMp4.toggled.connect(self.onRadioChoise)
        self.btnMp3.toggled.connect(self.onRadioChoise)

        grid.addWidget(labelRadio)
        grid.addWidget(self.btnMp4,1,0)
        grid.addWidget(self.btnMp3,1,1)

        return grid

    def onRadioChoise(self):
        selectedRadioBtn = self.sender()
        if selectedRadioBtn.isChecked():
            if selectedRadioBtn.text() == "Mp3":
                self.audio = True

    def setPathLineEdit(self):
        grid_layout = QtWidgets.QGridLayout()
        self.labelPath = QtWidgets.QLabel("Insert the where the file will be saved")
        self.lePath = QtWidgets.QLineEdit()
        self.lePath.setDisabled(True)
        self.pathButton = QtWidgets.QPushButton()
        self.pathButton.setText("Apri")
        self.pathButton.clicked.connect(self.showPathDialog)
        self.pathButton.setGeometry(30, 30, 30, 30)

        grid_layout.addWidget(self.labelPath)
        grid_layout.addWidget(self.lePath, 1, 0)
        grid_layout.addWidget(self.pathButton, 1, 1)


        return grid_layout

    def showPathDialog(self):
        self.lePath.setDisabled(False)
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        self.lePath.setText(str(dlg.getExistingDirectory()))


    def setUrlLineEdit(self):
        grid_layout = QtWidgets.QGridLayout()
        self.labelUrl = QtWidgets.QLabel("Insert the video url")
        self.leUrl = QtWidgets.QLineEdit()

        self.leUrl.textEdited.connect(self.showResolution)

        grid_layout.addWidget(self.labelUrl)
        grid_layout.addWidget(self.leUrl)

        return grid_layout

    def setButtonHBox(self):
        h_box_button = QtWidgets.QHBoxLayout()
        self.bClear = QtWidgets.QPushButton("Download")

        self.bClear.clicked.connect(self.downloadVideo)

        h_box_button.addWidget(self.bClear)

        return h_box_button

    def setResComboBox(self):
        gridBox = QtWidgets.QGridLayout()
        self.resLabel = QtWidgets.QLabel()
        self.resComboBox = QtWidgets.QComboBox()

        self.resLabel.setHidden(True)
        self.resComboBox.setHidden(True)

        gridBox.addWidget(self.resLabel)
        gridBox.addWidget(self.resComboBox)

        return gridBox

    def showResolution(self):
        url = self.leUrl.text()
        url.replace(" ", "")
        url = getYouTubeRef(url)
        stream = StreamsVideo(url.streams)
        stream.append("Audio - Mp3")


        self.resLabel.setHidden(False)
        self.resLabel.setText("Inserisci la risoluzione desiderata")

        self.resComboBox.setHidden(False)
        for res in stream:
            self.resComboBox.addItem(res)

    def succes_box(self):
        #beepy.beep(sound=4)
        QtWidgets.QMessageBox.information(self, 'Download', 'Ho finito di scaricare il video.'+
                                               '\nPuoi trovare il file in: '+os.getcwd(),
                                     QtWidgets.QMessageBox.Ok)

    def error_box(self, text):
        #beepy.beep(sound=4)
        QtWidgets.QMessageBox.critical(self, 'Errore!', 'Ops, qualcosa è andato storto...'+
                                               '\n'+text,
                                     QtWidgets.QMessageBox.Ok)

    def downloadVideo(self):
        error = ""
        url = self.leUrl.text()
        if url == "":
            error += "Inserisci un url prima di scaricare qualcosa"
        path = self.lePath.text()
        if path == "":
            error +=  "\nInserisci dove scaricare il file"

        if error == "":
            if self.resComboBox.currentText() == "Audio - Mp3":
                self.audio = True
                res = self.resComboBox.itemText(0)
            else:
                self.audio = False
                res = self.resComboBox.currentText()

            print("Url: " + url)
            print("Path: " + path)
            print("Res: " + res)
            print("Audio: " + str(self.audio))

            if downloadVideoByUrl(url, path, res, self.audio):
                self.succes_box()
            else:
                self.error_box("Non sono riuscito a scaricare il video :(")
        else:
            self.error_box(error)
