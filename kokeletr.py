import tkinter as tk
from windo import  windo as wind
from tkinter import ttk


class kekolet(wind):
    def __init__(self,wid,hit):
        super().__init__(wind,hit,"kokelotr")
        self.windo.geometry(str(wid) + "x" + str(hit))
        self.titel_label = ttk.Label(self.windo, text="calculator", font=('c 20 bold'))
        self.titel_label.pack()
        self.frame = ttk.Frame(self.windo)
        self.int1 = tk.IntVar()
        self.taker1 = ttk.Entry(self.frame, textvariable=self.int1, font=('c 20'))
        self.taker1.pack(side='left', padx=10)
        self.taker_string = tk.StringVar()
        self.taker2 = ttk.Entry(self.frame, textvariable=self.taker_string, font=('c 20'))
        self.taker2.pack(side='left')
        self.int3 = tk.IntVar()
        self.taker3 = ttk.Entry(self.frame, textvariable=self.int3, font=('c 20'))
        self.taker3.pack(side='left')
        self.btom = ttk.Button(self.frame, text="prass", command=self.prass)
        self.btom.pack(side='left')
        self.frame.pack(pady=10)
        self.otpot_string = tk.StringVar()
        self.icswol_label = ttk.Label(self.windo, text="defolt", font=('c 20 bold'), textvariable=self.otpot_string)
        self.icswol_label.pack()
    def prass(self):
        if self.taker_string.get() == "+":
            self.x = self.int1.get() + self.int3.get()
        elif self.taker_string.get() == "-":
            self.x = self.int1.get() - self.int3.get()
        elif self.taker_string.get() == "*" or self.taker_string.get() == "x" or self.taker_string.get() == "X":
            self.x = self.int1.get() * self.int3.get()
        elif self.taker_string.get() == "/"or self.taker_string.get() == ":":
            self.x = self.int1.get() / self.int3.get()
        else:
            self.x = '?????????????????????????'
        self.otpot_string.set(str(self.x))
        print(self.x)

