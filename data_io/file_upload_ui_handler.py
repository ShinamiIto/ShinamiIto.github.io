# data_io/file_upload_ui_handler.py

import streamlit as st
from typing import Optional

def upload_file(
    label: str = "データファイルをアップロードしてください",
    accepted_types: list[str] = ["xlsx", "xls", "csv"]
) -> Optional[st.runtime.uploaded_file_manager.UploadedFile]:
    """
    Streamlit のファイルアップローダーを表示し、ユーザーがアップロードしたファイルオブジェクトを返す。

    Parameters
    ----------
    label : str, default "データファイルをアップロードしてください"
        Streamlit 上のラベル（説明文）
    accepted_types : list[str], default ["xlsx", "xls", "csv"]
        受け付ける拡張子リスト

    Returns
    -------
    Optional[UploadedFile]
        アップロードされたファイルオブジェクト。未アップロードの場合は None。
    """
    uploaded = st.file_uploader(label, type=accepted_types)
    return uploaded
