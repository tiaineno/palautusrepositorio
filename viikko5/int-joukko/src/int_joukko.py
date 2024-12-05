KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko: int = OLETUSKASVATUS):

        if kapasiteetti < 0:
            raise ValueError("kapasiteetin on oltava positiivinen kokonaisluku")
        self.kapasiteetti = kapasiteetti

        if kasvatuskoko < 0:
            raise ValueError("kasvatuskoon on oltava positiivinen kokonaisluku")
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        if self.alkioiden_lkm < self.kapasiteetti:
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        
        uusi_lista = (self.kapasiteetti + self.kasvatuskoko) * [0]

        self.kapasiteetti += self.kasvatuskoko
        self.kopioi_lista(self.lukujono, uusi_lista)
        self.lukujono = uusi_lista
        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm +=1

        return True

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
    
    def kopioi_lista(self, a, b):
        b[: len(a)] = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        return "{" + ", ".join(map(str, self.lukujono[:self.alkioiden_lkm])) + "}"
