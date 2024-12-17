from animal import * 

class ayam(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.suara = suara
    def cetak_ayam(self):
        super().cetak()
        print("\njenis \t\t\t\t\t: ", self.jenis,
              "\nsuara \t\t\t\t\t: ", self.suara)


ayam1 = ayam("ayam hutan", "pur", "hutan", "bertelur", "ayam jantan", "kukuruyukk")
ayam1.cetak_ayam()

ayam2 = ayam("ayam serama", "buah", "hutan", "bertelur", "ayam jantan", "uuuuuuu")
ayam2.cetak_ayam()
