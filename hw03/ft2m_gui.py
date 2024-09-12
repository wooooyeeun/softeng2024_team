import tkinter as tk
from tkinter import messagebox


def ft2m(ft: float) -> float:
    return ft * 0.3048


def convert_degree():
    try:
        ft = float(entry_f.get())
        m = ft2m(ft)
        label_result["text"] = f"{ft}ft => {m:.3f}m"
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력해주세요!")

def main():
    global entry_f, label_result

    root = tk.Tk()
    root.title("ft2m")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_f = tk.Label(root, text="숫자를 입력하세요:")
    label_f.grid(row=0, column=2, padx=100, pady=20)

    entry_f = tk.Entry(root)
    entry_f.grid(row=1, column=2)

    button_convert = tk.Button(root, text="↓", width=6, height=1, command=convert_degree)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()

