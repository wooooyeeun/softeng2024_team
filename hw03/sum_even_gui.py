import tkinter as tk
from tkinter import messagebox


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def calculate_sum():
    try:
        n = int(entry_n.get())
        sum_even = 0
        for i in range(1, n + 1):
            if is_even(i):
                sum_even += i
        label_result["text"] = f"1부터 {n}까지 짝수의 합은 {sum_even}입니다."
    except ValueError:
        messagebox.showerror("오류", "정수를 입력해주세요!")


def main():
    global entry_n, label_result

    root = tk.Tk()
    root.title("sum_even")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_p = tk.Label(root, text="숫자를 입력하세요.")
    label_p.grid(row=0, column=2, padx=100, pady=20)

    entry_n = tk.Entry(root)
    entry_n.grid(row=1, column=2)

    button_convert = tk.Button(root, text="↓", width=6, height=1, command=calculate_sum)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()

