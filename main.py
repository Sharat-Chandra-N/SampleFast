from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"Application Doc": "Random Number Generator"}

@app.get("/random")
async def random_num():
    randomNumber: int = random.randint(0, 100)
    return{"Random Number" : randomNumber}

@app.get("/random/{limit}")
async def random_num(limit: int):
    randomNumber: int = random.randint(0, limit)
    return{"Random Number" : randomNumber}