from flask import Blueprint, render_template, session, redirect



main = Blueprint('main', __name__)

@main.route('/')
def home():
    """redirect ke Halaman utama pengguna"""
    return redirect('/pengguna')


