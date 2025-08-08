from fastapi import APIRouter, UploadFile, File, Depends, Form
from src.controllers import analyze_controller
from src.middlewares.auth_middleware import require_auth

router = APIRouter()

@router.post('/conversation')
async def conversation(file: UploadFile = File(...), user=Depends(require_auth)):
    return await analyze_controller.handle_conversation(file)

@router.post('/image')
async def image(file: UploadFile = File(...), user=Depends(require_auth)):
    return await analyze_controller.handle_image(file)

@router.post('/document')
async def document(file: UploadFile = File(...), user=Depends(require_auth)):
    return await analyze_controller.handle_document(file)

@router.post('/url')
async def url(url: str = Form(...), user=Depends(require_auth)):
    return await analyze_controller.handle_url(url)