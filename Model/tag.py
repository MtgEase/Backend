"""Tag的数据模型

/tag可能的操作
/tag:
    获取所有tag
    新建tag
/tag/{tag}:
    获取/修改tag
    删除tag
"""
from pydantic import BaseModel
from typing import List
from Model import uuid, Permission


class Tag(BaseModel):
    """tag的数据模型"""
    tag: str
    permissions: List[Permission]
    targets: List[uuid]
    expire: str | None = None


class TagGetResponse(Tag):
    """响应获取tag的数据模型"""
    pass


class TagCreateRequest(Tag):
    """请求创建tag的数据模型"""
    pass


class TagUpdateRequest(Tag):
    """请求修改tag的数据模型"""
    expire: str | None
