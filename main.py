from fastapi import FastAPI, Query
import json
from pathlib import Path
import math

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
def get_produtos(
    page: int = Query(1, ge=1, description="Número da página"),
    limit: int = Query(200, ge=1, le=1000, description="Itens por página")
):
    # Calcular offset
    offset = (page - 1) * limit
    
    # Total de itens
    total_items = len(altered_data)
    
    # Paginar os dados
    paginated_data = altered_data[offset:offset + limit]
    
    # Calcular informações de paginação
    total_pages = math.ceil(total_items / limit)
    
    return {
        "data": paginated_data,
        "pagination": {
            "current_page": page,
            "items_per_page": limit,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next_page": page < total_pages,
            "has_previous_page": page > 1
        }
    }
