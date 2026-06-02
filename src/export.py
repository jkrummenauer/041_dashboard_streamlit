# src/export.py

import io

import pandas as pd


def converter_df_para_excel(dfs: dict[str, pd.DataFrame]) -> bytes:
    """
    Converte um ou mais DataFrames para um arquivo Excel em memória.
    """

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for nome_aba, df in dfs.items():
            nome_aba_seguro = nome_aba[:31]
            df.to_excel(
                writer,
                index=False,
                sheet_name=nome_aba_seguro,
            )

    return output.getvalue()