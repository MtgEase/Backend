"""组织会易约中各个数据模型的包"""
from Model.misc import RegisterRequest, LoginRequest
from Model.user import UserInfo, User, UserGetResponse, UserUpdateRequest, UserCreateRequest, UserPasswdUpdateRequest
from Model.meeting import MeetingStatus, Meeting, MeetingGetResponse, MeetingUpdateRequest, MeetingCreateRequest
from Model.room import Room, RoomGetResponse, RoomUpdateRequest, RoomCreateRequest
from Model.determine import DetermineAction, Determine, DetermineGetResponse, DetermineUpdateRequest
from Model.group import Group, GroupGetResponse, GroupCreateRequest, GroupUpdateRequest
from Model.tag import Tag, TagGetResponse, TagUpdateRequest, TagCreateRequest
from Model.permission import Permission

# 写这个UUID是为了在代码提示中突出显示方便开发，以及为了以后的扩展
uuid = str
