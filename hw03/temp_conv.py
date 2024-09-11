import tkinter as tk


def f2c():
    temp_f = int(ent_temp.get())
    temp_c = (temp_f - 32) * 5 / 9
    lbl_result["text"] = f"{temp_c:.2f} ℃"


window = tk.Tk()
window.title("GUI")
window.geometry("350x350")
window.resizable(width=False, height=False)

frm_ent_n = tk.Frame(master = window)
ent_temp = tk.Entry(master = frm_ent_n, width = 4)
lbl_n = tk.Label(window, text = "짝수의 합")

btn = tk.Button(
    master = window,
    text="->",
    width = 2, height = 1,
    command=f2c,
)

lbl_result = tk.Label(master=window)
lbl_n.grid(row=0, column =1, padx = 10, pady = 10)
frm_ent_n.grid(row = 1, column = 1, padx = 10, pady = 10)
ent_temp.grid(row = 1, column = 1, padx = 10, pady = 10)
btn.grid(row = 1, column = 2)
lbl_result.grid(row = 1, column = 3, padx = 10)


window.mainloop()

