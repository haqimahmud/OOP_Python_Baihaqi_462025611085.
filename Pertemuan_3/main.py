class JadwalKuliah :

    def __init__(self, nama_matkul, dosen_pengampu):
        self.Nama_Matkul = nama_matkul
        self.Dosen_Pengampu = dosen_pengampu

    @staticmethod
    def Pemberitahuan() :
        print(f"Akan diadakan kuliah pada hari ini")
    def Dosen(self) :
        print(f"Mata Kuliah {self.Nama_Matkul } Akan diajarkan oleh {self.Dosen_Pengampu}")
    def kelas(self,lokasi) :
        print(f"Mata Kuliah {self.Nama_Matkul } Akan dilaksanakan di {lokasi}")

JadwalKuliah1 = JadwalKuliah('Teori Peluang','Ustz. Triana Harmini M.Pd')
JadwalKuliah2 = JadwalKuliah("Basis Data 1","Ust. Aziz Musthafa S.Kom, M.T.")

JadwalKuliah.Pemberitahuan()

print()

JadwalKuliah1.Pemberitahuan()
JadwalKuliah1.Dosen()
JadwalKuliah1.kelas('Lab. 121') 

print()

JadwalKuliah2.Pemberitahuan()
JadwalKuliah2.Dosen()
JadwalKuliah2.kelas('Lab. 329') 



