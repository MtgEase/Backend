"""Group的数据模型

/group可能的操作
/group:
    获取所有group
    新建group
/group/{group}:
    获取/修改group
    删除group
"""
from pydantic import BaseModel
from typing import List
from .uuid import uuid
from .permission import Permission


class Group(BaseModel):
    """group的数据模型"""
    name: str
    belong_to: uuid
    permissions: List[Permission]


class GroupGetResponse(Group):
    """响应获取group的数据模型"""
    pass


class GroupCreateRequest(Group):
    """请求创建group的数据模型"""
    pass


class GroupUpdateRequest(Group):
    """请求修改group的数据模型"""
    pass
