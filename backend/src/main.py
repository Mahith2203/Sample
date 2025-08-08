from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import auth, analyze
from src.config import settings

app = FastAPI(title="Playground Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(analyze.router, prefix="/analyze")

@app.get("/")
async def root():
    return {"status": "ok", "service": "playground-backend"}