from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import studio, live
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tactic CRM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(studio.router, prefix="/api/studio", tags=["studio"])
app.include_router(live.router, prefix="/api/live", tags=["live"])

@app.get("/")
def read_root():
    return {"status": "ok"}
