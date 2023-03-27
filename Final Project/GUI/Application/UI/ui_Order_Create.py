# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Order_Create.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableView, QVBoxLayout, QWidget)

class Ui_Create_Order_Form(object):
    def setupUi(self, create_order_form):
        if not create_order_form.objectName():
            create_order_form.setObjectName(u"create_order_form")
        create_order_form.resize(400, 300)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        create_order_form.setFont(font)
        self.verticalLayout = QVBoxLayout(create_order_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(create_order_form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_name = QLineEdit(create_order_form)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_2.addWidget(self.le_name)

        self.label_3 = QLabel(create_order_form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.le_address = QLineEdit(create_order_form)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_2.addWidget(self.le_address)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tv_product = QTableView(create_order_form)
        self.tv_product.setObjectName(u"tv_product")

        self.horizontalLayout.addWidget(self.tv_product)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.p_add = QPushButton(create_order_form)
        self.p_add.setObjectName(u"p_add")

        self.verticalLayout_2.addWidget(self.p_add)

        self.pb_remove = QPushButton(create_order_form)
        self.pb_remove.setObjectName(u"pb_remove")

        self.verticalLayout_2.addWidget(self.pb_remove)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(create_order_form)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.label)

        self.sb_quantity = QSpinBox(create_order_form)
        self.sb_quantity.setObjectName(u"sb_quantity")

        self.horizontalLayout_3.addWidget(self.sb_quantity)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tv_orderproducts = QTableView(create_order_form)
        self.tv_orderproducts.setObjectName(u"tv_orderproducts")

        self.horizontalLayout.addWidget(self.tv_orderproducts)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(create_order_form)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout_4.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(create_order_form)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_4.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(create_order_form)

        QMetaObject.connectSlotsByName(create_order_form)
    # setupUi

    def retranslateUi(self, create_order_form):
        create_order_form.setWindowTitle(QCoreApplication.translate("create_order_form", u"Create Order", None))
        self.label_2.setText(QCoreApplication.translate("create_order_form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("create_order_form", u"Address", None))
        self.p_add.setText(QCoreApplication.translate("create_order_form", u"Add", None))
        self.pb_remove.setText(QCoreApplication.translate("create_order_form", u"Remove", None))
        self.label.setText(QCoreApplication.translate("create_order_form", u"Quantity", None))
        self.pb_ok.setText(QCoreApplication.translate("create_order_form", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("create_order_form", u"Cancel", None))
    # retranslateUi

