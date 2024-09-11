import tkinter as tk
import tkinter.ttk as ttk

from hw02.odd_even import is_even
from hw02.prime import prime


def select():
    def odd_even():
        n = int(ent_n.get())
        if n % 2 == 0:
            lbl_result["text"] = "짝수"
        else:
            lbl_result["text"] = "홀수"

    def is_prime():
        n = int(ent_n.get())
        if n < 2:
            lbl_result["text"] = "소수가 아닙니다"
        elif prime(n):
            lbl_result["text"] = "소수입니다."
        else:
            lbl_result["text"] = "소수가 아닙니다."

    def prime_all():
        n = int(ent_n.get())
        prime_list = []
        for i in range(1, n + 1):
            if prime(i):
                prime_list.append(i)
        lbl_result["text"] = f"{prime_list}"

    def factorial():
        n = int(ent_n.get())
        result = 1
        for i in range(1, n + 1):
            result = result * i
        lbl_result["text"] = f"{result}"

    def sum_even():
        n = int(ent_n.get())
        total = 0
        for i in range(1, n + 1):
            if is_even(i):
                total += i
        lbl_result["text"] = f"{total}"

    def f2c():
        temp_f = int(ent_n.get())
        temp_c = (temp_f - 32) * 5 / 9
        lbl_result["text"] = f"{temp_c:.2f} ℃"

    def remove_result():
        lbl_result["text"] = ""

    lbl_n = None
    btn_a = None


    frm_ent_n = tk.Frame(master=window)
    ent_n = tk.Entry(master=frm_ent_n, width=8)

    frm_ent_n.grid(row=3, column=1, padx=10, pady=10)
    ent_n.grid(row=3, column=1, padx=10, pady=10)


    if combobox.get() == "홀짝구분":
        lbl_n = tk.Label(window, text="<홀짝구분>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=odd_even,
        )
        btn_a.grid(row=3, column=2)

    elif combobox.get() == "소수판별":
        lbl_n = tk.Label(window, text="<소수판별>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=is_prime,
        )

    elif combobox.get() == "소수찾기":
        lbl_n = tk.Label(window, text="<소수찾기>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=prime_all,
        )

    elif combobox.get() == "팩토리얼":
        lbl_n = tk.Label(window, text="<팩토리얼>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=factorial,
        )

    elif combobox.get() == "짝수의합":
        lbl_n = tk.Label(window, text="<짝수의합>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=sum_even,
        )

    elif combobox.get() == "온도변환":
        lbl_n = tk.Label(window, text="<온도변환>", font=("gulim", 14))
        btn_a = tk.Button(
            master=window,
            text="→",
            width=6, height=1,
            command=f2c,
        )

    lbl_result = tk.Label(master=window, text="\t")
    lbl_result.grid(row=3, column=4, columnspan=2)
    lbl_n.grid(row=2, column=1, pady=10, sticky="w")
    btn_a.grid(row=3, column=2)


window = tk.Tk()
window.title("GUI")
window.geometry("350x200")
window.resizable(width=False, height=False)

lbl_select = tk.Label(window, text = "원하는 기능")
select_list = ["팩토리얼", "홀짝구분", "소수판별", "소수찾기", "짝수의합", "온도변환"]
combobox = ttk.Combobox(window, values = select_list)
combobox.set("선택")
combobox.grid(row = 1, column = 1, columnspan=3, padx = 10, pady = 10)
btn = tk.Button(
        master=window,
        text = "선택",
        width = 5, height = 1,
        command = select,
)
btn.grid(row = 1, column = 4, padx = 10)


window.mainloop()

