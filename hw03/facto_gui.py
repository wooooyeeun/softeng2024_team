import tkinter as tk

def facto(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)

def calculate():
    try:
        n = int(entry_n.get())
        output = facto(n)
        label_result.config(text=f"{n}! => {facto(n)}")
    except ValueError:
        label_result.config(text="다시")

def main():
    global entry_n, label_result

    root = tk.Tk()
    root.title("calculate_factorial")

    label_n = tk.Label(root, text="숫자를 입력하세요.")
    label_n.pack()

    entry_n = tk.Entry(root)
    entry_n.pack()

    button_convert = tk.Button(root, text="->", command=calculate)
    button_convert.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()