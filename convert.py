from tkinter import *


def fahrenheit_to_celsius():
    """
    Конвертирует значение Фаренгейта в Цельсий
    :return:
    """
    fahr = ent_temp.get()
    celsius = (5 / 9) * (float(fahr) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


root_win = Tk()
root_win.title('Конвертер температуры')
root_win.resizable(False, False)

frm_entry = Frame(root_win)
ent_temp = Entry(frm_entry, width=10)
ent_temp.focus()
lbl_temp = Label(frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0, column=0, sticky='e')
lbl_temp.grid(row=0, column=1, sticky='w')

btn_convert = Button(
    root_win,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)

lbl_result = Label(root_win, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)


root_win.mainloop()
