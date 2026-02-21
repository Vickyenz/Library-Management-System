import sqlite3
from library.models import Book

DB_NAME = "library.db"

class LibraryService:
    def __init__(self):
        self._init_db()

    def _connect(self):
        return sqlite3.connect(DB_NAME)

    def _init_db(self):
        with self._connect() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id TEXT PRIMARY KEY,
                title TEXT,
                author TEXT,
                checked_out INTEGER
            )
            """)

    def add_item(self, title, item_id, author):
        try:
            with self._connect() as conn:
                conn.execute(
                    "INSERT INTO books VALUES (?, ?, ?, ?)",
                    (item_id, title, author, 0),
                )
            return f"Added '{title}'."
        except sqlite3.IntegrityError:
            return "Error: ID already exists."

    def remove_item(self, item_id):
        with self._connect() as conn:
            cur = conn.execute("DELETE FROM books WHERE id=?", (item_id,))
            if cur.rowcount == 0:
                return "Error: Book not found."
        return "Book deleted."

    def toggle_status(self, item_id):
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT checked_out, title FROM books WHERE id=?",
                (item_id,),
            )
            row = cur.fetchone()

            if not row:
                return "Error: Book not found."

            new_status = 0 if row[0] else 1

            conn.execute(
                "UPDATE books SET checked_out=? WHERE id=?",
                (new_status, item_id),
            )

        status_text = "checked out" if new_status else "available"
        return f"'{row[1]}' is now {status_text}."

    def display_all(self):
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM books").fetchall()

        if not rows:
            return "Library empty."

        books = [
            Book(title, item_id, author, checked_out)
            for item_id, title, author, checked_out in rows
        ]

        return "\n".join(book.get_info() for book in books)
