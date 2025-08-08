import shutil
from pathlib import Path
from fastapi import UploadFile
from src.utils.storage import save_upload_file
from src.services import stt_service, diarization_service, image_service, summarize_service

async def handle_conversation(file: UploadFile):
    path = await save_upload_file(file)
    # 1) Run STT
    transcript = await stt_service.transcribe(path)
    # 2) Run diarization (custom implementation - do not rely on vendor diarization)
    diarized = await diarization_service.diarize(path, max_speakers=2)
    return {"transcript": transcript, "diarization": diarized}

async def handle_image(file: UploadFile):
    path = await save_upload_file(file)
    desc = await image_service.describe(path)
    return {"description": desc}

async def handle_document(file: UploadFile):
    path = await save_upload_file(file)
    text = await summarize_service.extract_text(path)
    summary = await summarize_service.summarize_text(text)
    return {"summary": summary}

async def handle_url(url: str):
    text = await summarize_service.extract_from_url(url)
    summary = await summarize_service.summarize_text(text)
    return {"summary": summary}