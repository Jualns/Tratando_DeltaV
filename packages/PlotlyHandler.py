from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import plotly.graph_objs as go
import polars as pl
from pathlib import Path
import os

# Função para criar um gráfico Plotly com anotações para valores médios, mínimos e máximos
def create_plotly_graph(df):
    fig = go.Figure()

    # Adicionar linhas para cada coluna de dados
    for column in df.columns[1:]:
        # Dados da série
        y_data = df[column]
        x_data = df['Data']
        
        # Adicionar a linha da série
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name=column))

        # Calcular valores médio, mínimo e máximo
        mean_y = y_data.mean()
        min_y = y_data.min()
        max_y = y_data.max()
        
        print("#"+"-"*50+"#\n")
        print(f"Valores {column}")
        print(f"Mínimo: {min_y}\nMáximo: {max_y}\nMédia: {mean_y}\n")
        print("#"+"-"*50+"#\n")

        # Adicionar linha para o valor médio
        fig.add_trace(go.Scatter(
            x=[x_data.min(), x_data.max()],
            y=[mean_y, mean_y],
            mode='lines',
            line=dict(dash='dash', color='red'),
            name=f'{column} Média'
        ))

        # Adicionar linha para o valor mínimo
        fig.add_trace(go.Scatter(
            x=[x_data.min(), x_data.max()],
            y=[min_y, min_y],
            mode='lines',
            line=dict(dash='dot', color='green'),
            name=f'{column} Mínimo'
        ))

        # Adicionar linha para o valor máximo
        fig.add_trace(go.Scatter(
            x=[x_data.min(), x_data.max()],
            y=[max_y, max_y],
            mode='lines',
            line=dict(dash='dashdot', color='blue'),
            name=f'{column} Máximo'
        ))

        # Adicionar anotações para valores médio, mínimo e máximo
        fig.add_annotation(
            x=x_data.max(), y=mean_y,
            text=f"Média: {mean_y:.2f}",
            showarrow=True,
            arrowhead=1
        )
        fig.add_annotation(
            x=x_data.max(), y=min_y,
            text=f"Mínimo: {min_y:.2f}",
            showarrow=True,
            arrowhead=1
        )
        fig.add_annotation(
            x=x_data.max(), y=max_y,
            text=f"Máximo: {max_y:.2f}",
            showarrow=True,
            arrowhead=1
        )

    return fig

# Criação da janela
class PlotlyHandle(QWebEngineView):
    def __init__(self, df: pl.DataFrame, save_f: bool, path_to_save: Path):
        super().__init__()

        self.dt = df

        # Criar um QWebEngineView para renderizar o gráfico
        #self.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        #self.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        
        try:
            fig = create_plotly_graph(self.dt)
            
            # Gera o HTML incluindo a referência ao CDN do Plotly
            html = fig.to_html(include_plotlyjs='cdn')
            
            # Caminho absoluto para salvar o arquivo HTML temporário
            html_file_path = Path(path_to_save, "plot.html").absolute()
            
            # Salvar o HTML em um arquivo
            if save_f:
                with open(html_file_path, 'w') as file:
                    file.write(html)

            # PARA ABRIR O ARQUIVO NO PRÓPRIO APP BASTA INSERIR O WEBENGINE TODO UM WIDGET E DESCOMENTAR self.setUrl(html_file_path.as_uri())
            # Carregar o arquivo HTML no QWebEngineView
            #self.setUrl(html_file_path.as_uri())
            
            # Abrir arquivo html
            #os.startfile(html_file_path)
            
            fig.show()
                
        except Exception as e:
            print(f"Erro ao renderizar o gráfico: {e}")
