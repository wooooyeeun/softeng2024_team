from hw03.sort_number_gui import is_even
import tkinter as tk

def calculate_sum():
    even_100 = [i for i in range(1, 101) if is_even(i)]
    sum_even = sum(even_100)
    label_result.config(text=f"1부터 100까지 짝수의 합은 {sum_even}입니다.")


def main():
    global label_result

    root = tk.Tk()
    root.title("1-100 짝수 합")

    label_prompt = tk.Label(root, text="1-100 짝수 합 계산")
    label_prompt.pack()

    button = tk.Button(root, text="->", command=calculate_sum)
    button.pack()

    label_result = tk.Label(root, text="결과")
    label_result.pack()

    root.mainloop()

if __name__ == "__main__":
    main()