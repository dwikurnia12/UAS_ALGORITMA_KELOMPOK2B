from order import Order
from queue_module import Queue

antrean = Queue()

antrean.enqueue(Order(1, "Budi", "reguler", 3))
antrean.enqueue(Order(2, "Ani", "express", 2))
antrean.enqueue(Order(3, "Cici", "cuci_kering", 1))

print("isi antrean sekarang:")
antrean.display()

print("\npeek (liat depan doang, ga dihapus):", antrean.peek())

print("\ndequeue satu-satu:")
while not antrean.is_empty():
    order = antrean.dequeue()
    print(" keluar:", order)

print("\nsisa antrean:")
antrean.display()