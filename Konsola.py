class Konsola:
    def __init__(self):
        self.a = []
        self.b = []
        self.sygnal = 0
        self.w = 1     # pulsacja sygnalu
        self.Ampli=1   # amplituda syganalu

    def pobieranieDanych(self):
        print("Podaj dane: \n")
        # i od 0 do 2
        for i in range(0, 3):
            bufor = input("a" + str(i) + " = ")
            self.a.insert(i, int(bufor))
            print('\n')

        for i in range(0, 4):
            bufor = input("b" + str(i) + " = ")
            self.b.insert(i, int(bufor))
            print("\n")


    def wybierzSygnalPocz(self):
        self.sygnal = input('Aby wyswietlic pobudzenie sinusioda wybierz 1\n'
                            'Aby wyswietlic pobudzenie skokiem wybierz 2\n'
                            'Aby wyswietlic pobudzenie fala prostokontna wybierz 3\n')

        self.Ampli=float(input('Wpisz tutaj amplitude sygnalu A \n'))
        

        if self.sygnal=='1'or self.sygnal=='3':
            self.w= float(input('Wpisz tutaj pulsacje sygnalu w \n'))


    def sprawdzanieStabilnosci(self):
        if self.a[0] > 0 and self.a[1] > 0 and self.a[2] > 0:
            if self.a[1] * self.a[2] > self.a[0]:
                print("Uklad jest stabilny \n")
        else:
            print("Uklad nie jest stabilny \n")
