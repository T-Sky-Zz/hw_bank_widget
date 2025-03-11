# import os
from typing import Any

import pandas as pd


def get_transactions_csv(file_path: str) -> Any:
    """Функция, которая считывает данные из файла CSV и преобразовывает в список словарей"""

    file_reader = pd.read_csv(file_path, delimiter=";")
    file_reader["id"] = file_reader["id"].fillna(0).astype(int)
    file_reader_dict = file_reader.to_dict(orient="records")
    return file_reader_dict


def get_transactions_excel(file_path: str) -> Any:
    """Функция, которая считывает данные из файла EXCEL и преобразовывает в список словарей"""

    file_reader = pd.read_excel(file_path)
    file_reader["id"] = file_reader["id"].fillna(0).astype(int)
    file_reader_dict = file_reader.to_dict(orient="records")
    return file_reader_dict


# if __name__ == "__main__":
#     path_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
#     reader_df_csv = get_transactions_csv(path_csv)
#     print(reader_df_csv)
#     print(type(reader_df_csv))
#
#
# if __name__ == "__main__":
#     path_excel = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
#     reader_df_xlsx = get_transactions_excel(path_excel)
#     print(reader_df_xlsx)
#     print(type(reader_df_xlsx))
