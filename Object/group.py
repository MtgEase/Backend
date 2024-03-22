"""用户组"""
import json
import uuid as uuid_pkg
from typing import List
from Model import Permission, uuid
from .manager import Manager


class Group:
    """用户组"""

    @staticmethod
    def create(name: str, belong_to: uuid, permissions: List[Permission]):
        """创建实例"""
        while True:
            gid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(gid):
                break
        Manager.db.insert_data(table='group', data={
            'gid': gid,
            'name': name,
            'belong_to': belong_to,
            'permissions': json.dumps(permissions)
        })
        return Group(gid)

    @staticmethod
    def load(gid: uuid):
        """加载实例"""
        return Group(gid)

    @staticmethod
    def load_all():
        """加载全部实例"""
        for gid in [item[0] for item in Manager.db.select_data(table='group', columns=['gid'])]:
            Group.load(gid)

    def __init__(self, gid: uuid):
        self.__db = Manager.db
        self.gid = gid
        Manager.groups[self.gid] = self

    def remove(self):
        """删除实例"""
        self.__db.delete_data(table='group', condition={'gid': self.gid})
        del Manager.groups[self.gid]

    @property
    def name(self) -> str:
        return self.__db.select_data(table='group', columns=['name'], condition={'gid': self.gid})[0][0]

    @name.setter
    def name(self, value: str) -> None:
        self.__db.update_data(table='group', data={'name': value}, condition={'gid': self.gid})

    @property
    def belong_to(self) -> uuid:
        return self.__db.select_data(table='group', columns=['belong_to'], condition={'gid': self.gid})[0][0]

    @belong_to.setter
    def belong_to(self, value: uuid) -> None:
        self.__db.update_data(table='group', data={'belong_to': value}, condition={'gid': self.gid})

    @property
    def permissions(self) -> List[Permission]:
        data = self.__db.select_data(table='group', columns=['permissions'], condition={'gid': self.gid})[0][0]
        return json.loads(data)

    def permissions_append(self, permission: Permission) -> None:
        data = self.permissions
        data.append(permission)
        data = json.dumps(data)
        self.__db.update_data(table='group', data={'permissions': data}, condition={'gid': self.gid})

    def permissions_remove(self, permission: Permission) -> None:
        data = self.permissions
        data.remove(permission)
        data = json.dumps(data)
        self.__db.update_data(table='group', data={'permissions': data}, condition={'gid': self.gid})

    @property
    def targets(self) -> List[uuid]:
        data = self.__db.select_data(table='group', columns=['targets'], condition={'gid': self.gid})[0][0]
        return json.loads(data)

    def targets_append(self, target: uuid) -> None:
        data = self.targets
        data.append(target)
        data = json.dumps(data)
        self.__db.update_data(table='group', data={'targets': data}, condition={'gid': self.gid})

    def targets_remove(self, target: uuid) -> None:
        data = self.targets
        data.remove(target)
        data = json.dumps(data)
        self.__db.update_data(table='group', data={'targets': data}, condition={'gid': self.gid})
