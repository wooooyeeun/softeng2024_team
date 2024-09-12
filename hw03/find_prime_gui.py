import tkinter as tk
from tkinter import messagebox


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return False
    return True

def count_prime(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        if is_prime(i):
            count += 1
    return count

def find_primes():
    try:
        n = int(entry_n.get())
        prime_count = count_prime(n)
        prime_list = []
        for i in range(1, n + 1):
            if is_prime(i):
                prime_list.append(i)
        label_result["text"] = f"소수는 {prime_list}로 총 {prime_count}개입니다."
    except ValueError:
        messagebox.showerror("오류", "정수를 입력해주세요!")

def main():
    global entry_n, label_result

    root = tk.Tk()
    root.title("find_prime")

    root.geometry("300x200")
    root.resizable(width=True, height=True)

    label_p = tk.Label(root, text="숫자를 입력하세요.")
    label_p.grid(row=0, column=2, padx=100, pady=20)

    entry_n = tk.Entry(root)
    entry_n.grid(row=1, column=2)

    button_convert = tk.Button(root, text="찾기", width=6, height=1, command=find_primes)
    button_convert.grid(row=2, column=2, pady=20)

    label_result = tk.Label(root, text="결과")
    label_result.grid(row=3, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()

