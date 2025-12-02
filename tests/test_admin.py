import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.admin_model import AdminModel

def test_login_wrong(app_context):
    result = AdminModel.login("salah", "password")
    assert result is None

def test_login_correct(app_context):
    result = AdminModel.login("admin", "admin")
    assert isinstance(result, dict)
