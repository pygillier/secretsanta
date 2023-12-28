import asyncio
from fastapi import FastAPI
from . import settings
from .database import engine

app = FastAPI(title="SecretSanta",
              description="Self-hosted Secret Santa",
              version=settings.app_version)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/people", tags=["People"])
async def people():
    return {"people": [{"name": "<NAME>", "discord_id": "<DISCORD_ID>"}]}


@app.post("/match", tags=["People"])
async def match_people():
    return {"message": "matching completed"}


@app.get("/trades", tags=["Trades"], description="List all existing trades following matching")
async def trade():
    return {"message": "All trades"}


@app.get("/trade/{discord_id}", tags=["Trades"])
async def get_single_trade(discord_id: str):
    return {"message": f"Trade done for {discord_id}"}