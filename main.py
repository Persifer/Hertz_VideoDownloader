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
# 3) Riconoscimento di path e link tramite regex
# 4) Output dell'errore quando non si riesce a scaricare il video
# 5) Disabilitazione/abilitazione bottone download quando è tutto okay | attivazione download dopo aver processato il
#       video


# ^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$