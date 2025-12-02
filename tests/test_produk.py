import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.produk_model import ProdukModel

def test_produk_get_all(app_context):
    data = ProdukModel.get_all()
    assert isinstance(data, list)

def test_produk_get_by_id(app_context):
    result = ProdukModel.get_by_id(1)
    assert result is None or isinstance(result, dict)
