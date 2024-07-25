# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressBar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(471, 199)
        self.ProgressBar_layout = QVBoxLayout(ProgressBar)
        self.ProgressBar_layout.setObjectName(u"ProgressBar_layout")
        self.titulo = QLabel(ProgressBar)
        self.titulo.setObjectName(u"titulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        self.titulo.setFrameShape(QFrame.StyledPanel)
        self.titulo.setFrameShadow(QFrame.Plain)
        self.titulo.setMidLineWidth(-1)
        self.titulo.setTextFormat(Qt.MarkdownText)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.ProgressBar_layout.addWidget(self.titulo)

        self.log_text = QTextEdit(ProgressBar)
        self.log_text.setObjectName(u"log_text")

        self.ProgressBar_layout.addWidget(self.log_text)

        self.progressBar = QProgressBar(ProgressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QSize(0, 40))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat(u"%p%")

        self.ProgressBar_layout.addWidget(self.progressBar)

        self.btn_close = QPushButton(ProgressBar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setEnabled(True)

        self.ProgressBar_layout.addWidget(self.btn_close)


        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Form", None))
        self.titulo.setText(QCoreApplication.translate("ProgressBar", u"# Etapa N - Descritivo", None))
        self.btn_close.setText(QCoreApplication.translate("ProgressBar", u"Finalizar Programa", None))
    # retranslateUi

