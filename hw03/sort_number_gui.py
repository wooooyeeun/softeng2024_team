import tkinter as tk

def is_even(n):
    return n % 2 == 0

def check_num():
    try:
        n = int(entry_number.get())
        if is_even(n):
            label_result.config(text=f"{n}은 짝수입니다.")
        else:
            label_result.config(text=f"{n}은 홀수입니다.")
    except ValueError:
        label_result.config(text="다시")

def main():
    global entry_number, label_result

    root = tk.Tk()
    root.title("prime_dist")

    label_prompt = tk.Label(root, text="숫자를 입력하세요.")
    label_prompt.pack()

    entry_number = tk.Entry(root)
    entry_number.pack()

    button_check = tk.Button(root, text="확인", command=check_num)
    button_check.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()


