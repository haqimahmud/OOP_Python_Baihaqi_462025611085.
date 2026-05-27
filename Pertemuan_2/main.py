class MakananKesukaan:
    def __init__(self, nama, umur, makanan):
            self.nama = nama 
            self.umur = umur
            self.makanan = makanan

orang1 = MakananKesukaan("Baihaqi Alwi Mahmudi", 19, "Mie Ayam")
orang2 = MakananKesukaan("Muhammad Ali" , 17, "bakso")

print(f"Nama: {orang1.nama}, Umur: {orang1.umur}, Makanan Kesukaan: {orang1.makanan}")
print(f"Nama: {orang2.nama}, Umur: {orang2.umur}, Makanan Kesukaan: {orang2.makanan}")