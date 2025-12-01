from app.database import get_db

class MejaModel:

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM meja ORDER BY id_meja ASC")
        return cursor.fetchall()
