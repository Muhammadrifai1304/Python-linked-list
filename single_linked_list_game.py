# Definisikan class Node untuk merepresentasikan setiap item
class Node:
    def _init_(self, nama, kepentingan):
        self.nama = nama
        self.kepentingan = kepentingan
        self.next = None

# Definisikan class LinkedList untuk merepresentasikan tas
class LinkedList:
    def _init_(self):
        self.head = None

    # Method untuk menambahkan item ke dalam tas
    def tambah_item(self, nama, kepentingan):
        new_item = Node(nama, kepentingan)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    # Method untuk menghapus item dari tas
    def hapus_item(self, nama):
        current = self.head
        previous = None
        while current:
            if current.nama == nama:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        print("Item tidak ditemukan dalam tas.")

    # Method untuk mencetak daftar item berdasarkan tingkat kepentingan
    def cetak_daftar_item(self):
        if self.head is None:
            print("Tas kosong.")
        else:
            current = self.head
            while current:
                print("Nama: {}, Kepentingan: {}".format(current.nama, current.kepentingan))
                current = current.next

# Membuat objek LinkedList untuk merepresentasikan tas
tas = LinkedList()

# Menambahkan item ke dalam tas
tas.tambah_item("Buku", 3)
tas.tambah_item("Pisau", 5)
tas.tambah_item("Peta", 2)
tas.tambah_item("Obat", 4)

# Mencetak daftar item
tas.cetak_daftar_item()
print()

# Menghapus item
tas.hapus_item("Pisau")
tas.hapus_item("Pulpen")

# Mencetak daftar item setelah penghapusan
tas.cetak_daftar_item()