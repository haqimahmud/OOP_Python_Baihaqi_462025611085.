# Sistem Pendaftaran Mahasiswa Baru UNIDA Gontor (Final Project PBO)

Aplikasi Web Pendaftaran Mahasiswa Baru berbasis Python Flask yang dibangun menggunakan pilar-pilar Pemrograman Berorientasi Objek (OOP).

## Fitur Utama
1. Pendaftaran Mahasiswa Baru secara online.
2. Cek Status Pendaftaran.
3. Portal Admin untuk Mengelola & Memverifikasi Data.
4. Pencarian Data Pendaftar.

## Menerapkan Pilar & Konsep OOP
- **Abstraction**: `Pengguna` sebagai Abstract Class dengan `@abstractmethod tampilInfo()`.
- **Inheritance**: `Mahasiswa` dan `Admin` mewarisi `Pengguna`.
- **Encapsulation**: Atribut private (`__nama`, `__noPendaftaran`, dll.) dengan Getter/Setter.
- **Polymorphism**: Implementasi method `tampilInfo()` yang berbeda di kelas turunan.
- **Magic Methods**: `__init__`, `__str__`, dan `__eq__`.
- **Advanced Methods**: `Instance Method` dan `@staticmethod validasi_no_pendaftaran()`.
- **Robustness**: Custom Exception Handling (`PendaftaranError`, `InvalidInputError`, `AuthenticationError`).

## Cara Menjalankan Aplikasi
1. Clone repositori ini:
   ```bash
   git clone <URL_REPOSITORY_GITHUB>
   cd OOP_BaihaqiAlwiMahmudi_462025611085/Final_Project