import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import plotly.graph_objs as go
import polars as pl
from pathlib import Path

# Função para ler o arquivo Excel e retornar um DataFrame Polars
def read_(excel_path: Path):
    dt = pl.read_excel(excel_path)
    return dt

# Função para criar um gráfico Plotly
def create_plotly_graph(df):
    fig = go.Figure()
    for column in df.columns[1:]:
        fig.add_trace(go.Scatter(x=df['Data'], y=df[column], mode='lines', name=column))
    return fig

# Criação da janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criar um layout
        layout = QVBoxLayout()

        # Criar um widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Criar um QWebEngineView para renderizar o gráfico
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)
        
        self.webview.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.webview.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)


        # Caminho para o arquivo Excel
        read = Path(r"C:\Users\joao.silva\Desktop\Github\Tratando_DeltaV\output\DeltaV_Tratado.xlsx")

        # Ler o arquivo Excel
        df = read_(read)
        
        try:
            fig = create_plotly_graph(df)
            
            # Gera o HTML incluindo a referência ao CDN do Plotly
            html = fig.to_html(include_plotlyjs='cdn')
            
            # Caminho absoluto para salvar o arquivo HTML temporário
            html_file_path = Path("plot.html").absolute()
            
            # Salvar o HTML em um arquivo
            with open(html_file_path, 'w') as file:
                file.write(html)
            
            # Carregar o arquivo HTML no QWebEngineView
            self.webview.setUrl(html_file_path.as_uri())
        except Exception as e:
            print(f"Erro ao renderizar o gráfico: {e}")

# Iniciar a aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
