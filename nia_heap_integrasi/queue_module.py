# QUEUE - buat nampung order yang baru masuk sebelum diproses admin
# dibikin manual pake linked list, ga boleh pake collections.deque
# anggota 1

class NodeQueue:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # paling depan, ini yang keluar duluan
        self.tail = None  # paling belakang, tempat nambah data baru
        self.jumlah = 0

    def is_empty(self):
        return self.jumlah == 0

    def enqueue(self, data):
        node = NodeQueue(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.jumlah += 1

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self.jumlah -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        return self.jumlah

    def display(self):
        if self.is_empty():
            print("  (antrean kosong)")
            return
        curr = self.head
        no = 1
        while curr:
            print(f"  {no}. {curr.data}")
            curr = curr.next
            no += 1