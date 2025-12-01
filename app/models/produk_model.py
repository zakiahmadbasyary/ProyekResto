from app.database import get_db

class ProdukModel:
    """ Model untuk Produk """
    
    @staticmethod
    def get_all():
        """ Mengambil semua data produk dari database """
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produk")
        return cursor.fetchall()

    
    @staticmethod
    def get_by_id(id_produk):
        """ Mengambil data produk berdasarkan ID """
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produk WHERE id_produk=%s", (id_produk,))
        return cursor.fetchone()
