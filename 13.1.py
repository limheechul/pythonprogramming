import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        f = float(entry_f.get())
        c = (f - 32) / 1.8
        entry_c.delete(0, tk.END)
        entry_c.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "화씨 온도를 숫자로 입력하세요.")

def celsius_to_fahrenheit():
    try:
        c = float(entry_c.get())
        f = (c * 1.8) + 32
        entry_f.delete(0, tk.END)
        entry_f.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "섭씨 온도를 숫자로 입력하세요.")

def reset_fields():
    entry_f.delete(0, tk.END)
    entry_c.delete(0, tk.END)

def exit_program():
    root.quit()

# 메인 윈도우 생성
root = tk.Tk()
root.title("섭씨-화씨 변환기")

# 화씨 라벨과 입력창
label_f = tk.Label(root, text="화씨 (°F):")
label_f.pack(pady=2)
entry_f = tk.Entry(root)
entry_f.pack(pady=2)

# 섭씨 라벨과 입력창
label_c = tk.Label(root, text="섭씨 (°C):")
label_c.pack(pady=2)
entry_c = tk.Entry(root)
entry_c.pack(pady=2)

# 변환 버튼들
btn_f_to_c = tk.Button(root, text="화씨→섭씨", width=20, command=fahrenheit_to_celsius)
btn_f_to_c.pack(pady=3)

btn_c_to_f = tk.Button(root, text="섭씨→화씨", width=20, command=celsius_to_fahrenheit)
btn_c_to_f.pack(pady=3)

# 초기화 및 종료 버튼들
btn_reset = tk.Button(root, text="초기화", width=20, command=reset_fields)
btn_reset.pack(pady=3)

btn_exit = tk.Button(root, text="종료", width=20, command=exit_program)
btn_exit.pack(pady=3)

# 메인 루프 실행
root.mainloop()
