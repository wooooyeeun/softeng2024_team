import tkinter as tk
from tkinter import messagebox


def facto(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)

def calculate():
    try:
        n = int(entry_n.get())
        label_result["text"] = f"{n}! => {facto(n)}"
    except ValueError:
        messagebox.showerror("오류", "정수를 입력해주세요!")

def main():
    global entry_n, label_result

    root = tk.Tk()
    root.title("calculate_factorial")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_n = tk.Label(root, text="숫자를 입력하세요.")
    label_n.grid(row=0, column=2, padx=100, pady=20)

    entry_n = tk.Entry(root)
    entry_n.grid(row=1, column=2)

    button_convert = tk.Button(root, text="↓", width=6, height=1, command=calculate)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()

if __name__ == "__main__":
    main()

    