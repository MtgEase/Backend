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
