"""标签"""
from datetime import datetime
import json
import uuid as uuid_pkg
from typing import List
from Model import Permission, uuid
from Object import Manager


class Tag:
    """ 标签"""

    def __init__(self, name: str, permissions: List[Permission], targets: List[str], created_by: uuid,
                 expire: datetime | None = None):
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
            'expire': expire.strftime("%Y-%m-%d %H:%M:%S") if expire else None,
            'created_by': created_by
        })
        Manager.tags[self.tid] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='tag', condition={'tid': self.tid})
        del Manager.tags[self.tid]

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

    def permissions_append(self, permission: Permission) -> None:
        data = self.permissions
        data.append(permission)
        data = json.dumps(data)
        self.__db.update_data(table='tag', data={'permissions': data}, condition={'tid': self.tid})

    def permissions_remove(self, permission: Permission) -> None:
        data = self.permissions
        data.remove(permission)
        data = json.dumps(data)
        self.__db.update_data(table='tag', data={'permissions': data}, condition={'tid': self.tid})

    @property
    def targets(self) -> List[uuid]:
        data = self.__db.select_data(table='tag', columns=['targets'], condition={'tid': self.tid})[0][0]
        return json.loads(data)

    def targets_append(self, target: uuid) -> None:
        data = self.targets
        data.append(target)
        data = json.dumps(data)
        self.__db.update_data(table='tag', data={'targets': data}, condition={'tid': self.tid})

    def targets_remove(self, target: uuid) -> None:
        data = self.targets
        data.remove(target)
        data = json.dumps(data)
        self.__db.update_data(table='tag', data={'targets': data}, condition={'tid': self.tid})

    @property
    def expire(self) -> datetime | None:
        data = self.__db.select_data(table='tag', columns=['expire'], condition={'tid': self.tid})[0][0]
        return data

    @expire.setter
    def expire(self, value: datetime | None) -> None:
        data = value.strftime("%Y-%m-%d %H:%M:%S") if value else None
        self.__db.update_data(table='tag', data={'expire': data}, condition={'tid': self.tid})

    @property
    def created_by(self) -> uuid:
        return self.__db.select_data(table='tag', columns=['created_by'], condition={'tid': self.tid})[0][0]
