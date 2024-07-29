# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Global.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDockWidget, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.infos_groupBox = QGroupBox(self.centralwidget)
        self.infos_groupBox.setObjectName(u"infos_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.infos_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.log_text = QTextEdit(self.infos_groupBox)
        self.log_text.setObjectName(u"log_text")

        self.verticalLayout_4.addWidget(self.log_text)

        self.progressBar = QProgressBar(self.infos_groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.gridLayout.addWidget(self.infos_groupBox, 3, 0, 1, 1)

        self.btn_finish = QPushButton(self.centralwidget)
        self.btn_finish.setObjectName(u"btn_finish")

        self.gridLayout.addWidget(self.btn_finish, 4, 0, 1, 1)

        self.data_groupBox = QGroupBox(self.centralwidget)
        self.data_groupBox.setObjectName(u"data_groupBox")
        self.data_groupBox.setEnabled(False)
        self.data_groupBox.setFlat(False)
        self.data_groupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.data_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_firts = QLabel(self.data_groupBox)
        self.label_firts.setObjectName(u"label_firts")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_firts)

        self.first_date = QDateTimeEdit(self.data_groupBox)
        self.first_date.setObjectName(u"first_date")
        self.first_date.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_date)

        self.label_last = QLabel(self.data_groupBox)
        self.label_last.setObjectName(u"label_last")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_last)

        self.last_date = QDateTimeEdit(self.data_groupBox)
        self.last_date.setObjectName(u"last_date")
        self.last_date.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_date)

        self.btn_start = QPushButton(self.data_groupBox)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setAutoDefault(False)
        self.btn_start.setFlat(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.btn_start)


        self.gridLayout.addWidget(self.data_groupBox, 2, 0, 1, 1)

        self.selection_groupBox = QGroupBox(self.centralwidget)
        self.selection_groupBox.setObjectName(u"selection_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.selection_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.select_dados = QHBoxLayout()
        self.select_dados.setObjectName(u"select_dados")
        self.edit_deltav = QLineEdit(self.selection_groupBox)
        self.edit_deltav.setObjectName(u"edit_deltav")
        self.edit_deltav.setReadOnly(True)

        self.select_dados.addWidget(self.edit_deltav)

        self.btn_tratar = QPushButton(self.selection_groupBox)
        self.btn_tratar.setObjectName(u"btn_tratar")

        self.select_dados.addWidget(self.btn_tratar)


        self.verticalLayout_3.addLayout(self.select_dados)


        self.gridLayout.addWidget(self.selection_groupBox, 1, 0, 1, 1)

        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setTextFormat(Qt.MarkdownText)
        self.Titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Titulo, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubTitulo = QLabel(self.dockWidgetContents)
        self.SubTitulo.setObjectName(u"SubTitulo")
        self.SubTitulo.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.SubTitulo)

        self.listView = QListView(self.dockWidgetContents)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)

        self.retranslateUi(MainWindow)

        self.btn_start.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.infos_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Log Informa\u00e7\u00f5es", None))
#if QT_CONFIG(statustip)
        self.log_text.setStatusTip(QCoreApplication.translate("MainWindow", u"Log das etapas", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.btn_finish.setStatusTip(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de finaliza\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar Programa", None))
        self.data_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o de Data", None))
        self.label_firts.setText(QCoreApplication.translate("MainWindow", u"Primeria Data", None))
#if QT_CONFIG(statustip)
        self.first_date.setStatusTip(QCoreApplication.translate("MainWindow", u"Data inicial dos dados", None))
#endif // QT_CONFIG(statustip)
        self.first_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy HH:mm:ss", None))
        self.label_last.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Data", None))
#if QT_CONFIG(statustip)
        self.last_date.setStatusTip(QCoreApplication.translate("MainWindow", u"Data final dos dados", None))
#endif // QT_CONFIG(statustip)
        self.last_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy HH:mm:ss", None))
#if QT_CONFIG(statustip)
        self.btn_start.setStatusTip(QCoreApplication.translate("MainWindow", u"Iniciar tratativa dos dados", None))
#endif // QT_CONFIG(statustip)
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Iniciar Tratativa", None))
        self.selection_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o de Arquivos", None))
#if QT_CONFIG(statustip)
        self.edit_deltav.setStatusTip(QCoreApplication.translate("MainWindow", u"Caminho do arquivo DeltaV", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.btn_tratar.setStatusTip(QCoreApplication.translate("MainWindow", u"Bot\u00e3o para procurar arquivo", None))
#endif // QT_CONFIG(statustip)
        self.btn_tratar.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivo", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"# Tratar arquivo DeltaV", None))
        self.SubTitulo.setText(QCoreApplication.translate("MainWindow", u"### Segmenta\u00e7\u00e3o de Dados", None))
#if QT_CONFIG(statustip)
        self.listView.setStatusTip(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o de colunas", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

