import sys
from datetime import date, datetime, timedelta
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import packages.Functions as Functions

from UI.Form_ui import Ui_Form
from packages.progress_bar import Progress

class Segmentacao(QWidget, Ui_Form):
    def __init__(self, parent):
        super(Segmentacao, self).__init__()
        self.main = parent
        
        self.setupUi(self)

        hoje = date.today()
        #dt_hoje = datetime(year=hoje.year, month=hoje.month, day=hoje.day, hour=12, minute=0, second=0)
        dt_hoje = datetime(year=2024, month=6, day=20, hour=1, minute=21, second=0)
        self.date_first.setDateTime(dt_hoje)
        self.date_last.setDateTime(dt_hoje + timedelta(hours=4))

        self.cols = Functions.Cols()

        self.model = QStandardItemModel()

        # Adicionar itens ao modelo com checkboxes
        items = self.cols.keys
        for item_text in items:
            item = QStandardItem(item_text)
            item.setCheckable(True)
            item.setEditable(False)
            self.model.appendRow(item)

        self.listView.setModel(self.model)

        self.btn_tratar.clicked.connect(self.save_selected_items)
        self.btn_change_state.clicked.connect(self.add_button_clicked)
        self.listView.doubleClicked.connect(self.change_item_state)

    def change_item_state(self, index):
        item = self.model.itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

    def save_selected_items(self):
        selected_items = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            if item.checkState() == Qt.CheckState.Checked:
                selected_items.append(item.text())

        if len(selected_items) == 0:
            QMessageBox.warning(self, "Erro ao tratar os dados", "Selecione pelo menos 1 coluna para poder tratar")
        else:    
            selected_items.insert(0,"Data")
            
            self.cols.selected_cols = self.cols.get_sub_dict(selected_items)
            
            self.progress = Progress(self.main, self)
            self.progress.show()

    def add_button_clicked(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            self.change_item_state(indexes[0])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            indexes = self.listView.selectedIndexes()
            if indexes:
                self.change_item_state(indexes[0])
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Segmentacao(None)
    widget.show()
    sys.exit(app.exec())
