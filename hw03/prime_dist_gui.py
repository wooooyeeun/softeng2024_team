import tkinter as tk
from tkinter import messagebox


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        n = int(entry_n.get())
        if is_prime(n):
            label_result["text"] = f"{n}은 소수입니다."
        else:
            label_result["text"] = f"{n}은 소수가 아닙니다."
    except ValueError:
        messagebox.showerror("오류", "정수를 입력해주세요!")

def main():
    global entry_n, label_result

    root = tk.Tk()
    root.title("prime_dist")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_p = tk.Label(root, text="숫자를 입력하세요.")
    label_p.grid(row=0, column=2, padx=100, pady=20)

    entry_n = tk.Entry(root)
    entry_n.grid(row=1, column=2)

    button_convert = tk.Button(root, text="확인", width=6, height=1, command=check_prime)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()

if __name__ == "__main__":
    main()


