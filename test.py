from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import time

class Worker(QObject):
    progress = Signal(int)  # Sinal para enviar o progresso para a UI

    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id

    def run(self):
        for i in range(1, 6):
            time.sleep(1)  # Simula uma tarefa demorada
            self.progress.emit(i)
        print(f"Thread {self.thread_id} terminou.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel("Thread 1: Aguardando...")
        self.label2 = QLabel("Thread 2: Aguardando...")

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        self.thread1 = QThread()
        self.thread2 = QThread()

        self.worker1 = Worker(thread_id=1)
        self.worker2 = Worker(thread_id=2)

        self.worker1.moveToThread(self.thread1)
        self.worker2.moveToThread(self.thread2)

        self.worker1.progress.connect(self.update_label1)
        self.worker2.progress.connect(self.update_label2)

        self.thread1.started.connect(self.worker1.run)
        self.thread2.started.connect(self.worker2.run)

        self.thread1.start()
        self.thread2.start()

    def update_label1(self, value):
        self.label1.setText(f"Thread 1: Progresso {value}/5")

    def update_label2(self, value):
        self.label2.setText(f"Thread 2: Progresso {value}/5")

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
