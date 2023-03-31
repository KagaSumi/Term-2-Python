import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Main import Ui_Main
from Product_Form import Form
from Order_Create import Order_Create_Form
from Order_Edit import Order_Edit_Form
URL = "http://127.0.0.1:5000/api/"

class Main(qtw.QMainWindow, Ui_Main):
    """This is defining our main application that will tie all the other ui elements together.
    It has functions to populate all information and handle the logic for any restrictions for the UI I had.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Initalizing variables
        self.selected_product = None
        self.order_list = json.loads(requests.get(URL + "/order").text)
        self.selected_order_id = None
        self.selected_order_products = None
        self.order_process_sort = None

        #Tie function calls to button clicked or clicked functionality
        self.pb_create.clicked.connect(self.process_form)
        self.pb_update.clicked.connect(self.process_form)
        self.pb_delete.clicked.connect(self.process_delete_product)
        self.pb_order_create.clicked.connect(self.process_create_order)
        self.cb_out_of_stock.clicked.connect(self.fetch_product_table)
        self.pb_order_delete.clicked.connect(self.process_delete_order)
        self.pb_order_process.clicked.connect(self.process_process_order)
        self.pb_order_update.clicked.connect(self.process_update_order)
        self.rb_order_no_filter.clicked.connect(self.order_no_filter)
        self.rb_order_unprocessed.clicked.connect(self.order_unprocessed_filter)
        self.rb_order_processed.clicked.connect(self.order_processed_filter)
        self.le_order_filter.textChanged.connect(self.update_order_table)

        #Run Fetch Tables to populate on launch
        self.fetch_product_table()
        self.fetch_order_table()

    def fetch_product_table(self) -> None:
        """This function will fetch the list of products from my API
        Then populate the Product Table with the list, and make sure that selection is by row and add function call on selecting a product.
        
        Will only populate the product table with quantity = 0 if checkbox out_of_stock is checked.
        """
        response = requests.get(URL + "/product")
        content = json.loads(response.text)
        if self.cb_out_of_stock.isChecked():
            content = [item for item in content if item["quantity"] == 0]
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

    def product_changed(self,selected:qtc.QItemSelection):
        """This function is called when there is a selection change in product table.
        This will change the local vairable to update to the name of product selected.
        If there is a selected product it will update the button states so that user can select
        Update and Delete
        
        Otherwise it will Disable those buttons.

        Args:
            selected (QItemSelection): This is the row we selected from the table. 
        """        
        try:
            row = selected.indexes()[0].row()
            self.selected_product = self.tv_product_list.model().index(row, 0).data().lower()
            self.pb_delete.setEnabled(True)
            self.pb_update.setEnabled(True)
        except IndexError:
            self.selected_product = None
            self.pb_delete.setDisabled(True)
            self.pb_update.setDisabled(True)

    def fetch_order_table(self) -> None:
        """Much Like fetch_product_Table this will populate our order table filling it out.
        However it has more filter options that modify the order table by the different sorting features. 
        It will redraw the entire order table to ensure it is completely updated after any changes.
        """
        content = self.order_list
        table = self.tv_order_view
        if self.order_process_sort == True:
            content = sorted([order for order in content if order["completed"]], key=lambda x: (x["time_processed"], x["time_created"]))
        elif self.order_process_sort == False:
            content = sorted([order for order in content if not order["completed"]], key=lambda x: x["time_created"])
        if self.le_order_filter.text():
            content = [order for order in content if self.le_order_filter.text().lower() in order["customer_name"].lower()]

        model = qtg.QStandardItemModel()
        model.setColumnCount(5)
        model.setHorizontalHeaderLabels(['Order_ID', 'Name', 'Address','Time Created', 'Time Processed'])
        for row_num, row_data in enumerate(content):
            order_id = qtg.QStandardItem(str(row_data['id']))
            name = qtg.QStandardItem(row_data['customer_name'].title())
            address = qtg.QStandardItem(row_data['customer_address'].title())
            time_create = qtg.QStandardItem(row_data['time_created'])
            time_process = qtg.QStandardItem(row_data['time_processed'])

            model.setItem(row_num, 0, order_id)
            model.setItem(row_num, 1, name)
            model.setItem(row_num, 2, address)
            model.setItem(row_num, 3, time_create)
            model.setItem(row_num, 4, time_process)

        table.setModel(model)
        table.selectionModel().selectionChanged.connect(self.order_changed)
        table.setSelectionBehavior(qtw.QTableView.SelectRows)
        table.resizeColumnsToContents()
        table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)

    def order_changed(self,selected:qtc.QItemSelection) -> None:
        """This function is called when the order selected has changed.
        This function handles enabling and disabling the buttons on the order section.
        This will also update our stored order id to for our other button to use.
        
        If an order is selected it will call the fetch_order_product_table function
        which populates the adjacent table view with the items in the order selected.

        Args:
            selected (QItemSelection): Selected row for the order selected
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_order_id = int(self.tv_order_view.model().index(row, 0).data())
            self.pb_order_delete.setEnabled(True)
            self.pb_order_update.setEnabled(True)
            self.pb_order_process.setEnabled(True)
            self.fetch_order_product_table()
        except IndexError:
            self.selected_order_products = None
            self.selected_order_id = None
            self.pb_order_delete.setDisabled(True)
            self.pb_order_update.setDisabled(True)
            self.pb_order_process.setDisabled(True)
            self.tv_order_items.setModel(None)

    def fetch_order_product_table(self) -> None:
        """This will fetch all the products for the selected order.
        """        
        for order in self.order_list:
            if order["id"] == self.selected_order_id:
                table = self.tv_order_items
                model = qtg.QStandardItemModel()
                model.setColumnCount(2)
                model.setHorizontalHeaderLabels(['Name','Quantity'])
                for row_num, row_data in enumerate(order["products"]):
                    name = qtg.QStandardItem(row_data['name'].title())
                    quantity = qtg.QStandardItem(str(row_data['quantity']))
                    model.setItem(row_num, 0, name)
                    model.setItem(row_num,1, quantity)
                table.setModel(model)
                table.resizeColumnsToContents()

    def update_order_table(self) -> None:
        """This Function is just a wrapper to update my stored value before I run the update function
        """
        self.order_list = json.loads(requests.get(URL + "/order").text)
        self.fetch_order_table()

