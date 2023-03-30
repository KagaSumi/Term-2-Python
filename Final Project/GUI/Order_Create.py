import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Order_Create import Ui_Create_Order_Form
from Alert import Alert
URL = "http://127.0.0.1:5000/api/"

class Order_Create_Form(qtw.QWidget, Ui_Create_Order_Form):
    finished = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_product = None
        self.selected_cart = None
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_ok)
        self.pb_remove.clicked.connect(self.process_remove)
        self.p_add.clicked.connect(lambda: self.process_add(self.selected_product,self.sb_quantity.value()))
        self.output = {
            "name": None,
            "address": None,
            "products": []
        }
        self.fetch_product_table()
        
    def update_cart(self):
        content = self.output["products"]
        table = self.tv_orderproducts
        if content != []:
            model = qtg.QStandardItemModel()
            model.setColumnCount(2)
            model.setHorizontalHeaderLabels(['Name', 'Quantity'])
            for row_num, row_data in enumerate(content):
                name = qtg.QStandardItem(row_data['name'].title())
                quantity = qtg.QStandardItem(str(row_data['quantity']))
                model.setItem(row_num, 0, name)
                model.setItem(row_num, 1, quantity)

            table.setModel(model)
            table.selectionModel().selectionChanged.connect(self.cart_changed)
            table.setSelectionBehavior(qtw.QTableView.SelectRows)
            table.resizeColumnsToContents()
            table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
            table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        else:
            table.setModel(None)
            
    
    def fetch_product_table(self):
        # Goal of this function is to update the product_table in case there are new values.
        # This function should also check if the show out of stock boolean is set and adjust accordingly
        # This shouldn't have any dependencies on any other function to run
        get_url = URL + "/product"
        response = requests.get(get_url)
        content = json.loads(response.text)
        table = self.tv_product
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
        
    def cart_changed(self,selected):
        try:
            row = selected.indexes()[0].row()
            self.selected_cart = self.tv_orderproducts.model().index(row, 0).data().lower()
            self.p_add.setDisabled(True)
            self.pb_remove.setEnabled(True)
        except IndexError:
            self.selected_product = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)
            
    def product_changed(self,selected):
        try:
            row = selected.indexes()[0].row()
            self.selected_product = self.tv_product.model().index(row, 0).data().lower()
            self.p_add.setEnabled(True)
            self.pb_remove.setDisabled(True)
        except IndexError:
            self.selected_product = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)
            
    def product_changed_cart(self,selected):
        try:
            row = selected.indexes()[0].row()
            self.selected_cart = self.tv_product.model().index(row, 0).data().lower()
            self.p_add.setEnabled(True)
            self.pb_remove.setEnabled(True)
        except IndexError:
            self.selected_cart = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)
            
        
    def raise_alert(self,message):
        self.alert = Alert(message)
        self.alert.show()
        

    @qtc.Slot()
    def process_ok(self):
        #Take all the information from the form and send it through a request.
        if self.le_name.text():
            self.output["name"] = self.le_name.text()
            self.output["address"] = self.le_address.text()
            requests.post(f"{URL}/order", json=self.output)
            self.finished.emit()
            self.close()
        else:
            self.raise_alert("Please enter a Name")

    @qtc.Slot()
    def process_add(self,product ,quantity):
        is_in_cart = False
        for cart_product in self.output["products"]:
            if cart_product["name"] == product:
                is_in_cart = True
        if not is_in_cart:
            self.output["products"].append({"name": product.lower(),"quantity": quantity})
        else:
            for cart_product in self.output["products"]:
                if cart_product["name"] == product:
                    cart_product["quantity"] = quantity
        self.update_cart()

    @qtc.Slot()
    def process_remove(self):
        self.output["products"] = [product for product in self.output["products"] if product["name"] != self.selected_cart]
        self.update_cart()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Order_Create_Form()    
    window.show()
    sys.exit(app.exec())