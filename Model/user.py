"""用户的数据模型

/user可能的操作
/user:
    获取所有用户
    新建用户
/user/{uid}:
    获取单个用户
    修改密码
    删除用户
/user/{uid}/{items}:
    获取/修改tag
    获取/修改groups
    获取permissions
    获取meetings
    获取/修改info
"""
from pydantic import BaseModel
from typing import List
from .uuid import uuid
from .permission import Permission


class UserInfo(BaseModel):
    """用户个人信息的数据模型"""
    name: str
    email: str | None = None


class User(BaseModel):
    """用户的数据模型"""
    info: UserInfo
    hashed_passwd: str


class UserGetResponse(BaseModel):
    """响应获取用户的数据模型"""
    info: UserInfo
    meetings: List[uuid]
    group: uuid
    tags: List[uuid]
    permissions: List[Permission]


class UserCreateRequest(BaseModel):
    """请求创建用户的数据模型"""
    name: str
    password: str
    email: str | None = None
    group: uuid
    tags: List[uuid]


class UserUpdateRequest(BaseModel):
    """请求修改用户的数据模型"""
    name: str
    email: str | None
    group: uuid
    tags: List[uuid]


class UserPasswdUpdateRequest(BaseModel):
    """请求更新密码的数据模型"""
    old_password: str
    new_password: str
