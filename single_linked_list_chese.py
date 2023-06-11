class Node:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.next = None


class ParticipantList:
    def __init__(self):
        self.head = None

    def add_participant(self, name, rating):
        new_participant = Node(name, rating)
        if self.head is None:
            self.head = new_participant
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_participant

    def remove_loser(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def print_participants_by_rating(self):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        participants = []
        current = self.head
        while current is not None:
            participants.append((current.name, current.rating))
            current = current.next

        participants.sort(key=lambda x: x[1], reverse=True)

        print("Daftar peserta berdasarkan peringkat:")
        for participant in participants:
            print("Nama: {}, Peringkat: {}".format(participant[0], participant[1]))


# Contoh penggunaan program
turnamen_chess = ParticipantList()

# Menambahkan peserta
turnamen_chess.add_participant("John", 1500)
turnamen_chess.add_participant("Alice", 1800)
turnamen_chess.add_participant("Bob", 1700)
turnamen_chess.add_participant("Charlie", 1600)

# Mencetak daftar peserta berdasarkan peringkat
turnamen_chess.print_participants_by_rating()

# Menghapus peserta yang telah kalah
turnamen_chess.remove_loser("Charlie")

# Mencetak daftar peserta setelah penghapusan
turnamen_chess.print_participants_by_rating()
