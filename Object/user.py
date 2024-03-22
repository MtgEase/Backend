"""用户"""
import hashlib
import os
import uuid as uuid_pkg
from typing import List
from typing import Tuple
from Model import uuid
from Object import Manager


class User:
    """用户"""

    @staticmethod
    def hash_passwd(passwd: str, salt: str | None = None) -> Tuple[str, str]:
        if salt:
            salt = bytes.fromhex(salt)
        else:
            salt = os.urandom(16)
        hashed_passwd = hashlib.sha256(salt + passwd.encode('utf-8')).hexdigest()
        return hashed_passwd, salt.hex()

    @staticmethod
    def verify_passwd(password: str, hashed_passwd: str, salt: str) -> bool:
        salt = bytes.fromhex(salt)
        return hashlib.sha256(salt + password.encode('utf-8')).hexdigest() == hashed_passwd

    def __init__(self, name: str, group: uuid, email: str | None = None, wxid: str | None = None,
                 passwd: str | None = None):
        assert not (wxid is None and passwd is None)
        self.__db = Manager.db
        while True:
            self.uid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.uid):
                break

        __salt = os.urandom(16).hex()
        self.__db.insert_data(table='user', data={
            'uid': self.uid,
            'name': name,
            'email': email,
            'wxid': wxid,
            'hashed_passwd': User.hash_passwd(passwd, __salt) if passwd else None,
            'salt': __salt,
            'group': group
        })
        Manager.users[self.uid] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='user', condition={'uid': self.uid})
        del Manager.users[self.uid]

    @property
    def name(self) -> str:
        return self.__db.select_data(table='user', columns=['name'], condition={'uid': self.uid})[0][0]

    @name.setter
    def name(self, value: str) -> None:
        self.__db.update_data(table='user', data={'name': value}, condition={'uid': self.uid})

    @property
    def email(self) -> str | None:
        return self.__db.select_data(table='user', columns=['email'], condition={'uid': self.uid})[0][0]

    @email.setter
    def email(self, value: str | None) -> None:
        self.__db.update_data(table='user', data={'email': value}, condition={'uid': self.uid})

    @property
    def wxid(self) -> str | None:
        return self.__db.select_data(table='user', columns=['wxid'], condition={'uid': self.uid})[0][0]

    @wxid.setter
    def wxid(self, value: str | None) -> None:
        self.__db.update_data(table='user', data={'wxid': value}, condition={'uid': self.uid})

    def verify_user_passwd(self, passwd: str) -> bool:
        hashed_passwd = self.__db.select_data(table='user', columns=['hashed_passwd'],
                                              condition={'uid': self.uid})[0][0]
        if not hashed_passwd:
            return False
        salt = self.__db.select_data(table='user', columns=['salt'], condition={'uid': self.uid})[0][0]
        return User.verify_passwd(passwd, hashed_passwd, salt)

    def update_passwd(self, old_passwd: str, new_passwd: str) -> bool:
        if self.verify_user_passwd(old_passwd):
            salt = self.__db.select_data(table='user', columns=['salt'], condition={'uid': self.uid})[0][0]
            hashed_passwd = User.hash_passwd(new_passwd, salt)
            self.__db.update_data(table='user', data={'hashed_passwd': hashed_passwd}, condition={'uid': self.uid})
            return True
        else:
            return False

    @property
    def meetings(self) -> List[uuid]:
        meetings = []
        for mid, meeting in Manager.meetings.items():
            if meeting.created_by == self.uid:
                meetings.append(mid)
        return meetings

    @property
    def group(self) -> uuid:
        return self.__db.select_data(table='user', columns=['group'], condition={'uid': self.uid})[0][0]

    @group.setter
    def group(self, value: uuid) -> None:
        self.__db.update_data(table='user', data={'group': value}, condition={'uid': self.uid})

    @property
    def tags(self) -> List[uuid]:
        tags = []
        for tid, tag in Manager.tags.items():
            if self.uid in tag.targets:
                tags.append(tid)
        return tags

    def tag_append(self, tid: uuid) -> None:
        Manager.tags[tid].targets_append(self.uid)

    def tag_remove(self, tid: uuid) -> None:
        Manager.tags[tid].targets_remove(self.uid)

    @property
    def permissions(self) -> List[uuid]:
        permissions = []
        permissions.extend(Manager.groups[self.group].permissions)
        for tid, tag in Manager.tags.items():
            if self.uid in tag.targets:
                permissions.extend(tag.permissions)
        return permissions
