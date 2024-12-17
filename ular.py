from animal import * 

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("design \t\t\t\t\t: ", self.design,
              "\nracun \t\t\t\t\t: ", self.racun)


anaconda1 = ular("anaconda", "kambing", "amazon", "bertelur", "batik solo", "tidak berbisa")
anaconda1.cetak_ular()

anaconda2 = ular("python", "hewan", "hutan", "bertelur", "campuran", "berbisa")
anaconda2.cetak_ular()
