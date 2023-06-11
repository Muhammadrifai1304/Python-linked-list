class Node:
    def _init_(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class TaskList:
    def _init_(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            if priority > current.priority:
                new_task.next = self.head
                self.head = new_task
            else:
                while current.next is not None and current.next.priority >= priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return
        if self.head.description == description:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.description != description:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
        else:
            current = self.head
            print("Daftar tugas:")
            while current is not None:
                print("Deskripsi:", current.description, "| Prioritas:", current.priority)
                current = current.next


# Contoh penggunaan program

task_list = TaskList()

task_list.print_tasks()  # Output: Daftar tugas kosong.

task_list.add_task("Mengerjakan tugas matematika", 2)
task_list.add_task("Membaca buku", 1)
task_list.add_task("Berolahraga", 3)

task_list.print_tasks()
# Output:
# Daftar tugas:
# Deskripsi: Berolahraga | Prioritas: 3
# Deskripsi: Mengerjakan tugas matematika | Prioritas: 2
# Deskripsi: Membaca buku | Prioritas: 1

task_list.remove_task("Mengerjakan tugas matematika")

task_list.print_tasks()
# Output:
# Daftar tugas:
# Deskripsi: Berolahraga | Prioritas: 3
# Deskripsi: Membaca buku | Prioritas: 1