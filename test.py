import json
import os

# Carpeta on tens tots els JSON generats
JSON_FOLDER = "./PAU/"     # ajusta la ruta segons la teva estructura

OUTPUT = "bloc4_problemes.json"

def es_bloc4(p):
    bloc = p.get("bloc", "").lower()
    return bloc.startswith("bloc 4")

def main():
    tots = []

    for filename in os.listdir(JSON_FOLDER):
        if filename.endswith(".json"):
            ruta = os.path.join(JSON_FOLDER, filename)
            with open(ruta, "r", encoding="utf-8") as f:
                data = json.load(f)

            for problema in data:
                if es_bloc4(problema):
                    tots.append(problema)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(tots, f, indent=2, ensure_ascii=False)

    print(f"✔ {len(tots)} problemes trobats del Bloc 4")
    print(f"✔ Guardat a: {OUTPUT}")

if __name__ == "__main__":
    main()
