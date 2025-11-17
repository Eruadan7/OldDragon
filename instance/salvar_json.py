import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PASTA_JSON = os.path.join(BASE_DIR, "personagens_json")

def salvar_personagem_json(personagem):
    # cria a pasta se não existir
    if not os.path.exists(PASTA_JSON):
        os.makedirs(PASTA_JSON)

    arquivo = os.path.join(PASTA_JSON, f"{personagem.nome}.json")

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(personagem.to_dict(), f, ensure_ascii=False, indent=4)

    print(f"Personagem salvo em: {arquivo}")
