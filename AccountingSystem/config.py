from pathlib import Path

from decouple import config

# 基本設定
BASE_DIR = Path(__file__).resolve().parent.parent

# データベース設定
DB_BASE_DIR = Path.joinpath(BASE_DIR, "sqlite3")
DB_NAME = config("DATABASE_NAME")


if __name__ == "__main__":
    print(BASE_DIR)
    print(DB_BASE_DIR)
    print(DB_NAME)
