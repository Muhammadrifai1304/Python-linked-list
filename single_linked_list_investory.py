class Node:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Node(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.code == code:
                current.next = current.next.next
                return
            current = current.next

