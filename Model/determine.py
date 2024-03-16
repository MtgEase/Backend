"""
审批的数据模型

/determine可能的操作
/determine:
    获取所有审批
/determine/{did}:
    处理审批（通过或拒绝）
"""
from pydantic import BaseModel
from enum import Enum
from .uuid import uuid


class DetermineAction(str, Enum):
    """审批操作的枚举"""
    Accept: str = "accept"
    Reject: str = "reject"


class Determine(BaseModel):
    """审批的数据模型"""
    is_meeting: bool = True
    id: uuid


class DetermineGetResponse(Determine):
    """响应获取审批的数据模型"""
    pass


class DetermineUpdateRequest(BaseModel):
    """请求修改审批的数据模型"""
    action: DetermineAction
    note: str | None = None
