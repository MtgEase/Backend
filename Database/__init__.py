"""与会易约存储后端交互的模块"""
import yaml


class Database:
    """
    通用存储后端交互的基类。
    此类封装了对存储后端的增删改查功能。
    """
    # db存储了实际的存储后端驱动的对象
    db = None

    def __init__(self):
        # 存储后端驱动应实现增删改查的功能
        self.insert_data = Database.db.insert_data
        self.select_data = Database.db.select_data
        self.delete_data = Database.db.delete_data
        self.update_data = Database.db.update_data


# 读取配置文件的Database键值
with open('Config/config.yaml', 'r', encoding='utf-8') as __f:
    __config: dict = yaml.safe_load(__f)['Database']
    __driver: str = __config['Driver']
    __args: dict = __config['DriverArgs']
# 使用exec函数，拼接从配置文件读取到的驱动名并执行，获取到驱动后端对象
__global_vars: dict = {}
exec(f'from Database.StorageDriver.{__driver} import {__driver};'
     f'db = {__driver}(**{str(__args)})', __global_vars)
# 保存实际的对象到Database的db变量
Database.db = __global_vars['db']
