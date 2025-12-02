import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.meja_model import MejaModel

def test_meja_get_all(app_context):
    data = MejaModel.get_all()
    assert isinstance(data, list)
