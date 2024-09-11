import tkinter as tk

def f2c(temp_f: float) -> float:
    return(temp_f - 32) * 5 / 9

def convert_temperature():
    try:
        temp_f = float(entry_f.get())
        temp_c = f2c(temp_f)
        label_result.config(text=f"{temp_f}F => {temp_c:.1f}C")
    except ValueError:
        label_result.config(text="다시")

def main():
    global entry_f, label_result

    root = tk.Tk()
    root.title("f2c")

    label_f = tk.Label(root, text="숫자를 입력하세요:")
    label_f.pack()

    entry_f = tk.Entry(root)
    entry_f.pack()

    button_convert = tk.Button(root, text="->", command=convert_temperature)
    button_convert.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()


if __name__ == "__main__":
    main()

