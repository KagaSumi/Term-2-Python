import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Main import Ui_Main
from Product_Form import Form
URL = "http://127.0.0.1:5000/api/"

class Main(qtw.QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_product = None
        self.selected_order = None
        self.pb_create.clicked.connect(self.process_form)
        self.pb_update.clicked.connect(lambda: self.process_form(self.selected_product))
        self.pb_delete.clicked.connect(lambda: self.delete_product(self.selected_product))
        self.cb_out_of_stock.clicked.connect(self.fetch_product_table)
        self.fetch_product_table()

            
    def fetch_product_table(self):
        # Goal of this function is to update the product_table in case there are new values.
        # This function should also check if the show out of stock boolean is set and adjust accordingly
        # This shouldn't have any dependencies on any other function to run
        get_url = URL + "/product"
        response = requests.get(get_url)
        content = json.loads(response.text)
        if self.cb_out_of_stock.isChecked():
            content = [item for item in content if item["quantity"] != 0]
        table = self.tv_product_list
        model = qtg.QStandardItemModel()
        model.setColumnCount(3)
        model.setHorizontalHeaderLabels(['Name', 'Price', 'Quantity'])
        for row_num, row_data in enumerate(content):
            name = qtg.QStandardItem(row_data['name'].title())
            price = qtg.QStandardItem(str(row_data['price']))
            quantity = qtg.QStandardItem(str(row_data['quantity']))
            model.setItem(row_num, 0, name)
            model.setItem(row_num, 1, price)
            model.setItem(row_num, 2, quantity)

        table.setModel(model)
        table.selectionModel().selectionChanged.connect(self.product_changed)
        table.setSelectionBehavior(qtw.QTableView.SelectRows)
        table.resizeColumnsToContents()
        table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)

    def product_changed(self,selected):
        try:
            row = selected.indexes()[0].row()
            self.selected_product = self.tv_product_list.model().index(row, 0).data().lower()
            self.pb_delete.setEnabled(True)
            self.pb_update.setEnabled(True)
        except IndexError:
            self.selected_product = None
            self.pb_delete.setDisabled(True)
            self.pb_update.setDisabled(True)

    def fetch_order_table(self):
        pass
    def order_changed(self,selected):
        pass
    
    def fetch_order_product_table(self):
        pass
# ----------------------------------------------------------------
# ----------------- Button Functionality--------------------------
# ----------------------------------------------------------------
    @qtc.Slot()
    def process_form(self, passed = None):
        if passed:
            self.product_form = Form(passed)
        else:
            self.product_form = Form()
        self.product_form.finished.connect(self.fetch_product_table)
        self.product_form.show()

    @qtc.Slot()
    def delete_product(self, product):
        delete_url = URL + "/product/" + product
        requests.delete(delete_url)
        self.selected_product=None
        self. fetch_product_table()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
