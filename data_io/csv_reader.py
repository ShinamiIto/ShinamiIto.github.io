# data_io/csv_reader.py

import pandas as pd

def read_csv(file_path: str, encoding: str = "utf-8", sep: str = ",", **kwargs) -> pd.DataFrame:
    """
    CSVファイル（.csv）を読み込み、DataFrameとして返す。

    Parameters
    ----------
    file_path : str
        読み込むCSVファイルのパス
    encoding : str, default "utf-8"
        ファイルのエンコーディング
    sep : str, default ","
        区切り文字（例: ",", "\t"）
    **kwargs : dict
        pandas.read_csv に渡す追加引数（例: header, usecols, dtype...）

    Returns
    -------
    pd.DataFrame
        読み込んだデータ
    """
    try:
        df = pd.read_csv(file_path, encoding=encoding, sep=sep, **kwargs)
    except Exception as e:
        raise RuntimeError(f"CSVファイルの読み込みに失敗しました: {e}")
    return df
