import sys
from PyQt5 import QtWidgets, uic

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi('trifecta.ui')
    window.show()
    app.exec()
