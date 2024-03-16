"""
后端处理需要的对象的管理类

为了保证同步，数据全部实时存储在数据库中，实例属性均为动态加载，而对上层屏蔽这一过程。
"""
from Database import Database


class Object:
    """管理并存储实例的静态类"""
    __db = Database()
    groups = {}
    tags = {}
    users = {}
    rooms = {}
    meetings = {}
    determines = {}
