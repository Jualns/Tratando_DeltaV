import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from pathlib import Path
import packages.Functions as Functions

from UI.MainWindow_ui import Ui_MainWindow
from packages.segmentacao import Segmentacao

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_tratar.clicked.connect(self.open_file_dialog)
        self.btn_cancel.clicked.connect(self.close_main)
        self.btn_ok.clicked.connect(self.ok_btn_open)
        
        self.global_vars = Functions.Global()

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
        self.btn_ok.setEnabled(True)
        
    def ok_btn_open(self):
        self.segmentacao = Segmentacao(self)
        self.segmentacao.show()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()