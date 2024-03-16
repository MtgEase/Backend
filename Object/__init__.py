"""
后端处理需要的对象的管理类

为了保证同步，数据全部实时存储在数据库中，实例属性均为动态加载，而对上层屏蔽这一过程。
"""
from Database import Database
from uuid import UUID


class DatabaseHandler:
    __db = Database()


class Manager(DatabaseHandler):
    """管理并存储实例的静态类"""
    groups = {}
    tags = {}
    users = {}
    rooms = {}
    meetings = {}
    determines = {}

    @staticmethod
    def is_uuid_exist(uuid: str | UUID) -> bool:
        """验证给定的UUID是否已存在"""
        uuid = str(uuid)
        if uuid in Manager.groups:
            return True
        if uuid in Manager.tags:
            return True
        if uuid in Manager.users:
            return True
        if uuid in Manager.rooms:
            return True
        if uuid in Manager.meetings:
            return True
        if uuid in Manager.determines:
            return True
        return False
