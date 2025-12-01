from flask import Blueprint, render_template, session, redirect
from app.models.pemesanan_model import PemesananModel
from app.models.meja_model import MejaModel

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect('/pengguna')

@main.route('/dashboard')
def dashboard():
    if 'admin_logged_in' not in session:
        return redirect('/login')

    pemesanan = PemesananModel.get_all()
    meja = MejaModel.get_all()

    return render_template(
        'dashboard.html',
        pemesanan=pemesanan,
        meja=meja,
        admin_name=session.get('admin_name')
    )