# ----------------------------------------------------------------
# ----------------- Button Functionality--------------------------
# ----------------------------------------------------------------
    @qtc.Slot()
    def process_form(self) -> None:
        """
        Opens a form for creating or editing a product and connects its finished signal to the fetch_product_table method.
        
        If product_name is None then it is assumed that we are creating a new product
        If product_name is not None then it is assumed that passed is a name of the product
        Args:
            product_name (str or None): The name of the product to edit, or None to create a new product.
        
        Returns:
            None
        """
        if self.selected_product:
            self.product_form = Form(self.selected_product)
        else:
            self.product_form = Form()
        self.product_form.finished.connect(self.fetch_product_table)
        self.product_form.show()

    @qtc.Slot()
    def process_delete_product(self) -> None:
        """
        Deletes a product from the database by sending a DELETE request to the API.
        
        Args:
            product_name (str): The name of the product to be deleted.
        
        Returns:
            None
        """
        delete_url = URL + "/product/" + self.selected_product
        requests.delete(delete_url)
        self.selected_product=None
        self.fetch_product_table()

    @qtc.Slot()
    def process_create_order(self) -> None:
        """
        Opens a new order creation form and connects its finished signal to the update_order_table method.
        
        Returns:
            None
        """
        self.Order_Create_Form = Order_Create_Form()
        self.Order_Create_Form.finished.connect(self.update_order_table)
        self.Order_Create_Form.show()

    @qtc.Slot()
    def process_delete_order(self) -> None:
        """
    Deletes the selected order from the database by sending a DELETE request to the API.
    Disables the delete, process, and update buttons, updates the order table, and clears the item list.
    
    Returns:
        None
        """
        requests.delete(URL + "/order/" + str(self.selected_order_id))
        self.selected_product=None
        self.pb_order_delete.setDisabled(True)
        self.pb_order_process.setDisabled(True)
        self.pb_order_update.setDisabled(True)
        self.update_order_table()
        self.tv_order_items.setModel(None)

    @qtc.Slot()
    def process_update_order(self) -> None:
        """
    Opens an order editing form for the selected order and connects its finished signal to the update_order_table method.
    Clears the item list.
    
    Returns:
        None
        """
        self.Order_Update_Form = Order_Edit_Form(self.selected_order_id)
        self.Order_Update_Form.finished.connect(self.update_order_table)
        self.tv_order_items.setModel(None)
        self.Order_Update_Form.show()

    @qtc.Slot()
    def process_process_order(self) -> None:
        """
    Marks the selected order as processed by sending a PUT request to the API.
    Fetches the product table and updates the order table.
    
    Returns:
        None
        """
        requests.put(URL +'/order/' + str(self.selected_order_id), json={"process": True})
        self.fetch_product_table()
        self.update_order_table()

    @qtc.Slot()
    def order_no_filter(self) -> None:
        """
    Resets the order process sort filter to None and updates the order table.
    
    Returns:
        None
        """
        self.order_process_sort = None
        self.update_order_table()

    @qtc.Slot()
    def order_processed_filter(self) -> None:
        """
    Sets the order process sort filter to True (processed orders only) and updates the order table.
    
    Returns:
        None
        """
        self.order_process_sort = True
        self.update_order_table()

    @qtc.Slot()
    def order_unprocessed_filter(self) -> None:
        """
        Sets the order process sort filter to False (unprocessed orders only) and updates the order table.
        
        Returns:
            None
        """
        self.order_process_sort = False
        self.update_order_table()

if __name__ == "__main__":
    app = qtw.QApplication()
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
