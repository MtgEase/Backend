"""与会易约存储后端交互的模块"""
import yaml


class Database:
    """
    通用存储后端交互的基类。
    此类封装了对存储后端的增删改查功能。
    任何对存储后端的操作对象都应该将此类作为基类以实现解耦。
    """
    # db存储了实际的存储后端驱动的对象
    db = None
    # 存储后端需要有以下表结构
    tables = {
        'user': ['uid', 'name', 'email', 'wxid', 'hashed_password'],
        'group': ['gid', 'name', 'level', 'permissions', 'targets'],
        'determine': ['did', 'is_meeting', 'id'],
        'meeting': ['mid', 'topic', 'time_start', 'time_stop', 'room', 'tip', 'status', 'determine_step', 'created_by'],
        'room': ['rid', 'name', 'position', 'tip', 'available', 'capacity', 'devices', 'rest'],
        'tag': ['tid', 'name', 'permissions', 'targets', 'expire', 'created_by']
    }

    def __init__(self):
        # 存储后端驱动应实现增删改查的功能
        self.insert_data = Database.db.insert_data
        self.select_data = Database.db.select_data
        self.delete_data = Database.db.delete_data
        self.update_data = Database.db.update_data


# 读取配置文件的Database键值
with open('config.yaml') as __f:
    __config: dict = yaml.safe_load(__f)['Database']
    __driver: str = __config['Driver']
    __args: dict = __config['DriverArgs']
# 使用exec函数，拼接从配置文件读取到的驱动名并执行，获取到驱动后端对象
__global_vars: dict = {}
exec(f'from Database.StorageDriver.{__driver}.{__driver} import {__driver};'
     f'db = {__driver}(**{str(__args)})', __global_vars)
# 保存实际的对象到Database的db变量
Database.db = __global_vars['db']
