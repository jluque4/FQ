import json
import glob

OUTPUT = "md/pau-problemes.md"

rows = []

# Carregar tots els JSON
json_files = glob.glob("PAU/pau_*.json")

entries = []
for path in json_files:
    with open(path, encoding="utf8") as f:
        data = json.load(f)

        for p in data:
            entries.append(p)

# -------------------------------------------------------
# ORDENAR DEL MÉS MODERN AL MÉS ANTIC
# any descendent, convocatòria jun abans que sep
# -------------------------------------------------------
def conv_priority(c):
    return 0 if c == "jun" else 1  # jun → primer

entries.sort(key=lambda x: (-x["any"], conv_priority(x["convocatoria"]), x["problema"]))


# -------------------------------------------------------
# GENERAR LES FILES DEL MARKDOWN
# -------------------------------------------------------
for p in entries:
    year = p["any"]
    conv = p["convocatoria"]
    pid = p["problema"]
    bloc = p["bloc"]
    desc = p["descripcio"]

    # Rutes PDF (no imatges!)
    pdf_enun = f"FQ/PAU/{p['imatge_enunciat']}"
    pdf_sol = f"FQ/PAU/{p['imatge_solucio']}"

    # Icones clicables
    enun_icon = (
    f'<a href="{pdf_enun}" target="_blank" type="application/pdf">'
    f'<img src="img/pdf_a.png" width="29"/></a>'
)

    sol_icon = (
        f'<a href="{pdf_sol}" target="_blank" type="application/pdf">'
        f'<img src="img/pdf_b.png" width="32"/></a>'
    )

    rows.append(f"| {year} | {pid} | {bloc} | {desc} | {enun_icon} | {sol_icon} |")


# -------------------------------------------------------
# GENERAR FITXER MARKDOWN
# -------------------------------------------------------
content = [
    "# PAU — Problemes 2008-2025",
    "",
    "",
    "| Any | ID | Bloc | Descripció | Exam | Resp |",
    "|--|--|:---|:---|:--:|:--:|",
] + rows

with open(OUTPUT, "w", encoding="utf8") as f:
    f.write("\n".join(content))

print("✔ Generat md/pau-problemes.md correctament.")

