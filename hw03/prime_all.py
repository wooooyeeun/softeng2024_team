import tkinter as tk

from hw02.prime import prime


def prime_all():
    n = int(ent_n.get())
    prime_list = []
    for i in range(1, n + 1):
        if prime(i):
            prime_list.append(i)
    lbl_result["text"] = f"{prime_list}"



window = tk.Tk()
window.title("GUI")
window.geometry("350x350")
window.resizable(width=False, height=False)

frm_ent_n = tk.Frame(master = window)
ent_n = tk.Entry(master = frm_ent_n, width = 4)
lbl_n = tk.Label(window, text = "소수구분")

btn = tk.Button(
    master = window,
    text="->",
    width = 2, height = 1,
    command=prime_all,
)

lbl_result = tk.Label(master=window)
lbl_n.grid(row=0, column =1, padx = 10, pady = 10)
frm_ent_n.grid(row = 1, column = 1, padx = 10, pady = 10)
ent_n.grid(row = 1, column = 1, padx = 10, pady = 10)
btn.grid(row = 1, column = 2)
lbl_result.grid(row = 1, column = 3, padx = 10)


window.mainloop()

