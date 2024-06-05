#Перевернуть двухзначное число

import tkinter as tk

def check_num():
    global num
    num = num_entry.get()
    num_entry.delete(0, tk.END)

    if len(num) != 2:
        result_label.config(text="Было введено не двузначное число")
    else:
        try:
            num = int(num)
            num = ((num % 10) * 10) + num // 10
            result_label.config(text=f"Результат: {num}")
        except ValueError:
            result_label.config(text="Ошибка: было получено не число")

root = tk.Tk()
root.title("Перестановка цифр")

num_label = tk.Label(root, text="Введите двухзначное число:")
num_label.pack()

num_entry = tk.Entry(root, width=10)
num_entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_num)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
