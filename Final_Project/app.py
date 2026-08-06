from flask import Flask, render_template, request, redirect, url_for, flash
import random
from models import Mahasiswa, Admin, Pendaftaran
from exceptions import PendaftaranError, InvalidInputError, AuthenticationError

app = Flask(__name__)
app.secret_key = 'unida_gontor_secret_key'

# Inisialisasi Admin Utama & Data Dummy
admin_utama = Admin("Admin PMB UNIDA", "Gontor, Ponorogo", "081234567890", "admin", "admin123")

# Pre-populate data awal
mhs_demo = Mahasiswa("Baihaqi Alwi Mahmudi", "Ngawi", "081299998888", "REG-2026-001", "PP Modern Darussalam Gontor", "Teknik Informatika")
pendaftaran_demo = Pendaftaran(mhs_demo)
pendaftaran_demo.simpanData()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pendaftaran', methods=['GET', 'POST'])
def pendaftaran():
    if request.method == 'POST':
        try:
            nama = request.form.get('nama')
            alamat = request.form.get('alamat')
            telp = request.form.get('telp')
            asal_sekolah = request.form.get('asal_sekolah')
            prodi = request.form.get('prodi')

            if not nama or not telp or not asal_sekolah:
                raise InvalidInputError("Semua bidang bertanda bintang wajib diisi!")

            # Generate Nomor Pendaftaran Otomatis
            no_pendaftaran = f"REG-2026-{random.randint(100, 999)}"

            # Instansiasi Objek
            mhs = Mahasiswa(nama, alamat, telp, no_pendaftaran, asal_sekolah, prodi)
            pembukuan = Pendaftaran(mhs)
            pembukuan.simpanData()

            flash(f"Pendaftaran Berhasil! Nomor Pendaftaran Anda: {no_pendaftaran}", "success")
            return redirect(url_for('status', no_reg=no_pendaftaran))

        except PendaftaranError as e:
            flash(str(e), "danger")
        except Exception as e:
            flash(f"Terjadi kesalahan sistem: {str(e)}", "danger")

    return render_template('pendaftaran.html')

@app.route('/status', methods=['GET', 'POST'])
def status():
    hasil = None
    no_reg_query = request.args.get('no_reg', '')

    if request.method == 'POST':
        no_reg_query = request.form.get('no_pendaftaran', '')

    if no_reg_query:
        for p in Pendaftaran._daftar_pendaftaran:
            if p.mahasiswa.get_no_pendaftaran() == no_reg_query:
                hasil = p.tampilData()
                break
        if not hasil:
            flash("Data pendaftaran tidak ditemukan!", "warning")

    return render_template('status.html', hasil=hasil, query=no_reg_query)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            if admin_utama.login(username, password):
                flash("Login Admin Berhasil!", "success")
                return redirect(url_for('admin_dashboard'))

        except AuthenticationError as e:
            flash(str(e), "danger")

    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    # Filter/Search & Verifikasi Data
    search_query = request.args.get('search', '')
    pendaftar_list = [p.tampilData() for p in Pendaftaran._daftar_pendaftaran]

    if search_query:
        pendaftar_list = [
            p for p in pendaftar_list 
            if search_query.lower() in p['nama'].lower() 
            or search_query.lower() in p['no_pendaftaran'].lower()
            or search_query.lower() in p['prodi'].lower()
        ]

    return render_template('admin.html', pendaftar_list=pendaftar_list, search_query=search_query)

@app.route('/admin/verifikasi/<no_reg>', methods=['POST'])
def verifikasi(no_reg):
    status_baru = request.form.get('status')
    try:
        for p in Pendaftaran._daftar_pendaftaran:
            if p.mahasiswa.get_no_pendaftaran() == no_reg:
                p.verifikasiData(status_baru)
                flash(f"Status {no_reg} berhasil diperbarui menjadi {status_baru}!", "info")
                break
    except PendaftaranError as e:
        flash(str(e), "danger")

    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)