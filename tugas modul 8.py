

data_awal = [
    ("2410433013", "cece", 100, 100, 100),
    ("2410433001", "naya", 70, 85, 95),
    ("2410433002", "cia", 90, 95, 85),
    ("2410433003", "cella", 80, 55, 70),
    ("2410433004", "tiara", 85, 80, 75),
    ("2410433005", "nayla", 50, 80, 60),
    ("2410433006", "pujhi", 95, 90, 88),
    ("2410433007", "dwi", 75, 40, 80),
    ("2410433008", "ika", 65, 60, 58),
    ("2410433009", "fiorenza", 88, 84, 82)
]


with open("data_praktikan.txt", "w") as file:
    for nim, nama, pre, post, tugas in data_awal:
        file.write(f"{nim},{nama},{pre},{post},{tugas}\n")

praktikan = {}

with open("data_praktikan.txt", "r") as file:
    for baris in file:
        baris = baris.strip()  
        nim, nama, pre, post, tugas = baris.split(",")
        praktikan[nim] = { 
            "nama": nama,
            "pretest": int(pre),
            "postest": int(post),
            "tugas": int(tugas)
        }


with open("data_nilai_akhir.txt", "w") as file:
    file.write("NIM       Nama           Pretest            Postest            Tugas          Total Nilai\n")
    for nim, data in praktikan.items():
        total = 0.35 * data["pretest"] + 0.35 * data["postest"] + 0.3 * data["tugas"]
        data["total"] = total
        file.write(f"{nim}     {data['nama']}    {data['pretest']}      {data['postest']}        {data['tugas']}         {total}\n")


total_nilai = [data["total"] for data in praktikan.values()]
rata_rata = sum(total_nilai) / len(total_nilai)


daftar_nim = list(praktikan.keys())
nim_tertinggi = daftar_nim[0]
nim_terendah = daftar_nim[0]

for nim in daftar_nim[1:]:
    if praktikan[nim]["total"] > praktikan[nim_tertinggi]["total"]:
        nim_tertinggi = nim
    elif praktikan[nim]["total"] < praktikan[nim_terendah]["total"]:
        nim_terendah = nim


jumlah_dibawah_rata = 0
for nilai in total_nilai:
    if nilai < rata_rata:
        jumlah_dibawah_rata += 1


print("== ANALISIS NILAI AKHIR PRAKTIKAN SHIFT 8 ==")
print()
print("1. Praktikan dengan nilai tertinggi    :", praktikan[nim_tertinggi]["nama"], f"({nim_tertinggi}) =", praktikan[nim_tertinggi]["total"])
print("2. Praktikan dengan nilai terendah     :", praktikan[nim_terendah]["nama"], f"({nim_terendah}) =", praktikan[nim_terendah]["total"])
print("3. Rata-rata Nilai Akhir               :", rata_rata)
print("4. Banyak praktikan di bawah rata-rata :", jumlah_dibawah_rata)


