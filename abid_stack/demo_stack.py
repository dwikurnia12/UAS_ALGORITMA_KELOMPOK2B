# Dikerjakan oleh Abid Satriyo Maulana (K3525045)
from order import Order
from stack_module import Stack

riwayat = Stack()

o1 = Order(1, "Budi", "reguler", 3)
o1.status = "Selesai"
o2 = Order(2, "Ani", "express", 2)
o2.status = "Selesai"

riwayat.push(o1)
riwayat.push(o2)

print("isi riwayat (paling atas = paling baru):")
riwayat.display()

print("\npeek:", riwayat.peek())

print("\npop (undo) satu kali:")
dibatalin = riwayat.pop()
print(" yang di-undo:", dibatalin)

print("\nsisa riwayat:")
riwayat.display()
