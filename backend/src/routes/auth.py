from fastapi import APIRouter, Depends
from src.controllers import auth_controller

router = APIRouter()

@router.post('/login')
async def login(payload: dict):
    return await auth_controller.login(payload)

# optional register route
@router.post('/register')
async def register(payload: dict):
    return await auth_controller.register(payload)