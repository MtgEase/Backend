"""用户组"""
import json
import uuid as uuid_pkg
from typing import List
from Model import Permission
from Object import Manager


class Group:
    """用户组"""

    def __init__(self, name: str, belong_to: str, permissions: List[Permission], targets: List[str]):
        self.__db = Manager.db
        while True:
            self.gid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.gid):
                break

        self.__db.insert_data(table='group', data={
            'gid': self.gid,
            'name': name,
            'belong_to': belong_to,
            'permissions': json.dumps(permissions),
            'targets': json.dumps(targets)
        })
        Manager.groups[self.gid] = self

    @property
    def name(self) -> str:
        return self.__db.select_data(table='group', columns=['name'], condition={'gid': self.gid})[0][0]

    @name.setter
    def name(self, value: str) -> None:
        self.__db.update_data(table='group', data={'name': value}, condition={'gid': self.gid})

    @property
    def belong_to(self) -> str:
        return self.__db.select_data(table='group', columns=['belong_to'], condition={'gid': self.gid})[0][0]

    @belong_to.setter
    def belong_to(self, value: str) -> None:
        self.__db.update_data(table='group', data={'belong_to': value}, condition={'gid': self.gid})

    @property
    def permissions(self) -> List[Permission]:
        data = self.__db.select_data(table='group', columns=['permissions'], condition={'gid': self.gid})[0][0]
        return json.loads(data)

    @permissions.setter
    def permissions(self, value: List[Permission]) -> None:
        data = json.dumps(value)
        self.__db.update_data(table='group', data={'permissions': data}, condition={'gid': self.gid})

    @property
    def targets(self) -> List[str]:
        data = self.__db.select_data(table='group', columns=['targets'], condition={'gid': self.gid})[0][0]
        return json.loads(data)

    @targets.setter
    def targets(self, value: List[str]) -> None:
        data = json.dumps(value)
        self.__db.update_data(table='group', data={'targets': data}, condition={'gid': self.gid})
