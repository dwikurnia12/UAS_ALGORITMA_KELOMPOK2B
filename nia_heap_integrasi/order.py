from datetime import datetime

# level prioritas untuk digunakan di heap nanti, semakin kecil semakin diprioritaskan

PRIORITAS_LAYANAN = {
    "Express": 1,
    "Reguler": 2,
    "cuci_kering": 3,
}

class Order:
    def __init__(self,order_id, nama_pelanggan, jenis_layanan, berat_kg):
        self.order_id = order_id
        self.nama_pelanggan =  nama_pelanggan
        self.jenis_layanan = jenis_layanan.lower().strip()
        self.berat_kg = berat_kg
        self.prioritas = PRIORITAS_LAYANAN.get(self.jenis_layanan, 2)
        self.status = "Menunggu Antrean"
        self.waktu_masuk = datetime.now().strftime("%H:%M:%S")

    def estimasi_biaya(self):
        harga_per_kg = {"Express": 10000, "Reguler": 6000, "cuci_kering": 7000}
        tarif = harga_per_kg.get(self.jenis_layanan, 6000)
        total = tarif * self.berat_kg
        if self.jenis_layanan == "Express":
            total += 5000
        return total
    
    def __str__(self):
        return (f"[#{self.order_id}]{self.nama_pelanggan} - {self.jenis_layanan_upper()}"
                f"({self.berat_kg}kg) | prioritas={self.prioritas} | {self.status} | jam {self.waktu_masuk}")