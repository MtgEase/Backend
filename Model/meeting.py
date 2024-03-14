"""
会议的数据模型

/meeting可能的操作
/meeting:
    获取所有会议
    新建会议
/meeting/{mid}
    获取/修改会议
    删除会议
"""
from pydantic import BaseModel
from typing import List
from enum import Enum
from Model import uuid


class MeetingStatus(str, Enum):
    """会议申请的各个状态"""
    Draft: str = 'Draft'
    Pending: str = 'Pending'
    Reviewing: str = 'Reviewing'
    Approved: str = 'Approved'
    Rejected: str = 'Rejected'


class Meeting(BaseModel):
    """会议的数据模型"""
    topic: str
    time_start: str
    time_stop: str
    room: uuid
    tip: str | None
    status: MeetingStatus
    determine_step: List[str]
    created_by: uuid


class MeetingGetResponse(Meeting):
    """响应获取会议的数据模型"""
    pass


class MeetingUpdateRequest(BaseModel):
    """请求修改会议的数据结构"""
    topic: str
    time_start: str
    time_stop: str
    room: uuid
    tip: str | None


class MeetingCreateRequest(MeetingUpdateRequest):
    """请求创建会议的数据结构"""
    tip: str | None = None
