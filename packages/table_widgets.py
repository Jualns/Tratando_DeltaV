import sys
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QProgressBar, QDateTimeEdit, QPushButton

class TableWidget(QTableWidget):
    def __init__(self, n_rows: int):
        super().__init__(rows = n_rows, columns = 4)

        # ! definir depois os nomes as colunas que vão aparecer
        self.setHorizontalHeaderLabels(["Data Inicial", "Data Final", "Tratativa Inicial", "Tratativa Final", "Botão de Ação"])
        
        # Preenche a tabela com widgets
        for i in range(n_rows):
            # Coluna de Data Inicial
            date_edit_start = QDateTimeEdit(self)
            date_edit_start.setDate(QDateTime.currentDateTime())
            self.setCellWidget(i, 0, date_edit_start)

            # Coluna de Data Final
            date_edit_end = QDateTimeEdit(self)
            date_edit_end.setDate(QDateTime.currentDateTime())
            self.setCellWidget(i, 1, date_edit_end)

            # Coluna de Barra de Progresso
            progress_bar = QProgressBar(self)
            progress_bar.setValue(10)
            self.setCellWidget(i, 2, progress_bar)
            
            # Coluna de Barra de Progresso
            progress_bar_final = QProgressBar(self)
            progress_bar_final.setValue(0)
            self.setCellWidget(i, 3, progress_bar_final)
            
            btn_push = QPushButton(self)
            self.setCellWidget(i, 4, btn_push)
            
        
        