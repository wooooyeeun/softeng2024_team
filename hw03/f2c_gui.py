import tkinter as tk
from tkinter import messagebox


def f2c(temp_f: float) -> float:
    return(temp_f - 32) * 5 / 9

def convert_temperature():
    try:
        temp_f = float(entry_f.get())
        temp_c = f2c(temp_f)
        label_result["text"] = f"{temp_f}℉ => {temp_c:.1f}℃"
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력해주세요!")

def main():
    global entry_f, label_result

    root = tk.Tk()
    root.title("f2c")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_f = tk.Label(root, text="숫자를 입력하세요.")
    label_f.grid(row=0, column=2, padx=100, pady=20)

    entry_f = tk.Entry(root)
    entry_f.grid(row=1, column=2)

    button_convert = tk.Button(root, text="↓", width = 6, height = 1, command=convert_temperature)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()

