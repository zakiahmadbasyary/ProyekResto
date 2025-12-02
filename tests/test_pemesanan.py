import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.pemesanan_model import PemesananModel

def test_pemesanan_get_all(app_context):
    data = PemesananModel.get_all()
    assert isinstance(data, list)

def test_pemesanan_get_by_id(app_context):
    result = PemesananModel.get_by_id(1)
    assert result is None or isinstance(result, dict)

def test_pemesanan_get_meja_by_pemesanan(app_context):
    meja = PemesananModel.get_meja_by_pemesanan(1)
    assert meja is None or isinstance(meja, dict)
