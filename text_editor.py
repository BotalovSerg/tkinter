import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """ Открывает файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root_win.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Сохраняет текущий файл как новый файл"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    root_win.title(f"Простой текстовый редактор - {filepath}")


root_win = tk.Tk()
root_win.title('Простой текстовый редактор')

root_win.rowconfigure(0, minsize=800, weight=1)
root_win.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(root_win)
fr_buttons = tk.Frame(root_win)
btn_open = tk.Button(fr_buttons, text='Открыть', command=open_file)
btn_save = tk.Button(fr_buttons, text='Сохранить как...', command=save_file)

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

root_win.mainloop()
