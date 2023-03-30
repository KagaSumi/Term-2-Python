# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(850, 578)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        Main.setFont(font)
        Main.setToolButtonStyle(Qt.ToolButtonTextOnly)
        Main.setAnimated(True)
        Main.setTabShape(QTabWidget.Rounded)
        self.actionExit = QAction(Main)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setEnabled(True)
        self.actionExit.setShortcutContext(Qt.WindowShortcut)
        self.actionExit.setMenuRole(QAction.TextHeuristicRole)
        self.actionAdd_New_Product = QAction(Main)
        self.actionAdd_New_Product.setObjectName(u"actionAdd_New_Product")
        self.actionCreate_New_Order = QAction(Main)
        self.actionCreate_New_Order.setObjectName(u"actionCreate_New_Order")
        self.actionEdit_Order = QAction(Main)
        self.actionEdit_Order.setObjectName(u"actionEdit_Order")
        self.actionCreated_By_Quinten_Leung = QAction(Main)
        self.actionCreated_By_Quinten_Leung.setObjectName(u"actionCreated_By_Quinten_Leung")
        self.actionCreated_By_Quinten_Leung.setEnabled(False)
        self.actionCreated_By_Quinten_Leung.setMenuRole(QAction.NoRole)
        self.actionCreated_By_Quinten = QAction(Main)
        self.actionCreated_By_Quinten.setObjectName(u"actionCreated_By_Quinten")
        self.actionCreated_By_Quinten.setEnabled(False)
        self.actionA01055681 = QAction(Main)
        self.actionA01055681.setObjectName(u"actionA01055681")
        self.actionA01055681.setEnabled(False)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Main_ui = QTabWidget(self.centralwidget)
        self.Main_ui.setObjectName(u"Main_ui")
        self.Main_ui.setLayoutDirection(Qt.LeftToRight)
        self.Main_ui.setAutoFillBackground(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(22)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.cb_out_of_stock = QCheckBox(self.tab)
        self.cb_out_of_stock.setObjectName(u"cb_out_of_stock")

        self.verticalLayout_2.addWidget(self.cb_out_of_stock)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pb_create = QPushButton(self.tab)
        self.pb_create.setObjectName(u"pb_create")
        self.pb_create.setAutoDefault(False)
        self.pb_create.setFlat(False)

        self.verticalLayout_3.addWidget(self.pb_create)

        self.pb_delete = QPushButton(self.tab)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pb_delete)

        self.pb_update = QPushButton(self.tab)
        self.pb_update.setObjectName(u"pb_update")
        self.pb_update.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pb_update)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 8, 0, 1, 1)

        self.tv_product_list = QTableView(self.tab)
        self.tv_product_list.setObjectName(u"tv_product_list")

        self.gridLayout_2.addWidget(self.tv_product_list, 8, 1, 1, 1)

        self.Main_ui.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rb_order_no_filter = QRadioButton(self.tab_2)
        self.rb_order_no_filter.setObjectName(u"rb_order_no_filter")
        self.rb_order_no_filter.setChecked(True)

        self.verticalLayout_6.addWidget(self.rb_order_no_filter)

        self.rb_order_unprocessed = QRadioButton(self.tab_2)
        self.rb_order_unprocessed.setObjectName(u"rb_order_unprocessed")

        self.verticalLayout_6.addWidget(self.rb_order_unprocessed)

        self.rb_order_processed = QRadioButton(self.tab_2)
        self.rb_order_processed.setObjectName(u"rb_order_processed")

        self.verticalLayout_6.addWidget(self.rb_order_processed)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setKerning(False)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.le_order_filter = QLineEdit(self.tab_2)
        self.le_order_filter.setObjectName(u"le_order_filter")

        self.horizontalLayout.addWidget(self.le_order_filter)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout_7, 4, 0, 1, 1)

        self.pb_order_delete = QPushButton(self.tab_2)
        self.pb_order_delete.setObjectName(u"pb_order_delete")
        self.pb_order_delete.setEnabled(False)

        self.gridLayout_3.addWidget(self.pb_order_delete, 2, 0, 1, 2)

        self.pb_order_update = QPushButton(self.tab_2)
        self.pb_order_update.setObjectName(u"pb_order_update")
        self.pb_order_update.setEnabled(False)

        self.gridLayout_3.addWidget(self.pb_order_update, 1, 0, 1, 2)

        self.pb_order_create = QPushButton(self.tab_2)
        self.pb_order_create.setObjectName(u"pb_order_create")

        self.gridLayout_3.addWidget(self.pb_order_create, 0, 0, 1, 2)

        self.pb_order_process = QPushButton(self.tab_2)
        self.pb_order_process.setObjectName(u"pb_order_process")
        self.pb_order_process.setEnabled(False)

        self.gridLayout_3.addWidget(self.pb_order_process, 3, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tv_order_view = QTableView(self.tab_2)
        self.tv_order_view.setObjectName(u"tv_order_view")

        self.verticalLayout_4.addWidget(self.tv_order_view)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.tv_order_items = QTableView(self.tab_2)
        self.tv_order_items.setObjectName(u"tv_order_items")

        self.verticalLayout_4.addWidget(self.tv_order_items)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.Main_ui.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.Main_ui, 1, 0, 1, 1)

        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 29))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menuFile)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setEnabled(True)
        Main.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionCreated_By_Quinten)
        self.menuAbout.addAction(self.actionA01055681)

        self.retranslateUi(Main)

        self.Main_ui.setCurrentIndex(0)
        self.pb_create.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionExit.setText(QCoreApplication.translate("Main", u"Exit", None))
        self.actionAdd_New_Product.setText(QCoreApplication.translate("Main", u"Create New Product", None))
        self.actionCreate_New_Order.setText(QCoreApplication.translate("Main", u"Create New Order", None))
        self.actionEdit_Order.setText(QCoreApplication.translate("Main", u"Edit Order", None))
        self.actionCreated_By_Quinten_Leung.setText(QCoreApplication.translate("Main", u"Created By Quinten Leung", None))
        self.actionCreated_By_Quinten.setText(QCoreApplication.translate("Main", u"Created By Quinten", None))
        self.actionA01055681.setText(QCoreApplication.translate("Main", u"A01055681", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Product List", None))
        self.cb_out_of_stock.setText(QCoreApplication.translate("Main", u"View Out of stock", None))
        self.pb_create.setText(QCoreApplication.translate("Main", u"Create", None))
        self.pb_delete.setText(QCoreApplication.translate("Main", u"Delete", None))
        self.pb_update.setText(QCoreApplication.translate("Main", u"Update", None))
        self.Main_ui.setTabText(self.Main_ui.indexOf(self.tab), QCoreApplication.translate("Main", u"Products", None))
        self.rb_order_no_filter.setText(QCoreApplication.translate("Main", u"No Filter", None))
        self.rb_order_unprocessed.setText(QCoreApplication.translate("Main", u"Unprocessed", None))
        self.rb_order_processed.setText(QCoreApplication.translate("Main", u"Processed", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"Filter By Name:", None))
        self.pb_order_delete.setText(QCoreApplication.translate("Main", u"Delete", None))
        self.pb_order_update.setText(QCoreApplication.translate("Main", u"Update", None))
        self.pb_order_create.setText(QCoreApplication.translate("Main", u"Create", None))
        self.pb_order_process.setText(QCoreApplication.translate("Main", u"Process", None))
        self.label.setText(QCoreApplication.translate("Main", u"Orders", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"Order's Item", None))
        self.Main_ui.setTabText(self.Main_ui.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Orders", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("Main", u"About", None))
    # retranslateUi

