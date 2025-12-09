import os
import json
import yaml

# ---------------------------------------------------------
# 1. LLEGIR claus.yaml i obtindre el rang d'un tema (CG, CE, CM...)
# ---------------------------------------------------------

def obtenir_rang_tema(tema_id, claus_path="claus.yaml"):
    with open(claus_path, "r", encoding="utf8") as f:
        data = yaml.safe_load(f)

    for bloc in data.values():
        if isinstance(bloc, dict) and "subarees" in bloc:
            for sub in bloc["subarees"].values():
                if sub.get("id") == tema_id:
                    return sub["rang"]

    raise ValueError(f"❌ Tema {tema_id} no trobat en claus.yaml")


# ---------------------------------------------------------
# 2. EXTREURE PROBLEMES COMPLETS D'UN TEMA (p. ex. CG)
# ---------------------------------------------------------

def extreure_problemes_tema(directori_json, tema_id="CG", claus_path="claus.yaml"):
    min_rang, max_rang = obtenir_rang_tema(tema_id, claus_path)
    problemes = []

    for fitxer in os.listdir(directori_json):
        if not fitxer.endswith(".json"):
            continue

        ruta = os.path.join(directori_json, fitxer)
        try:
            data = json.load(open(ruta, "r", encoding="utf8"))
        except:
            continue

        for p in data:
            if "id" not in p:
                continue

            parts = p["id"].split("-")
            if len(parts) < 3:
                continue

            # subàrea = CE, CM, CI...
            subarea = parts[1]
            if subarea != tema_id:
                continue

            # codi numèric
            try:
                codi = int(parts[2][:4])
            except:
                continue

            if min_rang <= codi <= max_rang:
                problemes.append(p)

    return problemes


# ---------------------------------------------------------
# 3. EXECUCIÓ PRINCIPAL
# ---------------------------------------------------------

if __name__ == "__main__":

    directori = "PAU"
    tema = "NU"   # <<-- CANVIA ACÍ: CE, CM, CI

    problemes = extreure_problemes_tema(directori, tema)

    # Guardar JSON com sempre
    output_file = f"{tema}_problemes.json"
    with open(output_file, "w", encoding="utf8") as f:
        json.dump(problemes, f, ensure_ascii=False, indent=2)

    print(f"\n✔ Creat el fitxer: {output_file}")
    print(f"✔ Nombre de problemes trobats: {len(problemes)}\n")

    # -----------------------------------------------------
    # NOVA PART: GENERAR LLISTA D'IDS DIRECTAMENT
    # -----------------------------------------------------

    ids = [p["id"] for p in problemes]

    print("📌 Llista d'IDs (per copiar al script):\n")
    print(f"{tema}_ids = [")
    for pid in ids:
        print(f'    "{pid}",')
    print("]\n")

    print("📌 Llista plana d'IDs:\n")
    for pid in ids:
        print(pid)

