import numpy
import numpy.linalg

class Macierz_LU():
    def __init__(self, wiersze, kolumny):
        self.x = wiersze
        self.y = kolumny

    def podaj_macierz(self, *args):
        self.A = numpy.asarray(args).reshape(self.x, self.y)