from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/stack-plugin")
async def root():
    with open("stack-plugin/data.json", "r") as f:
        data = eval(str(f.read()))
    return data
