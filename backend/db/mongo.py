from pymongo import MongoClient
from flask import current_app

_client = None  # 全域只建立一次連線

def get_client():
    """
    建立或取得 MongoClient（單例）
    """
    global _client
    if _client is None:
        uri = current_app.config["MONGO_URI"]
        _client = MongoClient(uri)
    return _client


def get_db():
    """
    取得目前設定的資料庫
    """
    db_name = current_app.config["MONGO_DB_NAME"]
    return get_client()[db_name]


def col(name: str):
    """
    取得指定 collection
    用法：col("users")
    """
    return get_db()[name]