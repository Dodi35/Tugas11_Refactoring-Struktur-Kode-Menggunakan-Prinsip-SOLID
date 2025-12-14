from abc import ABC, abstractmethod
# ==========================
# ABSTRAKSI (DIP & OCP)
# ==========================
class ValidationRule(ABC):
    @abstractmethod
    def validate(self, mahasiswa, matkul):
        pass
# ==========================
# VALIDASI SKS (SRP)
# ==========================
class SksValidator(ValidationRule):
    def validate(self, mahasiswa, matkul):
        if mahasiswa["sks"] + matkul["sks"] > 24:
            return False, "SKS melebihi batas"
        return True, ""
# ==========================
# VALIDASI PRASYARAT (SRP)
# ==========================
class PrasyaratValidator(ValidationRule):
    def validate(self, mahasiswa, matkul):
        if matkul["prasyarat"] not in mahasiswa["matkul_lulus"]:
            return False, "Prasyarat belum terpenuhi"
        return True, ""
# ==========================
# VALIDASI IPK (CHALLENGE OCP)
# ==========================
class IpkValidator(ValidationRule):
    def validate(self, mahasiswa, matkul):
        if mahasiswa["ipk"] < 3.15:
            return False, "IPK tidak mencukupi"
        return True, ""
# ==========================
# VALIDATOR MANAGER (DI)
# ==========================
class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, mahasiswa, matkul):
        for validator in self.validators:
            status, message = validator.validate(mahasiswa, matkul)
            if not status:
                return False, message
        return True, "Registrasi valid"
# ==========================
# CONTOH EKSEKUSI
# ==========================
if __name__ == "__main__":
    mahasiswa = {
        "nama": "Andi",
        "sks": 20,
        "ipk": 3.10,
        "matkul_lulus": ["IF101", "IF102"]
    }

    matkul = {
        "nama": "Struktur Data",
        "sks": 3,
        "prasyarat": "IF102"
    }

    validators = [
        SksValidator(),
        PrasyaratValidator(),
        IpkValidator()
    ]
    
    manager = ValidatorManager(validators)
    status, pesan = manager.validate(mahasiswa, matkul)

    print(status, "-", pesan)
