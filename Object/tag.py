"""标签"""
from datetime import datetime
import json
import uuid as uuid_pkg
from typing import List
from Model import Permission, uuid
from Object import Manager


class Tag:
    """用户组"""

    def __init__(self, name: str, permissions: List[Permission], targets: List[str],
                 expire: datetime, created_by: uuid):
        self.__db = Manager.db
        while True:
            self.tid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.tid):
                break

        self.__db.insert_data(table='tag', data={
            'tid': self.tid,
            'name': name,
            'permissions': json.dumps(permissions),
            'targets': json.dumps(targets),
            'expire': expire.strftime("%Y-%m-%d %H:%M:%S"),
            'created_by': created_by
        })
        Manager.groups[self.tid] = self

    @property
    def name(self) -> str:
        return self.__db.select_data(table='tag', columns=['name'], condition={'tid': self.tid})[0][0]

    @name.setter
    def name(self, value: str) -> None:
        self.__db.update_data(table='tag', data={'name': value}, condition={'tid': self.tid})

    @property
    def permissions(self) -> List[Permission]:
        data = self.__db.select_data(table='tag', columns=['permissions'], condition={'tid': self.tid})[0][0]
        return json.loads(data)

    @permissions.setter
    def permissions(self, value: List[Permission]) -> None:
        data = json.dumps(value)
        self.__db.update_data(table='tag', data={'permissions': data}, condition={'tid': self.tid})

    @property
    def targets(self) -> List[uuid]:
        data = self.__db.select_data(table='tag', columns=['targets'], condition={'tid': self.tid})[0][0]
        return json.loads(data)

    @targets.setter
    def targets(self, value: List[uuid]) -> None:
        data = json.dumps(value)
        self.__db.update_data(table='tag', data={'targets': data}, condition={'tid': self.tid})

    @property
    def expire(self) -> datetime:
        data = self.__db.select_data(table='tag', columns=['expire'], condition={'tid': self.tid})[0][0]
        return data

    @expire.setter
    def expire(self, value: datetime) -> None:
        data = value.strftime("%Y-%m-%d %H:%M:%S")
        self.__db.update_data(table='tag', data={'expire': data}, condition={'tid': self.tid})

    @property
    def created_by(self) -> uuid:
        return self.__db.select_data(table='tag', columns=['created_by'], condition={'tid': self.tid})[0][0]

    @created_by.setter
    def created_by(self, value: uuid) -> None:
        self.__db.update_data(table='tag', data={'created_by': value}, condition={'tid': self.tid})
