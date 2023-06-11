class Node:
    def _init_(self, visitor_name, book_title):
        self.visitor_name = visitor_name
        self.book_title = book_title
        self.next = None


class LibraryRecords:
    def _init_(self):
        self.head = None

    def borrow_book(self, visitor_name, book_title):
        new_record = Node(visitor_name, book_title)
        if self.head is None:
            self.head = new_record
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_record

    def print_records(self):
        if self.head is None:
            print("Daftar peminjaman kosong.")
        else:
            current = self.head
            while current is not None:
                print("Pengunjung:", current.visitor_name, "| Judul Buku:", current.book_title)
                current = current.next


# Contoh penggunaan program

library_records = LibraryRecords()

library_records.print_records()  # Output: Daftar peminjaman kosong.

library_records.borrow_book("Rina", "Harry Potter")
library_records.borrow_book("Yudi", "The Lord of the Rings")
library_records.borrow_book("Rina", "To Kill a Mockingbird")

library_records.print_records()
# Output:
# Pengunjung: Rina | Judul Buku: Harry Potter
# Pengunjung: Yudi | Judul Buku: The Lord of the Rings
# Pengunjung: Rina | Judul Buku: To Kill a Mockingbird