# bot/database.py

import sqlite3
import os


class DatabaseManager:

    def __init__(self):
        self.db_path = os.path.join("DB", "iris_nova.db")
        self._ensure_database()

    def _ensure_database(self):
        """
        Crea la base de datos si no existe.
        """
        if not os.path.exists("DB"):
            os.makedirs("DB")

        conn = sqlite3.connect(self.db_path)
        conn.close()

        print(f"[DB] Base de datos lista en {self.db_path}")

    def get_connection(self):
        """
        Retorna una nueva conexión a la base de datos.
        """
        return sqlite3.connect(self.db_path)