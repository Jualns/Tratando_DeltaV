from packages import PlotlyHandler
from PySide6.QtCore import Qt, QThread, Signal
from datetime import datetime
from PySide6.QtWidgets import QApplication
import time
import polars as pl
import packages.Functions as Functions

class WorkerThread(QThread):
    update_progress = Signal(int)
    update_log = Signal(str)
    task_completed = Signal()
    half_completed = Signal()
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
    
        self.half_completed.emit()
    
    def last_step(self):
        # Mudar o cursor para "carregando"
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        
        self.update_task("# Tratando Dados", 60)
        self.df = Functions.tratando_dados(self.df)

        self.update_task("# Filtrando Dados", 80)
        result: pl.DataFrame = Functions.filtrando_dados(
            start_date=self.main_window.first_date.dateTime().toPython(),
            end_date=self.main_window.last_date.dateTime().toPython(),
            tipo_cols=self.main_window.cols.selected_cols,
            dt=self.df)
        
        result = result.sort(by="Data")
        
        self.plot_handler = PlotlyHandler.PlotlyHandle(
                                            df = result, 
                                            save_f = self.main_window.actionSalvar_Arquivo.isChecked(),
                                            path_to_save = self.main_window.global_vars.home
                                        )

        if self.main_window.actionSalvar_Arquivo.isChecked():
            self.update_task("# Salvando DeltaV Tratado", 100)
            Functions.save_deltav(result, self.main_window.global_vars.path_to_save)
            self.update_log.emit(f"Finalizado - {datetime.now().strftime("%H:%M:%S")}\n")

        # Restaurar o cursor normal
        QApplication.restoreOverrideCursor()

        self.task_completed.emit()

    def update_task(self, title: str, percent: int):
        self.update_log.emit(f"OK - {datetime.now().strftime("%H:%M:%S")} - {title}")
        self.update_progress.emit(percent)