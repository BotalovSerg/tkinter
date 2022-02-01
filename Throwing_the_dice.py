import tkinter as tk
from random import randint


def r_cub():
    lbl_1['text'] = f'{randint(1, 6)}'


root = tk.Tk()
root.columnconfigure(0, minsize=150)
root.rowconfigure(0,  minsize=30)
root.rowconfigure(1, minsize=30)

btn_1 = tk.Button(root, text='Бросить', command=r_cub)
lbl_1 = tk.Label(root, text='777')

btn_1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
lbl_1.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
