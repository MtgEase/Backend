"""会议室"""
import json
import uuid as uuid_pkg
from typing import List
from Model import uuid
from Object import Manager


class Room:
    """会议室"""

    def __init__(self, name: str, position: str, tip: str | None = None, available: bool = True,
                 capacity: int | None = None, devices: List[str] | None = None, rest: list[str] | None = None):
        self.__db = Manager.db
        while True:
            self.rid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.rid):
                break

        self.__db.insert_data(table='room', data={
            'rid': self.rid,
            'name': name,
            'position': position,
            'tip': tip,
            'available': available,
            'capacity': capacity,
            'devices': devices,
            'rest': rest
        })
        Manager.rooms[self.rid] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='room', condition={'rid': self.rid})
        del Manager.rooms[self.rid]

    @property
    def name(self) -> str:
        return self.__db.select_data(table='room', columns=['name'], condition={'rid': self.rid})[0][0]

    @name.setter
    def name(self, value: str) -> None:
        self.__db.update_data(table='room', data={'name': value}, condition={'rid': self.rid})

    @property
    def position(self) -> str:
        return self.__db.select_data(table='room', columns=['position'], condition={'rid': self.rid})[0][0]

    @position.setter
    def position(self, value: str) -> None:
        self.__db.update_data(table='room', data={'position': value}, condition={'rid': self.rid})

    @property
    def tip(self) -> str | None:
        return self.__db.select_data(table='room', columns=['tip'], condition={'rid': self.rid})[0][0]

    @tip.setter
    def tip(self, value: str | None) -> None:
        self.__db.update_data(table='room', data={'tip': value}, condition={'rid': self.rid})

    @property
    def available(self) -> bool:
        data = self.__db.select_data(table='room', columns=['available'], condition={'rid': self.rid})[0][0]
        return data == b'\x01'

    @available.setter
    def available(self, value: bool) -> None:
        self.__db.update_data(table='room', data={'available': value}, condition={'rid': self.rid})

    @property
    def capacity(self) -> int | None:
        return self.__db.select_data(table='room', columns=['capacity'], condition={'rid': self.rid})[0][0]

    @capacity.setter
    def capacity(self, value: int | None) -> None:
        self.__db.update_data(table='room', data={'capacity': value}, condition={'rid': self.rid})

    @property
    def devices(self) -> List[str] | None:
        data = self.__db.select_data(table='room', columns=['devices'], condition={'rid': self.rid})[0][0]
        if data:
            return json.loads(data)
        else:
            return None

    def devices_append(self, device: str) -> None:
        data = self.devices
        if not data:
            data = []
        data.append(device)
        data = json.dumps(data)
        self.__db.update_data(table='room', data={'devices': data}, condition={'rid': self.rid})

    def devices_remove(self, device: str) -> None:
        data = self.devices
        data.remove(device)
        if len(data) != 0:
            data = json.dumps(data)
        else:
            data = None
        self.__db.update_data(table='room', data={'devices': data}, condition={'rid': self.rid})

    @property
    def rest(self) -> List[str] | None:
        data = self.__db.select_data(table='room', columns=['rest'], condition={'rid': self.rid})[0][0]
        if not data:
            return None
        else:
            return json.loads(data)

    @rest.setter
    def rest(self, value: List[str] | None) -> None:
        if value:
            self.__db.update_data(table='room', data={'rest': json.dumps(value)}, condition={'rid': self.rid})
        else:
            self.__db.update_data(table='room', data={'rest': None}, condition={'rid': self.rid})

    @property
    def meetings(self) -> List[uuid]:
        data = []
        for mid, meeting in Manager.meetings.items():
            if meeting.room == self.rid:
                data.append(mid)
        return data
