class AkunMediaSosial:

    def __init__(self , nama, sandi, email):
        self.__nama  = nama
        self.__sandi = sandi
        self.__email = email
        self.__jumlah_pengikut = 0

    def get_nama(self):
        return self.__nama

    def get_email(self,sandi):
        if sandi == self.__sandi:
            return self.__email
        else:
            return "Sandi yang anda masukkan salah !"

    def get_followers(self):
        return self.__jumlah_pengikut

    def tambah_followers(self, jumlah):
        self.__jumlah_pengikut += jumlah
        print(f"Pengikut berhasil ditambah {jumlah}")

    def ubah_sandi(self, sandi_lama, sandi_baru):
        if sandi_lama == self.__sandi:
            self.__sandi = sandi_baru
            print("Sandi berhasil diubah")

        else:
            print("Sandi lama salah! Tidak bisa mengubah sandi.")

    def ubah_email(self, password, email_baru):
        if password == self.__sandi:
            self.__email = email_baru
            print("Email berhasil diubah.")
        else:
            print("Password salah! Email gagal diubah")

akun1 = AkunMediaSosial("Baihaqi","12345","Baihaqi@gmail.com")

print("Nama :",akun1.get_nama())
print("Pengikut :", akun1.get_followers())

akun1.tambah_followers(100)

# Bukti atribut private tidak bisa diakses langsung
# print(akun1.__sandi)

print("Email :", akun1.get_email("23456"))

print("Email :", akun1.get_email("12345"))

akun1.ubah_sandi("12345","54321")

akun1.ubah_email("54321","alwi@gmail.com")

print("Email Baru:", akun1.get_email("54321"))

print("Email Baru:", akun1.get_email("12345"))
