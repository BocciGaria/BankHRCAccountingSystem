import sqlite3
from typing import *

from ...entity.base import ITableEntity
from ..operator import BaseOperator


class Sqlite3Operator(BaseOperator):
    """Database operator for SQLite3"""

    def __init__(self, connection_string: str) -> None:
        super().__init__(connection_string)

    def get_all(self, entity_type: Type[ITableEntity]) -> Iterable[ITableEntity]:
        connection = sqlite3.connect(self.connection_string)
        cursor = connection.cursor()
        sql = f"SELECT * FROM {entity_type.table_name}"
        query_result = cursor.execute(sql)
        result = list()
        for record in query_result.fetchall():
            entity = entity_type()
            index = 0
            for field in entity.fields.values():
                field.set_value(record[index])
                index += 1
            result.append(entity)
        return result

    def get_for_primary_key(self, entity_type: Type[ITableEntity]) -> ITableEntity:
        raise NotImplementedError()

    def save(self, entity: ITableEntity) -> None:
        raise NotImplementedError()
