from app.database import get_db

class PemesananModel:

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pr.nama AS nama_produk
            FROM pemesanan p
            JOIN produk pr ON p.id_produk = pr.id_produk
            ORDER BY p.id_pemesanan DESC
        """)
        return cursor.fetchall()

    @staticmethod
    def tambah(nama, nohp, id_meja, id_produk, id_admin):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO pemesanan (nama_pelanggan, nohp_pelanggan, id_meja, id_produk, id_admin)
            VALUES (%s, %s, %s, %s, %s)
        """, (nama, nohp, id_meja, id_produk, id_admin))
        db.commit()

    @staticmethod
    def get_by_id(id_pemesanan):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pr.nama AS nama_produk, pr.harga
            FROM pemesanan p
            JOIN produk pr ON p.id_produk = pr.id_produk
            WHERE p.id_pemesanan = %s
        """, (id_pemesanan,))
        return cursor.fetchone()

