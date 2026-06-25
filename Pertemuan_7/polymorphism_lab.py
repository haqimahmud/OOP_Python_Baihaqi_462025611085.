class Notifikasi:
    def __init__(self, nama: str):
        self.nama = nama
        
    def kirim(self):
        print(f"Notifikasi untuk {self.nama} sedang diproses secara umum.")

class Email(Notifikasi):
    def kirim(self):
        print(f"Notifikasi Email ke {self.nama} berhasil dikirim via server SMTP.")

class WhatsApp(Notifikasi):
    def kirim(self):
        print(f"Notifikasi WhatsApp ke {self.nama} berhasil dikirim via API Gateway.")

# === PENJELASAN DUCK TYPING & POLYMORPHISM ===
# Fungsi di bawah ini adalah fungsi mandiri yang menerapkan Duck Typing.
# Fungsi ini bisa memproses objek dari kelas yang berbeda (Email / WhatsApp)
# tanpa memedulikan tipe kelasnya, selama objek tersebut memiliki metode kirim()

def simulasikan_notifikasi(notifikasi):
    notifikasi.kirim()

# Instansiasi Objek (Sama persis alurnya dengan contoh materi)
notifikasi_biasa = Notifikasi("Baihaqi")
fitur_email = Email("Alwi")
fitur_wa = WhatsApp("Mahmudi")

print("--- Simulasi Sistem Notifikasi ---")
simulasikan_notifikasi(notifikasi_biasa)
simulasikan_notifikasi(fitur_email)
simulasikan_notifikasi(fitur_wa)