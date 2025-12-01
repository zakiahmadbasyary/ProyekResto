from app.database import get_db

class MejaModel:
    """ Model untuk Meja """
    
    @staticmethod
    def get_all():
        """ Mengambil semua data meja dari database """
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM meja ORDER BY id_meja ASC")
        return cursor.fetchall()
