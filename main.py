from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()
altered_data = []


@app.on_event("startup")
def load_data():
    global altered_data
    with open(
        Path(__file__).parent / "data" / "produtos_alterados.json", encoding="utf-8"
    ) as f:
        altered_data = json.load(f)


@app.get("/api/produtos")
def get_produtos():
    return altered_data
