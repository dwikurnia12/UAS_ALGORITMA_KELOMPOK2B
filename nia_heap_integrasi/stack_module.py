# Dikerjakan oleh Abid Satriyo Maulana (K3525045)

class NodeStack:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.jumlah = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        node = NodeStack(data)
        node.next = self.top
        self.top = node
        self.jumlah += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self.top
        self.top = node.next
        self.jumlah -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        return self.jumlah

    def display(self):
        if self.is_empty():
            print("  (belum ada riwayat)")
            return
        curr = self.top
        i = 1
        while curr:
            print(f"  {i}. {curr.data}")
            curr = curr.next
            i += 1
