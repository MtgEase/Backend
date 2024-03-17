"""审批"""
import uuid as uuid_pkg
from Model import uuid
from Object import Manager


class Determine:
    """审批"""

    def __init__(self, item_id: uuid, is_meeting: bool = True):
        self.__db = Manager.db
        while True:
            self.did = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.did):
                break

        self.__db.insert_data(table='determine', data={
            'did': self.did,
            'is_meeting': is_meeting,
            'id': item_id
        })
        Manager.determines[self.did] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='determine', condition={'did': self.did})
        del Manager.determines[self.did]

    @property
    def is_meeting(self) -> bool:
        return self.__db.select_data(table='determine', columns=['is_meeting'], condition={'did': self.did})[0][0]

    @is_meeting.setter
    def is_meeting(self, value: bool) -> None:
        self.__db.update_data(table='determine', data={'is_meeting': value}, condition={'did': self.did})

    @property
    def id(self) -> uuid:
        return self.__db.select_data(table='determine', columns=['id'], condition={'did': self.did})[0][0]

    @id.setter
    def id(self, value: id) -> None:
        self.__db.update_data(table='determine', data={'id': value}, condition={'did': self.did})
