import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Temperature converter')
root.resizable(False, False)

celsius_value = tk.StringVar()
fahrenheit_value = tk.StringVar(value='Temperature in fahrenheit...')


def convert(*args):
    try:
        celsius = float(celsius_value.get())
        fahrenheit = celsius * 9 / 5 + 32
        fahrenheit_value.set(f'{fahrenheit:.3f}')
    except ValueError:
        pass


main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.grid()

celsius_label = ttk.Label(main_frame, text='Celsius: ')
celsius_entry = ttk.Entry(main_frame, width=10, textvariable=celsius_value)
fahrenheit_label = ttk.Label(main_frame, text='Fahrenheit: ')
f_display_label = ttk.Label(main_frame, textvariable=fahrenheit_value)
convert_button = ttk.Button(main_frame, text='Convert', command=convert)

celsius_label.grid(row=0, column=0, sticky='W', padx=5, pady=5)
celsius_entry.grid(row=0, column=1, sticky='WE', padx=5, pady=5)
celsius_entry.focus()
fahrenheit_label.grid(row=1, column=0, sticky='W', padx=5, pady=5)
f_display_label.grid(row=1, column=1, sticky='WE', padx=5, pady=5)
convert_button.grid(row=2, column=0, columnspan=2, sticky='WE', padx=5, pady=5)

root.bind('<Return>', convert)

root.mainloop()
