class LibraryItem:
    def __init__(self, title, item_id, is_checked_out=False):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = is_checked_out


class Book(LibraryItem):
    def __init__(self, title, item_id, author, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.author = author

    def get_info(self):
        status = "🔴 Checked Out" if self.is_checked_out else "🟢 Available"
        return f"{self.item_id} | {self.title} | {self.author} | {status}"
