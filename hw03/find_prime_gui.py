import tkinter as tk

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
        if is_prime(iS):
            count += 1
    return count

def calculate_primes():
    try:
        n = int(entry_number.get())
        prime_count = count_prime(n)
        label_result.config(text=f"1부터 {n}까지의 소수는 {prime_count}개 입니다.")
    except ValueError:
        label_result.config(text="다시")

def main():
    global entry_number, label_result

    root = tk.Tk()
    root.title("소수 구하기")

    label_prompt = tk.Label(root, text="숫자를 입력하세요:")
    label_prompt.pack()

    entry_number = tk.Entry(root)
    entry_number.pack()

    button_calculate = tk.Button(root, text="->", command=calculate_primes)
    button_calculate.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

