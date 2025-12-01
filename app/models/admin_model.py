from app.database import get_db

class AdminModel:
    """ Model untuk Admin"""
    
    @staticmethod
    def login(username, password):
        """ Melakukan pengecekan login admin berdasarkan username dan password. """
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s",
                       (username, password))
        # Mengembalikan satu baris data atau None
        return cursor.fetchone()
