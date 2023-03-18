# biblioteki z wykresami
import matplotlib.pyplot as plt
import numpy as np
from Konsola import Konsola


class LiczenieWyjscia:
    def __init__(self, konsola):
        self.sygnal = konsola.sygnal
        self.a = konsola.a
        self.b = konsola.b
        self.ileElem = 10000
        self.h = 0.001                     # skok programu
        self.us = []
        self.Ampli = konsola.Ampli         #amplituda
        self.t = []
        self.w = konsola.w                 # pulsacja
        self.y = []  

    def listaWarSin(self):
        for i in range(0, self.ileElem):
            self.us.insert(i, self.Ampli * np.sin(self.w * i * self.h))
            self.t.insert(i, i * self.h)

    def listaWarSkok(self):
        for i in range(0, self.ileElem):
            self.us.insert(i, self.Ampli)
            self.t.insert(i, i * self.h)

    def listaWarFala(self):
        for i in range(0, self.ileElem):
            self.us.insert(i, self.Ampli * np.sign(np.sin(self.w * i * self.h)))
            self.t.insert(i, i * self.h)

    def rozwRowRoz(self):                                                                   #metoda Eulera
        macierzA = np.array([[0, 0, -self.a[0]], [1, 0, -self.a[1]], [0, 1, -self.a[2]]])
        macierzB = np.array([[self.b[0] - (self.a[0] * self.b[3])], [self.b[1] - (self.a[1] * self.b[3])],
                             [self.b[2] - (self.a[2] * self.b[3])]])
        macierzC = np.array([0, 0, 1])
        macierzD = self.b[3]
        wektorXpoprz = np.array([[0], [0], [0]])
        self.y = np.ones(self.ileElem)

        # dot to mnożenie dwóch macierzy
        for i in range(0, self.ileElem):
            Ax = np.dot(macierzA, wektorXpoprz)
            Bu = macierzB * self.us[i]
            Cx = np.dot(macierzC, wektorXpoprz)
            Du = macierzD * self.us[i]
            wektorX = Ax + Bu
            wektorX = wektorX * self.h
            wektorX = wektorXpoprz + wektorX
            wektorXpoprz = wektorX

            CxDu = Cx + Du
            self.y[i] = CxDu
