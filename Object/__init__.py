"""
后端处理需要的对象的管理类

为了保证同步，数据全部实时存储在数据库中，实例属性均为动态加载，而对上层屏蔽这一过程。
"""
from typing import Dict
from Database import Database
import uuid as uuid_pkg
from Model import uuid
from .determine import Determine
from .group import Group
from .meeting import Meeting
from .room import Room
from .tag import Tag
from .user import User


class Manager:
    """管理并存储实例的静态类"""
    db = Database()
    groups: Dict[uuid, Group] = {}
    tags: Dict[uuid, Tag] = {}
    users: Dict[uuid, User] = {}
    rooms: Dict[uuid, Room] = {}
    meetings: Dict[uuid, Meeting] = {}
    determines: Dict[uuid, Determine] = {}

    @staticmethod
    def is_uuid_exist(item_id: str | uuid_pkg.UUID) -> bool:
        """验证给定的UUID是否已存在"""
        item_id = str(item_id)
        if item_id in Manager.groups:
            return True
        if item_id in Manager.tags:
            return True
        if item_id in Manager.users:
            return True
        if item_id in Manager.rooms:
            return True
        if item_id in Manager.meetings:
            return True
        if item_id in Manager.determines:
            return True
        return False
