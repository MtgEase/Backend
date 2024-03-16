"""
会议室的数据模型

/room可能的操作
/room:
    获取所有会议室
    新建会议室
/room/{rid}:
    获取/修改会议室
    删除会议室
"""
from typing import List
from pydantic import BaseModel
from .uuid import uuid


class Room(BaseModel):
    """会议室的数据模型"""
    name: str
    position: str
    tip: str | None = None
    available: bool = True
    capacity: int | None = None
    devices: List[str] | None = None
    rest: List[str] | None = None


class RoomGetResponse(Room):
    """响应获取会议室的数据模型"""
    meetings: List[uuid]


class RoomUpdateRequest(BaseModel):
    """请求修改会议室的数据模型"""
    name: str
    position: str
    tip: str | None
    available: bool
    capacity: int | None
    devices: List[str] | None
    rest: List[str] | None


class RoomCreateRequest(Room):
    """请求创建会议室的数据模型"""
    pass
