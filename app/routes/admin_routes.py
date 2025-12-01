from flask import Blueprint, render_template, request, redirect, session, flash
from app.models.admin_model import AdminModel
from app.database import get_db

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        admin_data = AdminModel.login(user, pw)

        if admin_data:
            session['admin_logged_in'] = True
            session['admin_name'] = admin_data['username']
            return redirect('/dashboard')
        else:
            flash("Login gagal!")

    return render_template('login.html')

@admin.route('/logout')
def logout():
    session.clear()
    return redirect('/pengguna')

@admin.route('/ubah_status_meja', methods=['POST'])
def ubah_status_meja():
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
    if 'admin_logged_in' not in session:
        return redirect('/login')

    from app.models.pemesanan_model import PemesananModel
    data = PemesananModel.get_by_id(id)

    if not data:
        return "Data tidak ditemukan"

    return render_template('struk.html', p=data)

