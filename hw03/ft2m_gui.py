import tkinter as tk

def ft2m(ft: float) -> float:
    return ft * 0.3048


def convert_degree():
    try:
        ft = float(entry_f.get())
        m = ft2m(ft)
        label_result.config(text=f"{ft}ft -> {m:.3f}m")
    except ValueError:
        label_result.config(text="다시")

def main():
    global entry_f, label_result

    root = tk.Tk()
    root.title("ft2m")

    label_f = tk.Label(root, text="숫자를 입력하세요:")
    label_f.pack()

    entry_f = tk.Entry(root)
    entry_f.pack()

    button_convert = tk.Button(root, text="->", command=convert_degree)
    button_convert.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()


if __name__ == "__main__":
    main()

