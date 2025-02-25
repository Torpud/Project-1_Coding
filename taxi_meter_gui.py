import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        distance = float(entry_distance.get())

        if distance < 0:
            messagebox.showerror("ข้อผิดพลาด", "ระยะทางต้องเป็นค่ามากกว่า 0")
            return
        if distance <= 1:
            fare = 35
        elif distance <= 10:
            fare = 35 + (distance - 1) * 5
        elif distance <= 20:
            fare = 35 + (9 * 5) + (distance - 10) * 6.5
        else:
            fare = 35 + (9 * 5) + (10 * 6.5) + (distance - 20) * 7.5

        if peak_hour_var.get():
            fare += 20

        result_label.config(text=f"ค่าโดยสารที่ต้องชำระ: {fare:.2f} บาท")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกระยะทางเป็นตัวเลข")

root = tk.Tk()
root.title("คำนวณค่าโดยสารสุดคิ้วท์")
root.geometry("400x300")
root.configure(bg="#FFD1DC") 

FONT_MAIN = ("Helvetica", 12, "bold")
FONT_RESULT = ("Helvetica", 14, "bold")

header_label = tk.Label(root, text="✿ คำนวณค่าโดยสาร ✿", font=("Helvetica", 16, "bold"), bg="#FFD1DC", fg="#D1477E")
header_label.pack(pady=10)

frame_input = tk.Frame(root, bg="#FFD1DC")
frame_input.pack(pady=5)
tk.Label(frame_input, text="กรอกระยะทาง (กม.):", font=FONT_MAIN, bg="#FFD1DC").pack(side="left", padx=5)
entry_distance = tk.Entry(frame_input, width=10, font=FONT_MAIN, bg="#FFEEF0", fg="#D1477E", relief="ridge")
entry_distance.pack(side="left")

peak_hour_var = tk.BooleanVar()
peak_hour_checkbox = tk.Checkbutton(root, text="เป็นช่วงเวลาเร่งด่วน", variable=peak_hour_var, font=FONT_MAIN, bg="#FFD1DC", fg="#D1477E", selectcolor="#FFEEF0")
peak_hour_checkbox.pack(pady=5)

calculate_button = tk.Button(root, text="คำนวณค่าโดยสาร", font=FONT_MAIN, bg="#FFB6C1", fg="white", relief="ridge", command=calculate_fare)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=FONT_RESULT, bg="#FFD1DC", fg="#D1477E")
result_label.pack(pady=10)

root.mainloop()
