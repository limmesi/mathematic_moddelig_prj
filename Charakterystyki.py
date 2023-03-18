import math

import matplotlib.pyplot as plt
import numpy as np


class Charakterystyki:
    def __init__(self, konsola):
        self.amp = []
        self.fi = []
        self.a = konsola.a
        self.b = konsola.b

    def char_amp(self):
        self.w = np.linspace(0.01, 100, 100000)
        for i in range(len(self.w)):
            value = 20*np.log10(np.sqrt((self.b[0] - self.b[2] * self.w[i] ** 2)**2 + (self.b[1] * self.w[i] - self.b[3] * self.w[i] ** 3)**2) /\
                    np.sqrt((self.a[0] - self.a[2] * self.w[i] ** 2)**2 + (self.a[1] * self.w[i] - self.w[i] ** 3)**2))
            self.amp.append(value)
        
    def char_cz(self):
        self.w = np.linspace(0.01, 100, 100000)
        for i in range(len(self.w)):
            value = np.arctan2((self.b[1] * self.w[i] - self.b[3] * self.w[i] ** 3), (self.b[0] - self.b[2] * self.w[i] ** 2)) \
                    - np.arctan2((self.a[1]*self.w[i] - self.w[i]**3), (self.a[0] - self.a[2] * self.w[i] ** 2))
            if value < 0:
                value += 2*math.pi
            self.fi.append(value)
        