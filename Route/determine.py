from fastapi import APIRouter
from typing import List
from datetime import datetime
import Object
from Model import uuid, DetermineAction, DetermineGetResponse, DetermineUpdateRequest

router = APIRouter()


@router.get('/determine', response_model=List[uuid])
async def get_determines():
    return [did for did in Object.Manager.determines.keys()]


@router.get('/determine/{did}', response_model=DetermineGetResponse)
async def get_determine(did: uuid):
    return Object.Manager.determines[did]


@router.put('/determine/{did}')
async def update_determine(did: uuid, data: DetermineUpdateRequest):
    if data.action == DetermineAction.Accept:
        if Object.Manager.determines[did].is_meeting:
            mid = Object.Manager.determines[did].id
            Object.Manager.meetings[mid].determine_step_append(
                f'{datetime.now().strftime("%m-%d %H:%M")} {group_name}{name} 同意了申请' +
                f'\n备注：{data.note}' if data.action else '')
        else:
            pass
    elif data.action == DetermineAction.Reject:
        if Object.Manager.determines[did].ismeeting:
            pass
        else:
            pass
