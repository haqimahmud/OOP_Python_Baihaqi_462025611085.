
class NilaiTerlaluTinggiError(Exception):
    pass

class NilaiNegatifError(Exception):
    pass
        
class FormatNIMSalahError(Exception):
    pass
        
class MataKuliahTidakTerdaftarError(Exception):
    pass

class PortalNilai():
    def __init__(self, nama, nim, mata_kuliah, nilai_awal):
        self.nama = nama
        self.nim = nim
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai_awal

    def update_nilai(self, nilai_baru, nim, mata_kuliah):
        if nim != self.nim:
            raise FormatNIMSalahError("NIM Mahasiswa tidak cocok/salah")
        if mata_kuliah != self.mata_kuliah:
            raise MataKuliahTidakTerdaftarError("Mata kuliah tidak sesuai dengan KRS mahasiswa")
        if nilai_baru > 100:
            raise NilaiTerlaluTinggiError("Nilai tidak boleh lebih dari 100")
        if nilai_baru < 0:
            raise NilaiNegatifError("Nilai tidak boleh negatif (kurang dari 0)")
            
        self.nilai = nilai_baru
        print(f"Update berhasil! Nilai baru untuk {self.nama} adalah {self.nilai}")
    
    def cek_nilai(self, nim, mata_kuliah):
        if nim != self.nim:
            raise FormatNIMSalahError("NIM Mahasiswa tidak cocok/salah")
        if mata_kuliah != self.mata_kuliah:
            raise MataKuliahTidakTerdaftarError("Mata kuliah tidak sesuai dengan KRS mahasiswa")
        print(f"Nilai {self.nama} pada matkul {self.mata_kuliah} adalah {self.nilai}")
        
    def tambah_poin_keaktifan(self, poin, nim, mata_kuliah):
        if poin < 0:
            raise NilaiNegatifError("Poin keaktifan tidak boleh negatif")
        if nim != self.nim:
            raise FormatNIMSalahError("NIM Mahasiswa tidak cocok/salah")
        if mata_kuliah != self.mata_kuliah:
            raise MataKuliahTidakTerdaftarError("Mata kuliah tidak sesuai dengan KRS mahasiswa")
            
        if self.nilai + poin > 100:
            raise NilaiTerlaluTinggiError("Penambahan poin membuat nilai melebihi batas maksimal 100")
            
        self.nilai += poin
        print(f"Poin berhasil ditambahkan. Nilai baru sekarang: {self.nilai}")


mahasiswa = PortalNilai("Baihaqi", "46202561185", "statistika", 85)

try:    
    PortalNilai.update_nilai(mahasiswa, 150, "46202561185", "statistika") 
    PortalNilai.cek_nilai(mahasiswa, "46202561185", "statistika")
    PortalNilai.tambah_poin_keaktifan(mahasiswa, 5, "46202561185", "statistika")
except NilaiTerlaluTinggiError as e:
    print(f"[ERROR]: {e}")
except NilaiNegatifError as e:
    print(f"[ERROR]: {e}")
except FormatNIMSalahError as e:
    print(f"[ERROR]: {e}")
except MataKuliahTidakTerdaftarError as e:
    print(f"[ERROR]: {e}")
finally:
    print("INFO: Proses pemeriksaan nilai blok 1 selesai dilakukan.\n")

try:    
    PortalNilai.cek_nilai(mahasiswa, "46202561185", "statistika")
    PortalNilai.tambah_poin_keaktifan(mahasiswa, 10, "46202561185", "statistika") # Nilai jadi 90
    PortalNilai.update_nilai(mahasiswa, 95, "46202561185", "statistika") # Nilai diubah ke 95
except NilaiTerlaluTinggiError as e:
    print(f"[ERROR]: {e}")
except NilaiNegatifError as e:
    print(f"[ERROR]: {e}")
except FormatNIMSalahError as e:
    print(f"[ERROR]: {e}")
except MataKuliahTidakTerdaftarError as e:
    print(f"[ERROR]: {e}")
finally:
    print("INFO: Proses pemeriksaan nilai blok 2 selesai dilakukan.")