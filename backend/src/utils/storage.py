import os
from pathlib import Path
from fastapi import UploadFile
from src.config import settings

UPLOAD_DIR = Path(settings.upload_dir)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def save_upload_file(upload_file: UploadFile) -> str:
    dest = UPLOAD_DIR / upload_file.filename
    with open(dest, 'wb') as f:
        content = await upload_file.read()
        f.write(content)
    return str(dest)

def remove_file(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass