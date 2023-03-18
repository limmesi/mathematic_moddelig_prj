from Konsola import Konsola
from LiczenieWyjscia import LiczenieWyjscia
from RysowanieWykresow import RysowanieWykresow
from Charakterystyki import Charakterystyki

konsola = Konsola()

konsola.pobieranieDanych()
konsola.wybierzSygnalPocz()
konsola.sprawdzanieStabilnosci()

# konsola.a.insert(0,2)
# konsola.a.insert(1,3)
# konsola.a.insert(2,3)
# konsola.b.insert(0,1)
# konsola.b.insert(1,0)
# konsola.b.insert(2,0)
# konsola.b.insert(3,0)
# konsola.sygnal = '1'
# konsola.Ampli = 2.0
# konsola.w = 10.0

obliczenia = LiczenieWyjscia(konsola)
charakterystyki = Charakterystyki(konsola)
rysowanie = RysowanieWykresow(obliczenia,charakterystyki)

if konsola.sygnal == '1':
    obliczenia.listaWarSin()

elif konsola.sygnal == '2':
    obliczenia.listaWarSkok()

elif konsola.sygnal == '3':
    obliczenia.listaWarFala()

else:
    print('ERROR: WRONG INPUT')

rysowanie.rysowanieWejscia()

obliczenia.rozwRowRoz()
rysowanie.rysowanieWyjscia()
charakterystyki.char_amp()
charakterystyki.char_cz()
rysowanie.rysowanieCharAmplitudowej()
rysowanie.rysowanieCharCzestotliwosciowej()