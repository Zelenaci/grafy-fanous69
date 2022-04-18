import matplotlib.pyplot as plt
from math import pi
import tkinter as tk
from os.path import basename, splitext
import numpy as np


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Absolutně Luxusní Grafíček"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        self.var_jmeno_cary = tk.StringVar()
        self.var_amplituda_signalu = tk.IntVar()
        self.var_fazovy_posun_signalu = tk.IntVar()
        self.var_frekvence_signalu = tk.IntVar()
        self.var_periody_signalu = tk.IntVar()

        self.var_jmeno_cary.set("Grafovač")
        self.var_amplituda_signalu.set(12)
        self.var_fazovy_posun_signalu.set(0)
        self.var_frekvence_signalu.set(10)
        self.var_periody_signalu.set(2)
        

        vcmd = (self.register(self.callback))
        
        self.lbl_pomoc = tk.Label(self, text = "Pečlivě vyplňte hodnoty podle, kterých chcete vykreslit graf\n a pokud chcete načíst ze souboru klikněte na Načíst ze souboru.\n", font=("Helvetica", 12))
        self.lbl_pomoc.grid(row = 0, column = 1)

        self.lbl_jmeno_grafu = tk.Label(self, text = "Název čáry grafu: ")
        self.lbl_jmeno_grafu.grid(row = 1, column = 1, sticky = "w")
        self.entry_jmeno_grafu = tk.Entry(self, width = 30, textvariable = self.var_jmeno_cary)
        self.entry_jmeno_grafu.grid(row = 1, column = 2)

        self.lbl_frekvence = tk.Label(self, text = "Frekvence signálu: ")
        self.lbl_frekvence.grid(row = 2, column = 1, sticky = "w")
        self.entry_frekvence = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_frekvence_signalu)
        self.entry_frekvence.grid(row = 2, column = 2)

        self.lbl_amplituda = tk.Label(self, text = "Amplituda signálu: ")
        self.lbl_amplituda.grid(row = 3, column = 1, sticky = "w")
        self.entry_amplituda = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_amplituda_signalu)
        self.entry_amplituda.grid(row = 3, column = 2)

        self.lbl_periody = tk.Label(self, text = "Počet zobrazených period: ")
        self.lbl_periody.grid(row = 4, column = 1, sticky = "w")
        self.entry_periody = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_periody_signalu)
        self.entry_periody.grid(row = 4, column = 2)

        self.lbl_faz_posun = tk.Label(self, text = "Fázový posun signálu: ")
        self.lbl_faz_posun.grid(row = 5, column = 1, sticky = "w")
        self.entry_faz_posun = tk.Entry(self, width = 30, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_fazovy_posun_signalu)
        self.entry_faz_posun.grid(row = 5, column = 2)

        self.btn_vykresli = tk.Button(self, text = "Generovat graf", command = self.generuj_graf, width = 19, border = 3, background = "#5e5a9e")
        self.btn_vykresli.grid(row = 6, column = 2)
        
        self.btn_vykresli_example = tk.Button(self, text = "Načíst ze souboru", command = self.nacist, width = 19, border = 3, background = "#78769c")
        self.btn_vykresli_example.grid(row = 7, column = 2)
        
        self.btn_quit = tk.Button(self, text="Konec", command=self.quit, width = 10, border = 3, background = "#8f8e99")
        self.btn_quit.grid(row =7, column = 1)


    def generuj_graf(self):
        jmeno = self.var_jmeno_cary.get()
        amplituda = self.var_amplituda_signalu.get()
        faz_posun = self.var_fazovy_posun_signalu.get()
        frekvence = self.var_frekvence_signalu.get()
        periody = self.var_periody_signalu.get()
        x = np.linspace(0, periody*1/frekvence, frekvence*10000)
        y = amplituda * (np.sin(2*pi*frekvence*x + np.deg2rad(faz_posun)))
        plt.plot(x, y, label = jmeno)
        plt.xlabel
        plt.grid(True)
        plt.legend(loc=3)
        plt.show()

    def nacist(self):
        name = "soubor-win.txt"
        with open(name, "r") as f:
            radky = []
            x = []
            y = []
            i = 0
            while True:
                radek = f.readline()
                radky.append(radek.split())
                if radek == "":
                    break
                x.append(float(radky[i - 1][0]))
                y.append(float(radky[i - 1][1]))
                i = i + 1

        plt.plot(x, y, label = name)
        plt.xlabel
        plt.grid()
        plt.legend()
        plt.show()


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    
    

    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()
