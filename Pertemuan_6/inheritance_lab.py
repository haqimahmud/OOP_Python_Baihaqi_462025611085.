class AlatElektronik:
    def __init__(self, merk, jenis):
        self.merk = merk
        self.jenis = jenis

    def info(self):
        print(f"Ini adalah {self.merk} dengan jenis {self.jenis}.")
        
    def benda(self):
        print(f"Benda ini adalah benda Alat Elektronik")

class laptop(AlatElektronik):
    def benda(self):
        print(f"hasil print dari kelas Laptop")
        
    def dari_parent(self):
        super().benda()
        
class handphone(AlatElektronik):
    def benda(self):
        print(f"hasil print dari kelas Handphone")
        
    def dari_parent(self):
        super().benda()

laptop1 = laptop("Acer","Aspire E1-410")
laptop1.info()
laptop1.benda()
laptop1.dari_parent()

handphone1 = handphone("Vivo","Y75 5G")
handphone1.info()
handphone1.benda()
handphone1.dari_parent()

class PerangkatCerdas(laptop, handphone):
    def fitur(self):
        print("Perangkat cerdas (gabungan laptop dan handphone)")
        super().benda()  

perangkatcerdas = PerangkatCerdas("Asus","Hybrid Device")
perangkatcerdas.info()
perangkatcerdas.benda()

print(PerangkatCerdas.mro())
