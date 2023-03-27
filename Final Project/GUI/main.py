import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Main import Ui_Main

class Main(qtw.QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Main()    
    window.show()
    sys.exit(app.exec())