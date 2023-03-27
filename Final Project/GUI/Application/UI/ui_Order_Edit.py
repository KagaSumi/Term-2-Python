# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Order_Edit.ui'
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

class Ui_Edit_Order_Form(object):
    def setupUi(self, Edit_Order_Form):
        if not Edit_Order_Form.objectName():
            Edit_Order_Form.setObjectName(u"Edit_Order_Form")
        Edit_Order_Form.resize(614, 554)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        Edit_Order_Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Edit_Order_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(Edit_Order_Form)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.le_name_4 = QLineEdit(Edit_Order_Form)
        self.le_name_4.setObjectName(u"le_name_4")
        self.le_name_4.setEnabled(True)

        self.horizontalLayout_13.addWidget(self.le_name_4)

        self.label_11 = QLabel(Edit_Order_Form)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.le_address_4 = QLineEdit(Edit_Order_Form)
        self.le_address_4.setObjectName(u"le_address_4")

        self.horizontalLayout_13.addWidget(self.le_address_4)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tv_product_4 = QTableView(Edit_Order_Form)
        self.tv_product_4.setObjectName(u"tv_product_4")

        self.horizontalLayout_15.addWidget(self.tv_product_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(Edit_Order_Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_12.setIndent(-1)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.sb_quantity_4 = QSpinBox(Edit_Order_Form)
        self.sb_quantity_4.setObjectName(u"sb_quantity_4")

        self.horizontalLayout_16.addWidget(self.sb_quantity_4)

        self.p_add_4 = QPushButton(Edit_Order_Form)
        self.p_add_4.setObjectName(u"p_add_4")

        self.horizontalLayout_16.addWidget(self.p_add_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.pb_remove_4 = QPushButton(Edit_Order_Form)
        self.pb_remove_4.setObjectName(u"pb_remove_4")

        self.verticalLayout_5.addWidget(self.pb_remove_4)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.pb_ok = QPushButton(Edit_Order_Form)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout_14.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(Edit_Order_Form)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_14.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.verticalLayout.addLayout(self.horizontalLayout_18)


        self.retranslateUi(Edit_Order_Form)

        QMetaObject.connectSlotsByName(Edit_Order_Form)
    # setupUi

    def retranslateUi(self, Edit_Order_Form):
        Edit_Order_Form.setWindowTitle(QCoreApplication.translate("Edit_Order_Form", u"Edit Order", None))
        self.label_10.setText(QCoreApplication.translate("Edit_Order_Form", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("Edit_Order_Form", u"Address", None))
        self.label_12.setText(QCoreApplication.translate("Edit_Order_Form", u"Quantity", None))
        self.p_add_4.setText(QCoreApplication.translate("Edit_Order_Form", u"Update", None))
        self.pb_remove_4.setText(QCoreApplication.translate("Edit_Order_Form", u"Remove", None))
        self.pb_ok.setText(QCoreApplication.translate("Edit_Order_Form", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("Edit_Order_Form", u"Cancel", None))
    # retranslateUi

