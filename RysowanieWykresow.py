import matplotlib.pyplot as plt
import numpy as np
from LiczenieWyjscia import LiczenieWyjscia
from Charakterystyki import Charakterystyki


class RysowanieWykresow:
    def __init__(self, obliczenia,charakterystyki):
        self.x = []
        self.y = []
        self.obliczenia = obliczenia
        self.amp=charakterystyki.amp
        self.fi=charakterystyki.fi
        plt.figure(figsize=(14, 7))                                         #rozmiar okna w inch

    def rysowanieWejscia(self):
        self.x = self.obliczenia.t
        self.y = self.obliczenia.us
        plt.subplot(221)
        plt.plot(self.x, self.y)
        plt.xlabel("t")
        plt.ylabel("wejscie u(t)")
        plt.grid(True)

    def rysowanieWyjscia(self):
        plt.subplot(222)
        t = np.arange(0, self.obliczenia.h * self.obliczenia.ileElem, self.obliczenia.h)
        plt.plot(t, self.obliczenia.y)
        plt.xlabel("t")
        plt.ylabel("wyjscie y(t)")
        plt.grid(True)
    
    def rysowanieCharAmplitudowej(self):
        plt.subplot(223)
        w = np.linspace(0.01, 100, 100000)
        plt.plot(w, self.amp)
        plt.xlabel("czestotliwosc [Hz] (skala logarytmiczna)")
        plt.ylabel("amplituda")
        plt.xscale('log')
        plt.grid(True)
        
    def rysowanieCharCzestotliwosciowej(self):
        plt.subplot(224)
        w = np.linspace(0.01, 100, 100000)
        plt.plot(w, self.fi)
        plt.xlabel("czestotliwosc [Hz] (skala logarytmiczna)")
        plt.ylabel("faza")
        plt.xscale('log')
        plt.grid(True)
        plt.show()

