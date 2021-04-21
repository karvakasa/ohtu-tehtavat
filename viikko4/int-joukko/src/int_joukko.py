KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            self.alkioiden_lkm -= 1
        
    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu
        
    @staticmethod
    def yhdiste(aJoukko, bJoukko):
        a_taulu, yhdisteJoukko, b_taulu = IntJoukko.alustus(aJoukko, bJoukko)

        for i in range(0, len(a_taulu)):
            yhdisteJoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdisteJoukko.lisaa(b_taulu[i])

        return yhdisteJoukko

    @staticmethod
    def leikkaus(aJoukko, bJoukko):
        a_taulu, leikkausJoukko, b_taulu = IntJoukko.alustus(aJoukko, bJoukko)

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkausJoukko.lisaa(b_taulu[j])

        return leikkausJoukko

    @staticmethod
    def erotus(aJoukko, bJoukko):
        a_taulu, erotusJoukko, b_taulu = IntJoukko.alustus(aJoukko, bJoukko)

        for i in range(0, len(a_taulu)):
            erotusJoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotusJoukko.poista(b_taulu[i])

        return erotusJoukko

    @staticmethod
    def alustus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        return a_taulu, z, b_taulu

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos