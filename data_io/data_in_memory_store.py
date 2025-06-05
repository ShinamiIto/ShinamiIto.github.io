# data_io/data_in_memory_store.py

import pandas as pd
from typing import Optional, List

class DataInMemoryStore:
    """
    読み込んだDataFrameをメモリ上で一時的に保持し、名前（キー）で管理する。

    Attributes
    ----------
    _store : dict[str, pd.DataFrame]
        キーとDataFrameを紐付けて格納する内部辞書
    """

    def __init__(self):
        self._store: dict[str, pd.DataFrame] = {}

    def add(self, key: str, df: pd.DataFrame) -> None:
        """
        DataFrameをストアに追加する。

        Parameters
        ----------
        key : str
            DataFrameを参照するためのキー文字列
        df : pd.DataFrame
            ストアに格納するデータ
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("add: dfは pandas.DataFrame である必要があります。")
        self._store[key] = df

    def get(self, key: str) -> Optional[pd.DataFrame]:
        """
        キーに対応するDataFrameを返す。
        存在しない場合は None を返す。

        Parameters
        ----------
        key : str
            取得したいDataFrameのキー

        Returns
        -------
        Optional[pd.DataFrame]
        """
        return self._store.get(key)

    def list_keys(self) -> List[str]:
        """
        現在ストアに格納されているすべてのキーをリストで返す。

        Returns
        -------
        List[str]
        """
        return list(self._store.keys())

    def remove(self, key: str) -> bool:
        """
        指定したキーのDataFrameをストアから削除する。
        削除に成功したら True、それ以外は False を返す。

        Parameters
        ----------
        key : str

        Returns
        -------
        bool
        """
        if key in self._store:
            del self._store[key]
            return True
        return False

    def clear_all(self) -> None:
        """
        ストア内のすべてのDataFrameをクリアする。
        """
        self._store.clear()
