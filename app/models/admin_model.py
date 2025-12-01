from app.database import get_db

class AdminModel:

    @staticmethod
    def login(username, password):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s",
                       (username, password))
        return cursor.fetchone()
