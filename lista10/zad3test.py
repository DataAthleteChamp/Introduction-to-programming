import unittest
import numpy
import numpy.linalg
import scipy.linalg
import zadanie3

class Test_LU(unittest.TestCase):
    def setUp(self):
        self.macierz = zadanie3.Macierz_LU(2,2)
        self.macierz.podaj_macierz(0,1,5,0) #ta nie jest LU-decomposible
        #self.macierz.podaj_macierz(2,1,0,3) #ta jest LU-decomposible
        self.P, self.L, self.U = scipy.linalg.lu(self.macierz.A)

    def test_if_macierz_kwadratowa(self):
        self.assertEqual(self.macierz.x, self.macierz.y)

    def test_if_wyznacznik_różny_zero(self):
        self.assertNotEqual(numpy.linalg.det(self.macierz.A), 0)

    def test_if_L_razy_U_równa_się_A(self):
        self.assertEqual(numpy.array_equal(self.macierz.A, numpy.matmul(self.L, self.U)), True)