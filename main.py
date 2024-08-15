import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QActionGroup
from pathlib import Path
from datetime import datetime
import time
import polars as pl
import packages.Functions as Functions
from packages import PlotlyHandler
import os

from UI.Global_ui import Ui_MainWindow

class WorkerThread(QThread):
    update_progress = Signal(int)
    update_log = Signal(str)
    task_completed = Signal()
    date_filtered = Signal(datetime, datetime)

    def __init__(self, main):
        super().__init__()
        self.main_window = main
        self.df = None
        self.current_step = None

    def run(self):
        if self.current_step == "first_step":
            self.first_step()
        elif self.current_step == "last_step":
            self.last_step()
            
    def start_first_step(self):
        self.current_step = "first_step"
        self.start()

    def start_last_step(self):
        self.current_step = "last_step"
        self.start()

    def first_step(self):
        # Mudar o cursor para "carregando"
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        
        self.update_task("# Tratativas DeltaV", 0)
        time.sleep(1)

        self.update_task("# Lendo DeltaV", 20)
        dfs: pl.DataFrame = Functions.ler_arquivo(self.main_window.global_vars.path_to_read)

        self.update_task("# Mesclando Planilhas", 40)
        self.df: pl.DataFrame = Functions.merge_planilhas(dfs)

        self.update_task("# Obtendo Datas", 50)
        first, last = Functions.get_first_last_date(self.df)

        self.date_filtered.emit(first, last)

        self.update_task("# Selecione as Datas", 50)
        
        # Restaurar o cursor normal
        QApplication.restoreOverrideCursor()

    def last_step(self):
        # Mudar o cursor para "carregando"
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        
        self.update_task("# Tratando Dados", 60)
        self.df = Functions.tratando_dados(self.df)
        time.sleep(1)

        self.update_task("# Filtrando Dados", 80)
        result: pl.DataFrame = Functions.filtrando_dados(
            start_date=self.main_window.first_date.dateTime().toPython(),
            end_date=self.main_window.last_date.dateTime().toPython(),
            tipo_cols=self.main_window.cols.selected_cols,
            dt=self.df)
        
        self.plot_handler = PlotlyHandler.PlotlyHandle(
                                            result, 
                                            self.main_window.actionSalvar_Arquivo.isChecked()
                                        )
        
        #time.sleep(1)

        if self.main_window.actionSalvar_Arquivo.isChecked():
            self.update_task("# Salvando DeltaV Tratado", 100)
            Functions.save_deltav(result, self.main_window.global_vars.path_to_save)
            time.sleep(1)

        # Restaurar o cursor normal
        QApplication.restoreOverrideCursor()

        self.task_completed.emit()

    def update_task(self, title: str, percent: int):
        self.update_log.emit(f"OK - {datetime.now().strftime("%H:%M:%S")} - {title}")
        self.update_progress.emit(percent)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_tratar.clicked.connect(self.open_file_dialog)
        self.btn_start.clicked.connect(self.save_selected_items)
        
        self.global_vars = Functions.Global()
        self.window_icon = QIcon(str(self.global_vars.window_icon))
        self.setWindowIcon(self.window_icon)
        
        self.btn_finish.setVisible(False)
        self.btn_finish.clicked.connect(self.close_main)
        self.btn_finish.clicked.connect(self.open_excel_tratado)
        
        # Adicionar caixa de texto para registrar as etapas
        self.log_text.setReadOnly(True)
        
        self.data_groupBox.setVisible(False)
        
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

        self.listView.setModel(self.model)
        self.listView.doubleClicked.connect(self.change_item_state)
        
        # Criar e iniciar a thread
        self.worker_thread = WorkerThread(self)
        self.worker_thread.update_progress.connect(self.update_visual)
        self.worker_thread.update_log.connect(self.add_log_entry)
        self.worker_thread.task_completed.connect(self.show_close_button)
        self.worker_thread.date_filtered.connect(self.update_dates)

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
        
        
    def change_item_state(self, index):
        item = self.model.itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)        

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