# data_io/existing_data_selection_ui_handler.py

import streamlit as st
import os
from typing import Optional

def select_existing_dataset(
    data_dir: str = "data",
    label: str = "既存のデータセットを選択してください"
) -> Optional[str]:
    """
    永続化フォルダ（data_dir）に保存されているファイルを一覧表示し、
    Streamlit の selectbox でユーザーに選択させる。
    選択されたファイルのフルパスを返す。

    Parameters
    ----------
    data_dir : str, default "data"
        永続化ファイルが置かれているディレクトリ
    label : str, default "既存のデータセットを選択してください"
        Streamlit の selectbox に表示するラベル

    Returns
    -------
    Optional[str]
        選択されたファイルのフルパス。選択がなければ None。
    """
    # ディレクトリが存在しない場合は None を返す
    if not os.path.exists(data_dir):
        st.info(f"ディレクトリ '{data_dir}' が存在しません。")
        return None

    # ディレクトリ内のファイル一覧を取得
    files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    if not files:
        st.info("保存されているデータが見つかりません。")
        return None

    # Streamlit の selectbox でリスト表示
    selected_filename = st.selectbox(label, files)
    full_path = os.path.join(data_dir, selected_filename)
    return full_path

