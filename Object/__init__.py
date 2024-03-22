"""
后端处理需要的对象的管理类

为了保证同步，数据全部实时存储在数据库中，实例属性均为动态加载，而对上层屏蔽这一过程。
"""
from .determine import Determine
from .group import Group
from .meeting import Meeting
from .room import Room
from .tag import Tag
from .user import User
from .manager import Manager

Determine.load_all()
Group.load_all()
Meeting.load_all()
Room.load_all()
Tag.load_all()
User.load_all()
