"""
杂项数据模型

/register:
    用户注册
/login:
    用户登录
/wxlogin:
    用户微信登录
/logout:
    用户注销
"""
from pydantic import BaseModel


class RegisterRequest(BaseModel):
    """请求注册的数据模型"""
    name: str
    password: str | None = None
    email: str | None = None
    wxid: str | None = None


class LoginRequest(BaseModel):
    """请求登录的数据模型"""
    name: str | None = None
    email: str | None = None
    password: str
