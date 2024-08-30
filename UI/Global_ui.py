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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 586)
        self.actionSalvar_Arquivo = QAction(MainWindow)
        self.actionSalvar_Arquivo.setObjectName(u"actionSalvar_Arquivo")
        self.actionSalvar_Arquivo.setCheckable(True)
        self.actionSalvar_Arquivo.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_finish = QPushButton(self.centralwidget)
        self.btn_finish.setObjectName(u"btn_finish")

        self.gridLayout.addWidget(self.btn_finish, 4, 0, 1, 1)

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

        self.table_box = QGroupBox(self.centralwidget)
        self.table_box.setObjectName(u"table_box")
        self.verticalLayout_5 = QVBoxLayout(self.table_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.table_box)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.gridLayout.addWidget(self.table_box, 2, 0, 1, 1)

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

        self.log_box = QGroupBox(self.dockWidgetContents)
        self.log_box.setObjectName(u"log_box")
        self.verticalLayout_4 = QVBoxLayout(self.log_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.log_text = QTextEdit(self.log_box)
        self.log_text.setObjectName(u"log_text")

        self.verticalLayout_4.addWidget(self.log_text)


        self.verticalLayout.addWidget(self.log_box)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 953, 21))
        self.menuBar.setLayoutDirection(Qt.RightToLeft)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuGraph_Options = QMenu(self.menuBar)
        self.menuGraph_Options.setObjectName(u"menuGraph_Options")
        self.menuGraph_Options.setLayoutDirection(Qt.LeftToRight)
        self.menuGraph_Options.setTearOffEnabled(False)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuGraph_Options.menuAction())
        self.menuGraph_Options.addAction(self.actionSalvar_Arquivo)
        self.menuGraph_Options.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSalvar_Arquivo.setText(QCoreApplication.translate("MainWindow", u"Salvar Arquivo", None))
#if QT_CONFIG(statustip)
        self.btn_finish.setStatusTip(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de finaliza\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar Programa", None))
        self.selection_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Selecione uma Pasta", None))
#if QT_CONFIG(statustip)
        self.edit_deltav.setStatusTip(QCoreApplication.translate("MainWindow", u"Caminho da pasta com os arquivos DeltaV que vai comparar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.btn_tratar.setStatusTip(QCoreApplication.translate("MainWindow", u"Bot\u00e3o para procurar pasta", None))
#endif // QT_CONFIG(statustip)
        self.btn_tratar.setText(QCoreApplication.translate("MainWindow", u"Selecionar Pasta", None))
        self.table_box.setTitle(QCoreApplication.translate("MainWindow", u"Tabela de Tratativas", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"# Tratar arquivo DeltaV", None))
        self.SubTitulo.setText(QCoreApplication.translate("MainWindow", u"### Segmenta\u00e7\u00e3o de Dados", None))
#if QT_CONFIG(statustip)
        self.listView.setStatusTip(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o de colunas", None))
#endif // QT_CONFIG(statustip)
        self.log_box.setTitle(QCoreApplication.translate("MainWindow", u"Log das Etapas", None))
        self.menuGraph_Options.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es do Gr\u00e1fico", None))
    # retranslateUi

