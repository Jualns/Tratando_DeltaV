import polars as pl
from datetime import datetime, date
from PySide6.QtGui import QIcon 
import os
from pathlib import Path
from typing import Dict
from dataclasses import dataclass

@dataclass
class Cols:
    keys = ["Data", "Temperatura Vaso Balanca V-125", "Peso Real Vaso Balanca V-125", "Valv Fino Agua Entrada V-125", "Valv Fino Fenol Entrada V-125", "Valv Fino Formol Entrada V-125", "Valv Fino Glicerina Entrada V-125", "Valv Fino Metanol Entrada V-125", "Valv Vapor Entrada V-125", "Totalizador Vaso Balanca V-125", "Vazao de MP que sai V-125 para R-106", "Valv Control Fundo V-125", "Valv Control Fundo V-125", "Valv Control Fundo V-125", "Valv Entrada MP R-106", "Peso Real Vaso Balanca V-121 - Soda", "Totalizador Vaso Balanca V-121 - Soda", "Vazao de MP que sai V-121 para R-106", "Valv Entrada Soda R-106", "Valv Control Retorno AGR Condensador", "Valv Control Retorno AGR Condensador", "Valv Control Retorno AGR Condensador", "Medidor de vazao Retorno Agua Torre ", "Temp Entrada Agua Torre Condensador", "Temp RETORNO Agua Torre Condensador", "Temp Destilado", "Temp Reator", "Taxa Temp / Min", "Vazao Massica de vapor", "Pressao de vapor", "Valv Control Vapor", "Valv Control Vapor", "Valv Control Vapor", "Valv Vapor Serpentina", "Valv Ar Comprimido", "Valv Condensado", "Valv Vapor Vivo 1", "Valv Vapor Vivo 2", "Valv Vapor Vivo 3", "Valv Vapor Vivo 4", "Valv Entrada Agua Torre Reator", "Pressao Reator", "Valv Control Vacuo", "Valv Control Vacuo", "Valv Control Vacuo", "Valv Quebra Vacuo", "Valv Destilado Reator", "Valv Destilado Vaso Aparas", "Nivel Vaso de Aparas", "Corrente Agitador Reator", "Balanca Soda", "Balanca Acido Fluoridrico", "Balanca DIBP/DBE", "Balanca SOLVESSO / ALCOOL"]
    dic = {"Data": datetime, 'Temperatura Vaso Balanca V-125': float, 'Peso Real Vaso Balanca V-125': float, 'Valv Fino Agua Entrada V-125': str, 'Valv Fino Fenol Entrada V-125': str, 'Valv Fino Formol Entrada V-125': str, 'Valv Fino Glicerina Entrada V-125': str, 'Valv Fino Metanol Entrada V-125': str, 'Valv Vapor Entrada V-125': str, 'Totalizador Vaso Balanca V-125': float, 'Vazao de MP que sai V-125 para R-106': float, 'Valv Control Fundo V-125': float, 'Valv Entrada MP R-106': str, 'Peso Real Vaso Balanca V-121 - Soda': float, 'Totalizador Vaso Balanca V-121 - Soda': float, 'Vazao de MP que sai V-121 para R-106': str, 'Valv Entrada Soda R-106': str, 'Valv Control Retorno AGR Condensador': float, 'Medidor de vazao Retorno Agua Torre ': float, 'Temp Entrada Agua Torre Condensador': float, 'Temp RETORNO Agua Torre Condensador': float, 'Temp Destilado': float, 'Temp Reator': float, 'Taxa Temp / Min': float, 'Vazao Massica de vapor': float, 'Pressao de vapor': float, 'Valv Control Vapor': float, 'Valv Vapor Serpentina': str, 'Valv Ar Comprimido': str, 'Valv Condensado': str, 'Valv Vapor Vivo 1': str, 'Valv Vapor Vivo 2': str, 'Valv Vapor Vivo 3': str, 'Valv Vapor Vivo 4': str, 'Valv Entrada Agua Torre Reator': str, 'Pressao Reator': float, 'Valv Control Vacuo': float, 'Valv Quebra Vacuo': str, 'Valv Destilado Reator': str, 'Valv Destilado Vaso Aparas': str, 'Nivel Vaso de Aparas': float, 'Corrente Agitador Reator': float, 'Balanca Soda': float, 'Balanca Acido Fluoridrico': float, 'Balanca DIBP/DBE': float, 'Balanca SOLVESSO / ALCOOL': float}
    selected_cols = dict()
    
    def get_sub_dict(self, list_keys: list[str])->Dict[str, float | str]:
        return {key: self.dic[key] for key in list_keys}
    
class Global:
    home = Path(os.getcwd())
    arquivo_original = None
    save_name = "DeltaV_Tratado.xlsx"
    
    path_to_read = Path(home, arquivo_original if arquivo_original else "")
    path_to_save = Path(home, save_name)
    
    window_icon = Path('./UI/icon_delta.png')
    
    def set_path_to_read(self, new_path: Path):
        self.home = new_path.parent
        self.path_to_save = Path(self.home, self.save_name)
        
        self.path_to_read = new_path
        self.arquivo_original = new_path.name
        
    def check_excel_file(self, str_path: str) -> bool:
        if Path(str_path).suffix != ".xlsx":
            return False
        return True
        

def ler_arquivo(path: Path) -> pl.DataFrame:
    # Lendo arquivo
    dfs = pl.read_excel(
        path,
        engine = "calamine",
        sheet_id = 0
    )
    return dfs

def merge_planilhas(dfs: pl.DataFrame) -> pl.DataFrame:
    # Obtendo colunas
    keys = list(dfs.keys())
    cols = dfs[keys[1]].columns

    # Mesclando planilhas
    dt = pl.DataFrame(schema=dfs[keys[1]].schema)
    for k in keys:
        try:
            df = dfs[k][cols]
            dt = dt.extend(df)
        except pl.exceptions.ColumnNotFoundError:
            None

    return dt

def tratando_dados(dt: pl.DataFrame) -> pl.DataFrame:    
    # Removendo datas vazias
    dt = dt.filter(pl.all_horizontal(pl.col("Data").is_not_null()))

    # Removendo #N/A
    dt = dt.with_columns(
        pl.when(pl.col(pl.String) == "#N/A")
        .then(None)
        .otherwise(pl.col(pl.String))
        .name.keep()
    )
    
    return dt

def get_first_last_date(dt: pl.DataFrame) -> list[datetime]:
    col = dt.select(pl.col("Data"))

    return [col.min()[0,0], col.max()[0,0]]


def filtrando_dados(start_date: datetime, end_date: datetime, tipo_cols: Dict[str, float | str], dt: pl.DataFrame) -> pl.DataFrame:
    # filtra data e por colunas no cols
    result = dt.filter(
        (pl.col("Data") >= start_date) & (pl.col("Data") <= end_date)
    ).select(tipo_cols.keys())

    # alterando o tipo das colunas já selecionadas
    result = result.cast(tipo_cols)
    
    return result

def save_deltav(dt: pl.DataFrame, path_to_save: Path):
    # Salvando o DeltaV em excel
    dt.write_excel(path_to_save)


def read_excel(path_to_read: Path) -> pl.DataFrame:
    # Lendo as colunas que vamos extrair
    df = pl.read_excel(
        path_to_read
    )
    return df


