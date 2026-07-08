# demo buat ngetes bst_module sendiri sebelum digabung

from order import Order
from bst_module import BST

data_aktif = BST()

for i, (nama, jenis, berat) in enumerate([
    ("Budi", "reguler", 3),
    ("Ani", "express", 2),
    ("Cici", "cuci_kering", 1),
    ("Dedi", "express", 5),
    ("Eka", "reguler", 4),
], start=1):
    data_aktif.insert(i, Order(i, nama, jenis, berat))

print("daftar order aktif (inorder, harusnya urut ID 1-5):")
data_aktif.display()

print("\ntinggi tree:", data_aktif.height())
print("jumlah node:", data_aktif.count_nodes())

print("\ncari order id 3:", data_aktif.search(3))
print("cari order id 99 (ga ada):", data_aktif.search(99))

print("\nhapus order id 2 (Ani)...")
data_aktif.delete(2)
data_aktif.display()
print("jumlah node setelah delete:", data_aktif.count_nodes())