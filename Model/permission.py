"""用户权限枚举"""
from enum import Enum


class Permission(str, Enum):
    """用户权限枚举"""
    Register: str = "Register"
    BasicAccess: str = "BasicAccess"
    DirectlyApply: str = "DirectlyApply"
    Determine_All: str = "Determine.All"
    Determine_Stu: str = "Determine.Stu"
    Determine_Tch: str = "Determine.Tch"
    ManageUser_All: str = "ManageUser.All"
    ManageUser_Stu: str = "ManageUser.Stu"
    ManageUser_Tch: str = "ManageUser.Tch"
    ManageRoom_All: str = "ManageRoom.All"
