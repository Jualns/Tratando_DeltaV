import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget, QListView
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QActionGroup
from pathlib import Path
from datetime import datetime
import time
import polars as pl
import packages.Functions as Functions

import os

from UI.Global_ui import Ui_MainWindow
from packages.thread import WorkerThread
from packages.table_widgets import TableWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_tratar.clicked.connect(self.open_file_dialog)
        
        self.global_vars = Functions.Global()
        self.window_icon = QIcon(str(self.global_vars.window_icon))
        self.setWindowIcon(self.window_icon)
        
        self.btn_finish.setVisible(False)
        self.btn_finish.clicked.connect(self.close_main)
        self.btn_finish.clicked.connect(self.open_excel_tratado)
        
        # Adicionar caixa de texto para registrar as etapas
        self.log_text.setReadOnly(True)
        
        self.cols = Functions.Cols()

        self.model = QStandardItemModel()

        # Adicionar itens ao modelo com checkboxes
        items = self.cols.keys
        for item_text in items:
            if item_text != "Data":
                item = QStandardItem(item_text)
                item.setCheckable(True)
                item.setEditable(False)
                self.model.appendRow(item)
                #item.setCheckable(False)
        
        self.model.itemChanged.connect(self.change_item_state)
        
        self.listView.setModel(self.model)
        
        self.listView.doubleClicked.connect(self.double_change_item_state)
        
        # Criar e iniciar a thread
        self.worker_thread = WorkerThread(self)
        self.worker_thread.update_progress.connect(self.update_visual)
        self.worker_thread.update_log.connect(self.add_log_entry)
        self.worker_thread.task_completed.connect(self.show_close_button)
        self.worker_thread.half_completed.connect(self.message_half)
        self.worker_thread.date_filtered.connect(self.update_dates)

    def message_half(self):
        QMessageBox.information(self, "Dados Tratados", "Selecione uma coluna a esquerda e as datas para tratar os dados!")

    def save_selected_items(self):
        selected_items = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            if item.checkState() == Qt.CheckState.Checked:
                selected_items.append(item.text())

        if len(selected_items) == 0:
            QMessageBox.warning(self, "Erro ao tratar os dados", "Selecione pelo menos 1 coluna para poder tratar")
        else:
            selected_items.insert(0, "Data")

            self.cols.selected_cols = self.cols.get_sub_dict(selected_items)

            self.worker_thread.start_last_step()

            #self.dockWidgetContents.setEnabled(False)
        
    
    def change_item_state(self, item: QStandardItem):
        # Não deixar pesado pois é executado 2 vezes ao dar double_click
        if item.checkState() == Qt.CheckState.Checked:
            self.demsmarca_todos_outros_itens(item)
    
    def double_change_item_state(self, index):
        item = self.model.itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Unchecked:
            # roda 2 vezes o change_item_state mas não causa grandes problemas de performance
            item.setCheckState(Qt.CheckState.Checked)
        else:
            item.setCheckState(Qt.CheckState.Unchecked)       
            
    def demsmarca_todos_outros_itens(self, item: QStandardItem):
         for row in range(self.model.rowCount()):
                model_item = self.model.item(row)
                if model_item != item and model_item.checkState() == Qt.CheckState.Checked:
                    model_item.setCheckState(Qt.CheckState.Unchecked)

    def update_dates(self, first: datetime, last: datetime):
        self.data_groupBox.setVisible(True)
        self.data_groupBox.setEnabled(True)
        
        self.first_date.setEnabled(True)
        self.last_date.setEnabled(True)

        self.first_date.setDateTime(first)
        self.last_date.setDateTime(last)

    def close_main(self):
        self.close()

    def open_file_dialog(self):
        file_dialog = QFileDialog(self, directory=str(self.global_vars.home))
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        
        if file_dialog.exec() == QFileDialog.DialogCode.Rejected:
            self.close_main()
        else:
            file_path = file_dialog.selectedFiles()[0]
            
            excel_ = self.global_vars.check_excel_file(file_path)
            
            if excel_:
                print(f"Arquivo selecionado: {file_path}")
                self.global_vars.set_path_to_read(Path(file_path))
        
        self.edit_deltav.setText(file_path)
        self.btn_start.setEnabled(True)
        
        QMessageBox.information(self, "Tratando Dados", "O arquivo do DeltaV já está sendo tratado em segundo plano!")
        
        self.start_workthread()
        
    def start_workthread(self):
        self.worker_thread.start_first_step()
    
    def update_visual(self, percent: int):
        self.progressBar.setValue(percent)

    def add_log_entry(self, text: str):
        self.log_text.append(text)
    
    def show_close_button(self):
        self.btn_finish.setVisible(True)

    def open_excel_tratado(self):
        time.sleep(1)
        print(self.global_vars.path_to_save)
        os.startfile(self.global_vars.path_to_save)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()