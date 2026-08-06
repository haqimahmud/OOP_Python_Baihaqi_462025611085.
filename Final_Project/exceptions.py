class PendaftaranError(Exception):
    """Base Exception untuk aplikasi pendaftaran."""
    pass

class InvalidInputError(PendaftaranError):
    """Exception jika input pengguna tidak valid."""
    def __init__(self, message="Input yang dimasukkan tidak valid!"):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(PendaftaranError):
    """Exception jika login admin gagal."""
    def __init__(self, message="Username atau Password salah!"):
        self.message = message
        super().__init__(self.message)