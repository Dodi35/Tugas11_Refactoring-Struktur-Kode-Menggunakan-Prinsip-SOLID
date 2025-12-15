## Deskripsi
Repository ini berisi implementasi refactoring kode berorientasi objek menggunakan prinsip **SOLID**
(Single Responsibility Principle, Open/Closed Principle, dan Dependency Inversion Principle)
pada studi kasus **Sistem Validasi Registrasi Mahasiswa**.

---

## Permasalahan
Pada kode awal, seluruh proses validasi (validasi SKS dan prasyarat mata kuliah)
ditangani dalam satu class menggunakan struktur `if/else`. Hal ini menyebabkan:
- Class memiliki lebih dari satu tanggung jawab (melanggar SRP)
- Sulit menambahkan aturan validasi baru (melanggar OCP)
- Class bergantung pada implementasi konkret (melanggar DIP)

---

## Solusi Refactoring
Refactoring dilakukan dengan cara:
- Memisahkan setiap aturan validasi ke dalam class tersendiri (SRP)
- Menggunakan abstract class `ValidationRule` sebagai kontrak (DIP)
- Menambahkan aturan validasi baru tanpa mengubah kode lama (OCP)

---

## Struktur File
- `sebelum_refactor.py` : Kode sebelum menerapkan prinsip SOLID
- `sesudah_refactor.py` : Kode setelah refactoring dengan SRP, OCP, dan DIP
- `README.md` : Dokumentasi proyek

---
