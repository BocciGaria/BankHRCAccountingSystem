from pathlib import Path

from decouple import config

from .const import *

# 基本設定
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent

# データベース設定
DB = SQLITE3
DB_CONNECTION_STRING = config("DATABASE_CONNECTION_STRING")

# コンテンツフォルダ
CONTENT_DIR = Path.joinpath(APP_DIR, "content")
# 画像フォルダ
IMAGE_DIR = Path.joinpath(CONTENT_DIR, "image")


def get_image_path(image_name):
    return Path.joinpath(IMAGE_DIR, image_name)
