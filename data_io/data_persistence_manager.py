# data_io/data_persistence_manager.py

import os
import pandas as pd
from typing import List

class DataPersistenceManager:
    """
    データの永続化を担当する。ローカルフォルダに CSV / Excel / Pickle などで保存・読み込みを行う。

    Attributes
    ----------
    base_dir : str
        永続化用ディレクトリのパス
    """

    def __init__(self, base_dir: str = "data"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save(
        self,
        key: str,
        df: pd.DataFrame,
        file_format: str = "csv"
    ) -> str:
        """
        DataFrame を指定の形式で保存する。

        Parameters
        ----------
        key : str
            保存時のファイル名のベース（拡張子なし）
        df : pd.DataFrame
            保存する DataFrame
        file_format : str, default "csv"
            保存形式: "csv", "xlsx", "xls", "pickle" のいずれか

        Returns
        -------
        str
            保存先のフルパス
        """
        supported = ["csv", "xlsx", "xls", "pickle"]
        if file_format not in supported:
            raise ValueError(f"Unsupported format: {file_format}. Supported = {supported}")

        filename = f"{key}.{file_format}"
        filepath = os.path.join(self.base_dir, filename)

        if file_format == "csv":
            df.to_csv(filepath, index=False)
        elif file_format in ("xlsx", "xls"):
            df.to_excel(filepath, index=False)
        elif file_format == "pickle":
            df.to_pickle(filepath)

        return filepath

    def load(
        self,
        key: str,
        file_format: str = "csv"
    ) -> pd.DataFrame:
        """
        保存されているファイルを読み込み、DataFrame として返す。

        Parameters
        ----------
        key : str
            読み込み元ファイル名のベース（拡張子なし）
        file_format : str, default "csv"
            読み込み形式: "csv", "xlsx", "xls", "pickle" のいずれか

        Returns
        -------
        pd.DataFrame
        """
        filename = f"{key}.{file_format}"
        filepath = os.path.join(self.base_dir, filename)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"[{filepath}] が存在しません。")

        if file_format == "csv":
            return pd.read_csv(filepath)
        elif file_format in ("xlsx", "xls"):
            return pd.read_excel(filepath)
        elif file_format == "pickle":
            return pd.read_pickle(filepath)
        else:
            # ここには来ない想定
            raise ValueError(f"Unsupported format: {file_format}")

    def list_files(self) -> List[str]:
        """
        永続化ディレクトリ内のすべてのファイル名をリストで返す。

        Returns
        -------
        List[str]
        """
        return [f for f in os.listdir(self.base_dir) if os.path.isfile(os.path.join(self.base_dir, f))]
