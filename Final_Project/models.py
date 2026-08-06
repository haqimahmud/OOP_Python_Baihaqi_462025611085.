from abc import ABC, abstractmethod
from exceptions import InvalidInputError, AuthenticationError

# 1. ABSTRACTION & INHERITANCE: Parent Class Pengguna
class Pengguna(ABC):
    def __init__(self, nama: str, alamat: str, nomorTelepon: str):
        # 2. ENCAPSULATION: Atribut private
        self.__nama = nama
        self.__alamat = alamat
        self.__nomorTelepon = nomorTelepon

    # Getter & Setter
    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        if not nama.strip():
            raise InvalidInputError("Nama tidak boleh kosong.")
        self.__nama = nama

    def get_alamat(self):
        return self.__alamat

    def set_alamat(self, alamat):
        self.__alamat = alamat

    def get_nomor_telepon(self):
        return self.__nomorTelepon

    def set_nomor_telepon(self, no_telp):
        if not no_telp.isdigit():
            raise InvalidInputError("Nomor telepon hanya boleh berisi angka.")
        self.__nomorTelepon = no_telp

    # Abstract Method
    @abstractmethod
    def tampilInfo(self):
        pass

    # Magic Method
    def __str__(self):
        return f"Pengguna: {self.__nama} ({self.__nomorTelepon})"


# Child Class: Mahasiswa
class Mahasiswa(Pengguna):
    def __init__(self, nama: str, alamat: str, nomorTelepon: str, noPendaftaran: str, asalSekolah: str, programStudi: str):
        super().__init__(nama, alamat, nomorTelepon)
        self.__noPendaftaran = noPendaftaran
        self.asalSekolah = asalSekolah
        self.programStudi = programStudi

    def daftar(self):
        pendaftaran_baru = Pendaftaran(self)
        pendaftaran_baru.simpanData()
        return pendaftaran_baru

    def get_no_pendaftaran(self):
        return self.__noPendaftaran

    def lihatStatus(self, daftar_pendaftaran):
        for p in daftar_pendaftaran:
            if p.mahasiswa.get_no_pendaftaran() == self.__noPendaftaran:
                return p.statusPendaftaran
        return "Data tidak ditemukan"

    # 3. POLYMORPHISM: Implementasi tampilInfo
    def tampilInfo(self):
        return {
            "Tipe": "Mahasiswa",
            "No Pendaftaran": self.__noPendaftaran,
            "Nama": self.get_nama(),
            "Prodi": self.programStudi,
            "Asal Sekolah": self.asalSekolah
        }

    def __str__(self):
        return f"Mahasiswa: {self.get_nama()} - {self.programStudi} [{self.__noPendaftaran}]"


# Child Class: Admin
class Admin(Pengguna):
    def __init__(self, nama: str, alamat: str, nomorTelepon: str, username: str, password: str):
        super().__init__(nama, alamat, nomorTelepon)
        self.__username = username
        self.__password = password

    def login(self, username_input, password_input):
        if self.__username == username_input and self.__password == password_input:
            return True
        raise AuthenticationError("Username atau password Admin salah.")

    def lihatData(self, daftar_pendaftaran):
        return [p.tampilData() for p in daftar_pendaftaran]

    def ubahData(self, pendaftaran, status_baru):
        pendaftaran.verifikasiData(status_baru)

    def hapusData(self, daftar_pendaftaran, pendaftaran):
        if pendaftaran in daftar_pendaftaran:
            daftar_pendaftaran.remove(pendaftaran)

    def tampilInfo(self):
        return {
            "Tipe": "Admin",
            "Nama": self.get_nama(),
            "Username": self.__username
        }

    def __str__(self):
        return f"Admin: {self.get_nama()} ({self.__username})"


# Class Pendaftaran (Relasi dengan Mahasiswa)
class Pendaftaran:
    _daftar_pendaftaran = []  # Static / Class Variable

    def __init__(self, mahasiswa: Mahasiswa):
        self.mahasiswa = mahasiswa
        self.statusPendaftaran = "Sedang Diproses"

    # Static Method (Persyaratan Advanced Methods)
    @staticmethod
    def validasi_no_pendaftaran(no_pendaftar: str) -> bool:
        """Validasi format No Pendaftaran (harus diawali 'REG-')"""
        return no_pendaftar.startswith("REG-") and len(no_pendaftar) >= 8

    # Instance Methods
    def simpanData(self):
        if not Pendaftaran.validasi_no_pendaftaran(self.mahasiswa.get_no_pendaftaran()):
            raise InvalidInputError("Format Nomor Pendaftaran tidak valid! Harus diawali 'REG-'.")
        Pendaftaran._daftar_pendaftaran.append(self)

    def verifikasiData(self, status_baru: str):
        valid_status = ["Diterima", "Ditolak", "Sedang Diproses", "Memerlukan Perbaikan"]
        if status_baru not in valid_status:
            raise InvalidInputError("Status pendaftaran tidak valid.")
        self.statusPendaftaran = status_baru

    def tampilData(self):
        return {
            "no_pendaftaran": self.mahasiswa.get_no_pendaftaran(),
            "nama": self.mahasiswa.get_nama(),
            "prodi": self.mahasiswa.programStudi,
            "asal_sekolah": self.mahasiswa.asalSekolah,
            "status": self.statusPendaftaran
        }

    # Magic Method __eq__ untuk perbandingan data
    def __eq__(self, other):
        if isinstance(other, Pendaftaran):
            return self.mahasiswa.get_no_pendaftaran() == other.mahasiswa.get_no_pendaftaran()
        return False