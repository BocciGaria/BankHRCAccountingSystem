from pathlib import Path

from decouple import config

# 基本設定
BASE_DIR = Path(__file__).resolve().parent.parent

# データベース設定
DB_BASE_DIR = Path.joinpath(BASE_DIR, config("DATABSE_DIR"))
DB_NAME = config("DATABASE_NAME_ACCOUNTING_SYSTEM")
DB_PATH = Path.joinpath(DB_BASE_DIR, DB_NAME)


if __name__ == "__main__":
    print(BASE_DIR)
    print(DB_BASE_DIR)
    print(DB_NAME)
