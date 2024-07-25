# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 179)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy2)
        self.titulo.setTextFormat(Qt.MarkdownText)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.edits_layout = QHBoxLayout()
        self.edits_layout.setObjectName(u"edits_layout")
        self.edits_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.edit_deltav = QLineEdit(self.centralwidget)
        self.edit_deltav.setObjectName(u"edit_deltav")
        sizePolicy2.setHeightForWidth(self.edit_deltav.sizePolicy().hasHeightForWidth())
        self.edit_deltav.setSizePolicy(sizePolicy2)

        self.edits_layout.addWidget(self.edit_deltav)

        self.btn_tratar = QPushButton(self.centralwidget)
        self.btn_tratar.setObjectName(u"btn_tratar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_tratar.sizePolicy().hasHeightForWidth())
        self.btn_tratar.setSizePolicy(sizePolicy3)

        self.edits_layout.addWidget(self.btn_tratar)


        self.verticalLayout.addLayout(self.edits_layout)

        self.btns_layout = QHBoxLayout()
        self.btns_layout.setObjectName(u"btns_layout")
        self.btns_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.btns_layout.addWidget(self.btn_cancel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btns_layout.addItem(self.horizontalSpacer)

        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setEnabled(False)
        self.btn_ok.setCheckable(False)
        self.btn_ok.setAutoDefault(False)
        self.btn_ok.setFlat(False)

        self.btns_layout.addWidget(self.btn_ok)


        self.verticalLayout.addLayout(self.btns_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_ok.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"# Tratar arquivo DeltaV", None))
        self.btn_tratar.setText(QCoreApplication.translate("MainWindow", u"Procurar Arquivo", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"Obter Dados", None))
    # retranslateUi

