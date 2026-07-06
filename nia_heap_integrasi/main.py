# digunakan untuk menyatukan semua modul menjadi satu sistem

from order import Order
from queue_module import Queue
from stack_module import Stack
from bst_module import BST
from heap_module import BinaryHeap

class SistemLaundry:
    def __init__(self):
        self.antrean_masuk = Queue()
        self.data_aktif = BST()
        self.jadwal = BinaryHeap()
        self.riwayat = Stack()
        self.id_berikutnya = 1

    def terima_order_baru(self, nama, jenis_layanan, berat_kg):
        order = Order(self.id_berikutnya, nama, jenis_layanan, berat_kg)
        self.id_berikutnya += 1
        self.antrean_masuk.enqueue(order)
        print(f"Order baru masuk antrean: {order}")

    def proses_dari_antrean(self):
        order = self.antrean_masuk.dequeue()

        if order is None:
            print("Antrean masih kosong.")
            return

        self.data_aktif.insert(order)
        self.jadwal.insert(order)

    print(f"Order diproses admin: {order}")
    
    def kerjakan_prioritas_tertinggi(self):
        order = self.jadwal.delete_root()

        if order is None:
            print("Tidak ada order yang siap dikerjakan.")
            return

        order.status = "Sedang Dicuci"
        print(f"Order sedang dikerjakan: {order}")

    def selesaikan_order(self, order_id):
        order = self.data_aktif.search(order_id)
        if order is None:
            print(f"Order #{order_id} tidak ditemukan di data aktif...")
            return
        order.status = "Selesai"
        self.data_aktif.delete(order_id)
        self.riwayat.push(order)
        print(f"Order #{order_id} selesai, masuk ke dalam riwayat: {order}")

    def undo_riwayat_terakhir(self):
        order = self.riwayat.pop()
        if order is None:
            print("Riwayat kosong, tidak ada yang dapat di undo")
            return
        print("Riwayat terakhir dibatalkan: {order}")

    def cari_order(self, order_id):
        order = self.data_aktif.search(order_id)
        if order is None:
            print(f"Order #{order_id} tidak ada di data order aktif")
        else:
            print(f"Ditemukan: {order}")
    
    def tampilkan_order_aktif(self):
        print("Daftar order aktif (urut ID, hasil inorder BST):")
        self.data_aktif.display()

    def tampilkan_antrean_masuk(self):
        print("Antrean order yang belum diproses:")
        self.antrean_masuk.display()

    def tampilkan_jadwal(self):
        print("Antrean prioritas pengerjaan (heap):")
        self.jadwal.display()

    def tampilkan_riwayat(self):
        print("Riwayat order (stack, paling atas = paling baru):")
        self.riwayat.display()

    def info_tree(self):
        print(f"Tinggi BST: {self.data_aktif.height()}")
        print(f"Jumlah node aktif: {self.data_aktif.count_nodes()}")
    
def cetak_menu():
    print("\n===== SISTEM LAUNDRY KILAT BERSIH =====")
    print("1.  Terima order baru (Queue)")
    print("2.  Proses order dari antrean (Queue -> BST & Heap)")
    print("3.  Kerjakan order prioritas tertinggi (Heap)")
    print("4.  Selesaikan order (BST -> Stack)")
    print("5.  Undo riwayat terakhir (Stack)")
    print("6.  Cari order by ID (BST)")
    print("7.  Tampilkan semua order aktif (BST - inorder)")
    print("8.  Tampilkan antrean masuk (Queue)")
    print("9.  Tampilkan antrean prioritas (Heap)")
    print("10. Tampilkan riwayat (Stack)")
    print("11. Info BST (tinggi & jumlah node)")
    print("0.  Keluar")

def main():
    sistem = SistemLaundry()
    while True:
        cetak_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nama = input("Nama pelanggan: ")
            jenis = input("Jenis layanan (Express/Reguler/cuci_kering): ")
            try:
                berat = float(input("Berat cucian (kg): "))
            except ValueError:
                print("Beratnya harus angka.")
                continue
            sistem.terima_order_baru(nama, jenis, berat)

        elif pilihan == "2":
            sistem.proses_dari_antrean()

        elif pilihan == "3":
            sistem.kerjakan_prioritas_tertinggi()

        elif pilihan == "4":
            try:
                oid = int(input("Order ID yang selesai: "))
            except ValueError:
                print("ID harus angka.")
                continue
            sistem.selesaikan_order(oid)

        elif pilihan == "5":
            sistem.undo_riwayat_terakhir()

        elif pilihan == "6":
            try:
                oid = int(input("Order ID yang dicari: "))
            except ValueError:
                print("ID harus angka.")
                continue
            sistem.cari_order(oid)

        elif pilihan == "7":
            sistem.tampilkan_order_aktif()

        elif pilihan == "8":
            sistem.tampilkan_antrean_masuk()

        elif pilihan == "9":
            sistem.tampilkan_jadwal()

        elif pilihan == "10":
            sistem.tampilkan_riwayat()

        elif pilihan == "11":
            sistem.info_tree()

        elif pilihan == "0":
            print("Terima kasih sudah menggunakan jasa laundry Kilat Bersih!")
            break

        else:
            print("Menu tidak tersedia, silahkan pilih menu yang lain")


if __name__ == "__main__":
    main()
