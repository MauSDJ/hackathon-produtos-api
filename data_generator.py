import csv
import random
import string
import json
from faker import Faker
from pathlib import Path

fake = Faker()


def random_word(length=3):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_csv_and_json(csv_path: str, json_path: str, num_rows: int = 500_000):
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)

    categorias = ["Periféricos", "Móveis", "Hardware", "Acessórios", "Componentes"]
    fornecedores = ["TechNova", "ClickPro", "OfficeLine", "HardZone", "SupraTech"]

    all_rows = []

    with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "nome", "categoria", "preco", "estoque", "fornecedor"])

        for i in range(1, num_rows + 1):
            nome = fake.word().capitalize() + " " + random_word()
            categoria = random.choice(categorias)
            preco = round(random.uniform(10.0, 1500.0), 2)
            estoque = random.randint(0, 500)
            fornecedor = random.choice(fornecedores)
            row = {
                "id": i,
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "estoque": estoque,
                "fornecedor": fornecedor,
            }
            all_rows.append(row)
            writer.writerow(row.values())

    # Modificar 20%
    altered_rows = []
    for row in all_rows:
        altered = row.copy()
        if random.random() < 0.2:
            campo = random.choice(["nome", "preco", "estoque", "fornecedor"])
            if campo == "nome":
                altered["nome"] += " X"
            elif campo == "preco":
                altered["preco"] = round(
                    altered["preco"] * random.uniform(0.95, 1.05), 2
                )
            elif campo == "estoque":
                altered["estoque"] += random.randint(-3, 3)
            elif campo == "fornecedor":
                altered["fornecedor"] += " Ltda"
        altered_rows.append(altered)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(altered_rows, f, ensure_ascii=False, indent=2)
