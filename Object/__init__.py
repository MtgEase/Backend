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
    # 数据库连接对象
    db = Database()
    # 存储已有的实例的列表
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

    @staticmethod
    def load_objects():
        """从数据库中读取已有的实例"""
        dids = [item[0] for item in Manager.db.select_data(table='determine', columns=['did'])]
        for did in dids:
            Determine.load(did)
        gids = [item[0] for item in Manager.db.select_data(table='group', columns=['gid'])]
        for gid in gids:
            Group.load(gid)
        mids = [item[0] for item in Manager.db.select_data(table='meeting', columns=['mid'])]
        for mid in mids:
            Meeting.load(mid)
        rids = [item[0] for item in Manager.db.select_data(table='room', columns=['rid'])]
        for rid in rids:
            Room.load(rid)
        tids = [item[0] for item in Manager.db.select_data(table='tag', columns=['tid'])]
        for tid in tids:
            Tag.load(tid)
        uids = [item[0] for item in Manager.db.select_data(table='user', columns=['uid'])]
        for uid in uids:
            User.load(uid)


Manager.load_objects()
