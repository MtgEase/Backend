from Database import Database
import uuid as uuid_pkg
from Model import uuid


class Manager:
    """管理并存储实例的静态类"""
    # 数据库连接对象
    db = Database()
    # 存储已有的实例的列表
    groups = {}
    tags = {}
    users = {}
    rooms = {}
    meetings = {}
    determines = {}
    # 取消注释下面这些代码可以使编辑器支持类型提示，但由于架构问题会导致运行时的循环导入问题
    # from typing import Dict
    # from Object import Group, Tag, User, Room, Meeting, Determine
    # groups: Dict[uuid, Group] = {}
    # tags: Dict[uuid, Tag] = {}
    # users: Dict[uuid, User] = {}
    # rooms: Dict[uuid, Room] = {}
    # meetings: Dict[uuid, Meeting] = {}
    # determines: Dict[uuid, Determine] = {}

    @staticmethod
    def is_uuid_exist(item_id: uuid | uuid_pkg.UUID) -> bool:
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
