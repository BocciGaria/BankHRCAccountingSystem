import sqlite3

from ...entity.base import ITableEntity
from ..operator import BaseOperator


class Sqlite3Operator(BaseOperator):
    """Database operator for SQLite3"""

    def __init__(self, connection_string: str) -> None:
        super().__init__(connection_string)

    def get_all(self, entity_type: ITableEntity):
        connection = sqlite3.connect(self.connection_string)
        cursor = connection.cursor()
        sql = f"SELECT * FROM {entity_type.table_name}"
        result = cursor.execute(sql)
        return result.fetchall()

    def get_for_primary_key(self, entity_type: ITableEntity):
        raise NotImplementedError()
