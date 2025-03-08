
"""
This is launch pad for this project.

Classes:
    Game: The main class of the game.

Functions:


"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "World"}
