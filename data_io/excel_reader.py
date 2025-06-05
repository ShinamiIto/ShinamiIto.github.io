# data_io/excel_reader.py

import pandas as pd

def read_excel(file_path: str, sheet_name=None, **kwargs) -> pd.DataFrame:
    """
    Excelファイル（.xlsx, .xls）を読み込み、DataFrameとして返す。
    
    Parameters
    ----------
    file_path : str
        読み込むExcelファイルのパス
    sheet_name : str or int or list[str] or None
        読み込むシート名 or シート番号。Noneなら全シートを辞書形式で返す。
    **kwargs : dict
        pandas.read_excel に渡す追加引数（例: header, usecols, dtype...）

    Returns
    -------
    pd.DataFrame
        読み込んだデータ。sheet_name=None の場合は dict[str, DataFrame] を返す。
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, **kwargs)
    except Exception as e:
        raise RuntimeError(f"Excelファイルの読み込みに失敗しました: {e}")
    return df
