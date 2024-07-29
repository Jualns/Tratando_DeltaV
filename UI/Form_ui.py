# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 461)
        icon = QIcon()
        icon.addFile(u"../icons8-delta-64.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_dates = QWidget(Form)
        self.widget_dates.setObjectName(u"widget_dates")
        self.formLayout = QFormLayout(self.widget_dates)
        self.formLayout.setObjectName(u"formLayout")
        self.label_fist_date = QLabel(self.widget_dates)
        self.label_fist_date.setObjectName(u"label_fist_date")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_fist_date)

        self.label_last_date = QLabel(self.widget_dates)
        self.label_last_date.setObjectName(u"label_last_date")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_last_date)

        self.date_first = QDateTimeEdit(self.widget_dates)
        self.date_first.setObjectName(u"date_first")
        self.date_first.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.date_first)

        self.date_last = QDateTimeEdit(self.widget_dates)
        self.date_last.setObjectName(u"date_last")
        self.date_last.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.date_last)


        self.verticalLayout_2.addWidget(self.widget_dates)

        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)

        self.widget_btns_list = QWidget(Form)
        self.widget_btns_list.setObjectName(u"widget_btns_list")
        self.verticalLayout = QVBoxLayout(self.widget_btns_list)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_change_state = QPushButton(self.widget_btns_list)
        self.btn_change_state.setObjectName(u"btn_change_state")

        self.verticalLayout.addWidget(self.btn_change_state)


        self.verticalLayout_2.addWidget(self.widget_btns_list)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.widget_btns_page = QWidget(Form)
        self.widget_btns_page.setObjectName(u"widget_btns_page")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_btns_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_cancelar = QPushButton(self.widget_btns_page)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout_3.addWidget(self.btn_cancelar)

        self.horizontalSpacer_2 = QSpacerItem(199, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_tratar = QPushButton(self.widget_btns_page)
        self.btn_tratar.setObjectName(u"btn_tratar")
        self.btn_tratar.setEnabled(True)
        self.btn_tratar.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.btn_tratar)


        self.verticalLayout_2.addWidget(self.widget_btns_page)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Filtragem de Informa\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("Form", u"# Segmenta\u00e7\u00e3o de Dados", None))
        self.label_fist_date.setText(QCoreApplication.translate("Form", u"Primeira Data:", None))
        self.label_last_date.setText(QCoreApplication.translate("Form", u"\u00daltima Data:", None))
        self.date_first.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy HH:mm:ss", None))
        self.date_last.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy HH:mm:ss", None))
        self.btn_change_state.setText(QCoreApplication.translate("Form", u"Marcar/Desmarcar Coluna", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btn_tratar.setText(QCoreApplication.translate("Form", u"Obter Dados", None))
    # retranslateUi

