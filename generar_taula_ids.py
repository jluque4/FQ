import json

# -------------------------------------------
# 1) LLISTA D'IDS QUE VOLEM (passada manualment)
# -------------------------------------------
IDS_DESITJATS = [
    "6-NU-6600660766026601",
    "6-NU-660266016601",
    "6-NU-6602660166086607",
    "6-NU-660066026601",
    "6-NU-6600660266016257",
    "6-NU-6602660166016600",
    "6-NU-6600660266016608",
    "6-NU-660266016600",
    "6-NU-660066076608",
    "6-NU-660266016257",
    "6-NU-660266016600",
    "6-NU-660066026601",
    "6-NU-660066026601",
    "6-NU-660266016600",
    "6-NU-660266016600",
    "6-NU-6602660166006607",
    "6-NU-660066026601",
    "6-NU-660266016600",
    "6-NU-660066026601",
    "6-NU-660062526257",
    "6-NU-660066026601",
    "6-NU-6600625262576607",
    "6-NU-66026601",
    "6-NU-6600660262526257",
    "6-NU-660266016600",
    "6-NU-66026601",
    "6-NU-660066026601",
    "6-NU-6600660166026607",
    "6-NU-66006601660262526257",
    "6-NU-660066026601",
    "6-NU-660066026601",
    "6-NU-660066026601",
    "6-NU-660066036607",
    "6-NU-660066016602",
    "6-NU-660066076252",
    "6-NU-660066026601",
    "6-NU-660266016600",
    "6-NU-6600660266016607",
    "6-NU-660066026601",
    "6-NU-660066026601",
    "6-NU-660066076603",
    "6-NU-660066026601",
    "6-NU-660266016600",
    "6-NU-660266016600",
    "6-NU-6607660366086611",
    "6-NU-6608660966106611",
    "6-NU-66036604660566066607",
    "6-NU-660066016602",
    "6-NU-66006602",
    "6-NU-66006602",
    "6-NU-660066016602",
    "6-NU-6600660166024250",
    "6-NU-660066016602",
    "6-NU-660066016602",
]

OUTPUT = "md/pau-problemes-filtrats.md"

# -------------------------------------------
# 2) CARREGAR CG_problemes.json
# -------------------------------------------
json_files = ["NU_problemes.json"]

entries = []
for path in json_files:
    with open(path, encoding="utf8") as f:
        data = json.load(f)

        for p in data:
            # En CG_problemes.json EL CAMP ÉS "id"
            if "id" in p:
                entries.append(p)

# -------------------------------------------
# 3) FILTRAR NOMÉS ELS IDS PASSATS MANUALMENT
# -------------------------------------------
entries = [p for p in entries if p["id"] in IDS_DESITJATS]

if not entries:
    print("⚠️ No s'ha trobat cap ID dels proporcionats.")
    exit()

# -------------------------------------------
# 4) ORDENAR DEL MÉS MODERN AL MÉS ANTIC
# -------------------------------------------
def conv_priority(c):
    return 0 if c == "jun" else 1

entries.sort(
    key=lambda x: (-x["any"], conv_priority(x.get("convocatoria", "")), x["id"])
)

# -------------------------------------------
# 5) GENERAR LES FILES DEL MARKDOWN
# -------------------------------------------
rows = []

for num, p in enumerate(entries):

    year = p["any"]
    pid = p["id"]
    problema = p["problema"]
    bloc = pid.split("-")[1]  # CG
    desc = p["descripcio"]

    pdf_enun = f"PAU/{p['imatge_enunciat']}"
    pdf_sol = f"PAU/{p['imatge_solucio']}"

    enun_icon = f'<a href="{pdf_enun}"><img src="img/pdf_a.png" width="29"/></a>'
    sol_icon  = f'<a href="{pdf_sol}"><img src="img/pdf_b.png" width="32"/></a>'

    rows.append(
        f"| {num+1} | {year} | {problema} | {desc} | {enun_icon} | {sol_icon} |"
    )

# -------------------------------------------
# 6) GENERAR FITXER MARKDOWN FINAL
# -------------------------------------------
content = [
    "# PAU — Problemes filtrats",
    "",
    "| N | Any | ID | Descripció | Enunciat | Solució |",
    "|--|--|--|:---|:--:|:--:|",
] + rows

with open(OUTPUT, "w", encoding="utf8") as f:
    f.write("\n".join(content))

print(f"✔ Generat {OUTPUT} correctament.")
