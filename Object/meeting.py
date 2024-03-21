"""会议室"""
from datetime import datetime
import json
import uuid as uuid_pkg
from typing import List
from Model import uuid, MeetingStatus
from Object import Manager


class Meeting:
    """会议室"""

    def __init__(self, topic: str, time_start: datetime, time_stop: datetime, room: uuid, created_by: uuid,
                 tip: str | None = None, determine_step: List[str] | None = None):
        self.__db = Manager.db
        while True:
            self.mid = str(uuid_pkg.uuid4())
            if not Manager.is_uuid_exist(self.mid):
                break

        self.__db.insert_data(table='meeting', data={
            'mid': self.mid,
            'topic': topic,
            'time_start': time_start.strftime("%Y-%m-%d %H:%M:%S"),
            'time_stop': time_stop.strftime("%Y-%m-%d %H:%M:%S"),
            'room': room,
            'tip': tip,
            'status': MeetingStatus.Draft,
            'determine_step': json.dumps([] if not determine_step else determine_step),
            'created_by': created_by
        })
        Manager.meetings[self.mid] = self

    def remove(self):
        """删除对象"""
        self.__db.delete_data(table='meetings', condition={'mid': self.mid})
        del Manager.meetings[self.mid]

    @property
    def topic(self) -> str:
        return self.__db.select_data(table='meetings', columns=['topic'], condition={'mid': self.mid})[0][0]

    @topic.setter
    def topic(self, value: str) -> None:
        self.__db.update_data(table='meetings', data={'topic': value}, condition={'mid': self.mid})

    @property
    def time_start(self) -> datetime:
        return self.__db.select_data(table='meetings', columns=['time_start'], condition={'mid': self.mid})[0][0]

    @time_start.setter
    def time_start(self, value: datetime) -> None:
        self.__db.update_data(table='meetings', data={'time_start': value.strftime("%Y-%m-%d %H:%M:%S")},
                              condition={'mid': self.mid})

    @property
    def time_stop(self) -> datetime:
        return self.__db.select_data(table='meetings', columns=['time_stop'], condition={'mid': self.mid})[0][0]

    @time_stop.setter
    def time_stop(self, value: datetime) -> None:
        self.__db.update_data(table='meetings', data={'time_stop': value.strftime("%Y-%m-%d %H:%M:%S")},
                              condition={'mid': self.mid})

    @property
    def room(self) -> uuid:
        return self.__db.select_data(table='meetings', columns=['room'], condition={'mid': self.mid})[0][0]

    @room.setter
    def room(self, value: uuid) -> None:
        self.__db.update_data(table='meetings', data={'room': value}, condition={'mid': self.mid})

    @property
    def tip(self) -> str | None:
        return self.__db.select_data(table='meetings', columns=['tip'], condition={'mid': self.mid})[0][0]

    @tip.setter
    def tip(self, value: str | None) -> None:
        self.__db.update_data(table='meetings', data={'tip': value}, condition={'mid': self.mid})

    @property
    def status(self) -> MeetingStatus:
        return self.__db.select_data(table='meetings', columns=['status'], condition={'mid': self.mid})[0][0]

    @status.setter
    def status(self, value: MeetingStatus) -> None:
        self.__db.update_data(table='meetings', data={'status': value}, condition={'mid': self.mid})

    @property
    def determine_step(self) -> List[str]:
        return json.loads(
            self.__db.select_data(table='meetings', columns=['status'], condition={'mid': self.mid})[0][0]
        )

    def determine_step_append(self, step: str) -> None:
        steps = self.determine_step
        steps.append(step)
        self.__db.update_data(table='meetings', data={'status': json.dumps(steps)}, condition={'mid': self.mid})

    @property
    def created_by(self) -> uuid:
        return self.__db.select_data(table='meetings', columns=['created_by'], condition={'mid': self.mid})[0][0]
