from flask import Blueprint, render_template, request, redirect, session, flash
from app.models.admin_model import AdminModel
from app.database import get_db
from app.models.meja_model import MejaModel
from app.models.pemesanan_model import PemesananModel

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login admin"""
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        admin_data = AdminModel.login(user, pw)

        if admin_data:
            """Login berhasil"""
            session['admin_logged_in'] = True
            session['admin_name'] = admin_data['username']
            return redirect('/dashboard')
        else:
            flash("Login gagal!")

    return render_template('login.html')

@admin.route('/logout')
def logout():
    """Logout admin"""
    session.clear()
    return redirect('/pengguna')

@admin.route('/dashboard')
def dashboard():
    """Halaman dashboard admin"""
    if 'admin_logged_in' not in session:
        return redirect('/login')

    # Ambil data
    pemesanan = PemesananModel.get_all()
    meja = MejaModel.get_all()

    # Render halaman dashboard
    return render_template(
        'dashboard.html',
        pemesanan=pemesanan,
        meja=meja,
        admin_name=session.get('admin_name')
    )


@admin.route('/ubah_status_meja', methods=['POST'])
def ubah_status_meja():
    """Ubah status meja"""
    if 'admin_logged_in' not in session:
        return redirect('/login')

    id_meja = request.form['id_meja']
    status_baru = request.form['status']

    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE meja SET status=%s WHERE id_meja=%s", (status_baru, id_meja))
    db.commit()

    return redirect('/dashboard')

@admin.route('/pemesanan/<int:id>/struk')
def struk(id):
    """Tampilkan struk pemesanan"""
    if 'admin_logged_in' not in session:
        return redirect('/login')

    from app.models.pemesanan_model import PemesananModel
    data = PemesananModel.get_by_id(id)

    if not data:
        return "Data tidak ditemukan"

    return render_template('struk.html', p=data)

@admin.route('/pemesanan/<int:id>/hapus', methods=['POST'])
def hapus_pemesanan(id):
    """Hapus pemesanan dan kosongkan meja"""
    if 'admin_logged_in' not in session:
        return redirect('/login')

    from app.models.pemesanan_model import PemesananModel
    from app.database import get_db

    # ambil meja yg digunakan transaksi
    data = PemesananModel.get_meja_by_pemesanan(id)

    if data:
        id_meja = data['id_meja']

        # hapus transaksi
        PemesananModel.delete(id)

        # kosongkan meja (update status)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE meja SET status='Kosong' WHERE id_meja=%s", (id_meja,))
        db.commit()

    return redirect('/dashboard')

