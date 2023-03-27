import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Order_Create import Ui_Create_Order_Form

class Form(qtw.QWidget, Ui_Create_Order_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_ok)

    @qtc.Slot()
    def process_ok(self):
        if True:
            self.login_success.emit()
            self.close()
        else:
            self.le_message.setText("Error:")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Form()    
    window.show()
    sys.exit(app.exec())