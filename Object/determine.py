"""审批"""
import uuid as uuid_pkg
import Object
from Model import uuid
from Object import Manager


class Determine:
    """审批"""

    @staticmethod
    def create(item_id: uuid, is_meeting: bool = True) -> Object.Determine:
        while True:
            did = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(did):
                break
        Manager.db.insert_data(table='determine', data={
            'did': did,
            'is_meeting': is_meeting,
            'id': item_id
        })
        return Determine(did)

    @staticmethod
    def load(did: uuid) -> Object.Determine:
        return Determine(did)

    def __init__(self, did: uuid):
        self.__db = Manager.db
        self.did = did
        Manager.determines[self.did] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='determine', condition={'did': self.did})
        del Manager.determines[self.did]

    @property
    def is_meeting(self) -> bool:
        data = self.__db.select_data(table='determine', columns=['is_meeting'], condition={'did': self.did})[0][0]
        return data == b'\x01'

    @property
    def id(self) -> uuid:
        return self.__db.select_data(table='determine', columns=['id'], condition={'did': self.did})[0][0]
