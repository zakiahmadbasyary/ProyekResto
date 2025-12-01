from app.database import get_db

class ProdukModel:

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produk")
        return cursor.fetchall()

    @staticmethod
    def get_by_id(id_produk):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produk WHERE id_produk=%s", (id_produk,))
        return cursor.fetchone()
