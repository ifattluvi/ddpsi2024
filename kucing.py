from animal import * 

class kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna 
    def cetak_kucing(self):
        super().cetak()
        print("\njenis \t\t\t\t\t: ", self.jenis,
              "\nwarna \t\t\t\t\t: ", self.warna)


kucing1 = kucing("coki", "dry food", "darat", "melahirkan", "anggora", "oyen")
kucing1.cetak_kucing()

kucing3 = kucing("lomi", "daging mentah", "darat", "melahirkan", "savana", "abu")
kucing3.cetak_kucing()

