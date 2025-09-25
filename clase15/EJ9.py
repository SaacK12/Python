lista = [
    "Abaddon", "Abdiel", "Adramelech", "Aeros", "Agathion", "Agrat", "Aitvaras", "Alice", "Alilat", "Amabie",
    "Amanozako", "Ame no Uzume", "Amon", "Anahita", "Anansi", "Ananta", "Andras", "Angel", "Anubis", "Anzu",
    "Apsaras", "Aquans", "Arahabaki", "Archangel", "Arioch", "Armaiti", "Artemis", "Asura", "Atavaka", "Atropos",
    "Attis", "Azazel", "Azumi", "Baal", "Baphomet", "Basilisk", "Bugs", "Byakko", "Cait Sith", "Cerberus", "Chimera",
    "Cleopatra", "Cu Chulainn", "Danu", "Dionysus", "Dojin", "Dullahan", "Fafnir", "Feng Huang", "Fionn mac Cumhaill",
    "Fortuna", "Futsunushi", "Gabriel", "Girimekhala", "Gnome", "Gogmagog", "Gozu-Tennoh", "Hecatoncheires", "Hecate",
    "Horus", "Hydra", "Idun", "Inanna", "Inugami", "Jack Frost", "Jatayu", "Jikokuten", "Kali", "Kama", "Kartikeya",
    "Khonsu", "Kingu", "Kirin", "Kitsune", "Kohryu", "Kushinada", "Lakshmi", "Lilith", "Loki", "Loup-garou", "Lucifer",
    "Mada", "Mafdet", "Mara", "Mastema", "Medea", "Melchizedek", "Metatron", "Mithra", "Mokoi", "Mothman", "Naga",
    "Neko Shogun", "Nekomata", "Norn", "Nuwa", "Odin", "Omoikane", "Orobas", "Orthrus", "Ose", "Pazuzu", "Persephone",
    "Principality", "Raphael", "Red Rider", "Samael", "Sarasvati", "Scathach", "Seth", "Shiva", "Shiro", "Siegfried",
    "Sraosha", "Surt", "Tao", "Throne", "Thunderbird", "Trumpeter", "Uriel", "Vasuki"
]
contador_A= 0
contador_E= 0
contador_I= 0
contador_O= 0
contador_U= 0
for palabra in lista:
    for letra in palabra:
        if letra.lower() == "a":
            contador_A += 1
        if letra.lower() == "e":
            contador_E += 1
        if letra.lower() == "i":
            contador_I += 1
        if letra.lower() == "o":
            contador_O += 1
        if letra.lower() == "u":
            contador_U += 1
print(f"En Shin Megami Tensei V hay {contador_A} demonios con la letra A")
print(f"{contador_E} demonios con la letra E")
print(f"{contador_I} demonios con la letra I")
print(f"{contador_O} demonios con la letra O")
print(f"{contador_U} demonios con la letra U")