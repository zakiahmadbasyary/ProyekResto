# tests/conftest.py
import sys
import os
import pytest

# --- PENTING: pastikan parent folder proyek ada di sys.path dulu ---
# Menambahkan parent directory (ProyekResto) supaya import "app" berhasil.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Sekarang aman mengimpor create_app dari paket app
from app import create_app

@pytest.fixture(scope="session")
def app():
    """Buat instance Flask app untuk sesi test."""
    app = create_app()
    return app

@pytest.fixture(scope="session")
def app_context(app):
    """Jalankan application context untuk semua test yang butuh context."""
    with app.app_context():
        yield
