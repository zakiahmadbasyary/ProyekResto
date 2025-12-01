from flask import Blueprint, render_template, request, redirect
from app.models.meja_model import MejaModel
from app.models.produk_model import ProdukModel
from app.models.pemesanan_model import PemesananModel

pengguna = Blueprint('pengguna', __name__)

@pengguna.route('/pengguna')
def halaman_pengguna():
    pemesanan = PemesananModel.get_all()
    meja = MejaModel.get_all()
    produk = ProdukModel.get_all()

    return render_template(
        'pengguna/home.html',
        pemesanan=pemesanan,
        meja=meja,
        produk=produk
    )

@pengguna.route('/pengguna/pesan', methods=['POST'])
def proses_pemesanan():
    nama = request.form['nama']
    nohp = request.form['nohp']
    id_meja = request.form['id_meja']
    id_produk = request.form['id_produk']
    id_admin = 1  # default admin

    PemesananModel.tambah(nama, nohp, id_meja, id_produk, id_admin)

    # Update status meja
    from app.database import get_db
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE meja SET status='Terisi' WHERE id_meja=%s", (id_meja,))
    db.commit()

    return redirect('/pengguna')
