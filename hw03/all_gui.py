import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def select():
    def odd_even():
        try:
            n = int(ent_n.get())
            if n % 2 == 0:
                lbl_result["text"] = "짝수"
            else:
                lbl_result["text"] = "홀수"
        except ValueError:
            messagebox.showerror("오류", "정수를 입력해주세요!")

    def is_prime():
        try:
            n = int(ent_n.get())
            if n < 2:
                lbl_result["text"] = "소수가 아닙니다"
            elif prime(n):
                lbl_result["text"] = "소수입니다."
            else:
                lbl_result["text"] = "소수가 아닙니다."
        except ValueError:
            messagebox.showerror("오류", "정수를 입력해주세요!")

    def prime_all():
        try:
            n = int(ent_n.get())
            prime_list = []
            for i in range(1, n + 1):
                if prime(i):
                    prime_list.append(i)
            lbl_result["text"] = f"{prime_list}"
        except ValueError:
            messagebox.showerror("오류", "정수를 입력해주세요!")

    def factorial():
        try:
            n = int(ent_n.get())
            result = 1
            for i in range(1, n + 1):
                result = result * i
            lbl_result["text"] = f"{result}"
        except ValueError:
            messagebox.showerror("오류", "정수를 입력해주세요!")

    def sum_even():
        try:
            n = int(ent_n.get())
            total = 0
            for i in range(1, n + 1):
                if is_even(i):
                    total += i
            lbl_result["text"] = f"{total}"
        except ValueError:
            messagebox.showerror("오류", "정수를 입력해주세요!")

    def f2c():
        try:
            temp_f = float(ent_n.get())
            temp_c = (temp_f - 32) * 5 / 9
            lbl_result["text"] = f"{temp_c:.2f} ℃"
        except ValueError:
            messagebox.showerror("오류", "숫자를 입력해주세요!")


    lbl_n = None
    btn_a = None
    frm_ent_n = tk.Frame(master=root)
    ent_n = tk.Entry(master=frm_ent_n, width=8)

    frm_ent_n.grid(row = 3, column = 1, sticky = "e")
    ent_n.grid(row = 3, column = 1, sticky = "e")

    if combobox.get() == "홀짝구분":
        lbl_n = tk.Label(root, text = "<홀짝구분>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = odd_even,
        )

    elif combobox.get() == "소수판별":
        lbl_n = tk.Label(root, text = "<소수판별>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = is_prime,
        )

    elif combobox.get() == "소수찾기":
        lbl_n = tk.Label(root, text = "<소수찾기>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = prime_all,
        )

    elif combobox.get() == "팩토리얼":
        lbl_n = tk.Label(root, text = "<팩토리얼>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = factorial,
        )

    elif combobox.get() == "짝수의합":
        lbl_n = tk.Label(root, text = "<짝수의합>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = sum_even,
        )

    elif combobox.get() == "온도변환":
        lbl_n = tk.Label(root, text = "<온도변환>", font = ("gulim", 13, "bold"))
        btn_a = tk.Button(
            master = root,
            text = "→",
            width = 6, height = 1,
            command = f2c,
        )
        lbl_temp_f = tk.Label(root, text = "℉")
        lbl_temp_f.grid(row = 3, column = 1, sticky = "e")

    lbl_result = tk.Label(master = root, width = 20)
    lbl_result.grid(row = 3, column = 3, sticky="w")
    lbl_n.grid(row = 2, column = 2, pady = 10)
    btn_a.grid(row = 3, column = 2, pady = 20)


def main():
    global combobox, root
    root = tk.Tk()
    root.title("GUI")

    root.geometry("350x200")
    root.resizable(width=True, height=True)


    select_list = ["팩토리얼", "홀짝구분", "소수판별", "소수찾기", "짝수의합", "온도변환"]
    combobox = ttk.Combobox(root, values = select_list)
    combobox.set("원하는 기능 선택")
    combobox.grid(row = 1, column = 1, columnspan = 2, padx = 20, pady = 20, sticky = "w")
    btn = tk.Button(
            master=root,
            text = "선택",
            width = 5, height = 1,
            command = select,
    )
    btn.grid(row = 1, column = 3, sticky="w")


    root.mainloop()


if __name__ == "__main__":
    main()

