class SaldoRekening:
    pemilik = " "
    saldo = 0

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        if saldo < 0 :
            raise ValueError("Saldo tidak boleh negatif")
        self.saldo = saldo

    def __str__(self):
        return f"{self.pemilik} memiliki saldo {self.saldo}"

    def __eq__(self, other):
        return self.saldo == other.saldo

    def __lt__(self, other):
        return self.saldo < other.saldo

    def __gt__(self, other):
        return self.saldo > other.saldo
    
Pemilik1 = SaldoRekening("Baihaqi" , 20000000)
print(Pemilik1)
Pemilik2 = SaldoRekening("Alwi" , 20000000)
print(Pemilik2)
Pemilik3 = SaldoRekening("Mahmudi" , 80000000)
print(Pemilik3)
Pemilik4 = SaldoRekening("Ahmad" , 50000000)
print(Pemilik4)

print()

print("Apakah Saldo Rekening Pemilik 1 dan 2 Sama ?")
print(Pemilik1 == Pemilik2)

print("Apakah Saldo Rekening Pemilik 2 lebih kecil dari pemilik 3 ?")
print(Pemilik2 < Pemilik3)

print("Apakah Saldo Rekening Pemilik 3 lebih besar dari pemilik 4 ?")
print(Pemilik3 > Pemilik4)

print("Apakah Saldo Rekening Pemilik 4 dan 1 Sama ?")
print(Pemilik4 == Pemilik1)

print("Apakah Saldo Rekening Pemilik 1 lebih besar dari pemilik 3 ?")
print(Pemilik1 > Pemilik3)

print("Apakah Saldo Rekening Pemilik 2 lebih besar dari pemilik 4 ?")
print(Pemilik2 > Pemilik4)

