import tkinter as tk

from hw02.prime import prime


def is_prime():
    n = int(ent_n.get())
    if n < 2:
        lbl_result["text"] = "소수가 아닙니다"
    elif prime(n):
        lbl_result["text"] = "소수입니다."
    else:
        lbl_result["text"] = "소수가 아닙니다."


window = tk.Tk()
window.title("GUI")
window.geometry("350x350")
window.resizable(width=False, height=False)

frm_ent_n = tk.Frame(master = window)
ent_n = tk.Entry(master = frm_ent_n, width = 4)
lbl_n = tk.Label(window, text = "소수판별")

btn = tk.Button(
    master = window,
    text="->",
    width = 2, height = 1,
    command=is_prime,
)

lbl_result = tk.Label(master=window)
lbl_n.grid(row=0, column =1, padx = 10, pady = 10)
frm_ent_n.grid(row = 1, column = 1, padx = 10, pady = 10)
ent_n.grid(row = 1, column = 1, padx = 10, pady = 10)
btn.grid(row = 1, column = 2)
lbl_result.grid(row = 1, column = 3, padx = 10)


window.mainloop()

