import sys
import time
from datetime import datetime, timedelta
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt, QThread, Signal
import packages.Functions as Functions
import polars as pl

from UI.ProgressBar_ui import Ui_ProgressBar

class WorkerThread(QThread):
    update_progress = Signal(str, int)
    update_log = Signal(str)
    task_completed = Signal()

    def __init__(self, main, parent):
        super().__init__()
        self.main_window = main
        self.parent_window = parent

    def run(self):
        self.update_task("# Tratativas DeltaV", 0)
        time.sleep(1)

        self.update_task("# Lendo DeltaV", 20)
        dfs: pl.DataFrame = Functions.ler_arquivo(self.main_window.global_vars.path_to_read)

        self.update_task("# Mesclando Planilhas", 40)
        df: pl.DataFrame = Functions.merge_planilhas(dfs)
        time.sleep(1)

        self.update_task("# Tratando Dados", 60)
        df = Functions.tratando_dados(df)
        time.sleep(1)

        self.update_task("# Filtrando Dados", 80)
        result: pl.DataFrame = Functions.filtrando_dados(
            start_date=self.parent_window.date_first.dateTime().toPython(),
            end_date=self.parent_window.date_last.dateTime().toPython(),
            tipo_cols=self.parent_window.cols.selected_cols,
            dt=df)
        time.sleep(1)

        self.update_task("# Salvando DeltaV Tratado", 100)
        Functions.save_deltav(result, self.main_window.global_vars.path_to_save)
        time.sleep(1)

        self.task_completed.emit()

    def update_task(self, title: str, percent: int):
        self.update_log.emit(f"OK - {title}")
        self.update_progress.emit(title, percent)

class Progress(QWidget, Ui_ProgressBar):
    def __init__(self, main, parent):
        super(Progress, self).__init__()

        self.main_window = main
        self.parent_window = parent

        self.setupUi(self)

        # Adicionar caixa de texto para registrar as etapas
        self.log_text.setReadOnly(True)

        # Esconder o botão de fechar inicialmente
        self.btn_close.setVisible(False)

        # Criar e iniciar a thread
        self.worker_thread = WorkerThread(self.main_window, self.parent_window)
        self.worker_thread.update_progress.connect(self.update_visual)
        self.worker_thread.update_log.connect(self.add_log_entry)
        self.worker_thread.task_completed.connect(self.show_close_button)
        self.worker_thread.start()

        self.btn_close.clicked.connect(self.close_all_windows)

    def update_visual(self, title: str, percent: int):
        self.titulo.setText(title)
        self.progressBar.setValue(percent)

    def add_log_entry(self, text: str):
        self.log_text.append(text)

    def show_close_button(self):
        self.btn_close.setVisible(True)

    def close_all_windows(self):
        self.parent_window.close()
        self.main_window.close()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Progress(None, None)
    widget.show()
    sys.exit(app.exec())
