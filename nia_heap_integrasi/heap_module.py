class BinaryHeap:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0
    
    def size(self):
        return len (self.arr)
    
    def _menang(self, a, b):
        # true jika order a harus dikerjakan lebih dulu dari b
        if a.prioritas != b.prioritas:
            return a.prioritas < b.prioritas
        return a.order_id < b.order_id
    
    def insert(self, order):
        self.arr.append(order)
        self._heapify_up(len(self.arr) - 1)

    def _heapify_up(self,i):
        while i > 0:
            parent = (i - 1) // 2
            if self._menang(self.arr[i], self.arr[parent]):
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i =  parent
            else:
                break
    def delete_root(self):
        if self.is_empty():
            return None
        root = self.arr[0]
        terakhir = self.arr.pop()
        if self.arr:
            self.arr[0] = terakhir
            self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        n = len(self.arr)
        while True:
            kiri, kanan = 2 * i + 1, 2 * i + 2
            terkecil = i
            if kiri < n and self._menang(self.arr[kiri], self.arr[terkecil]):
                terkecil = kiri
            if kanan < n and self._menang(self.arr[kanan], self.arr[terkecil]):
                terkecil = kanan
            if terkecil == i:
                break
            self.arr[i], self.arr[terkecil] = self.arr[terkecil], self.arr[i]
            i= terkecil

    def peek(self):
        if self.is_empty():
            return None
        return self.arr[0]
    
    def display(self):
        if self.is_empty():
            print("(antrean prioritas kosong)")
            return
        for i, order in enumerate(self.arr):
            keterangan = "<-next dikerjakan" if i == 0 else ""
            print(f" [{i} {order}{keterangan}]")

