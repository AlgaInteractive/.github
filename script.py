import tkinter as tk

window = tk.Tk()
window.title("Мой ToDo-лист")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


btn = tk.Button(window, text="Добавить задачу", command=add_task)
btn.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

window.mainloop()