class ValidatorManager:
    def validate(self, mahasiswa, matkul):
        # Validasi SKS
        if mahasiswa["sks"] + matkul["sks"] > 24:
            return False, "SKS melebihi batas"

        # Validasi Prasyarat
        if matkul["prasyarat"] not in mahasiswa["matkul_lulus"]:
            return False, "Prasyarat belum terpenuhi"

        return True, "Registrasi valid"
# ==========================
# CONTOH PEMAKAIAN
# ==========================
if __name__ == "__main__":
    mahasiswa = {
        "nama": "Andi",
        "sks": 20,
        "matkul_lulus": ["IF101", "IF102"]
    }

    matkul = {
        "nama": "Struktur Data",
        "sks": 3,
        "prasyarat": "IF102"
    }

    manager = ValidatorManager()
    status, pesan = manager.validate(mahasiswa, matkul)

    print(status, "-", pesan)