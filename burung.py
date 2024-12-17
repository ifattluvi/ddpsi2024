from animal import * 

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("\njenis \t\t\t\t\t: ", self.jenis,
              "\nbunyi \t\t\t\t\t: ", self.bunyi)


burung1 = burung("merpati", "biji bijian", "sangkar", "bertelur", "merpati putih", "cikcikcik")
burung1.cetak_burung()

burung2 = burung("merak", "biji bijian", "kandang", "bertelur", "merak hijau", "utsutsust")
burung2.cetak_burung()
