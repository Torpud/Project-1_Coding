import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        # รับค่าระยะทางจากช่องอินพุต
        distance = float(entry_distance.get())

        # ตรวจสอบค่าระยะทาง
        if distance < 0:
            messagebox.showerror("ข้อผิดพลาด", "ระยะทางต้องเป็นค่ามากกว่า 0")
            return

        # คำนวณค่าโดยสารตาม Flowchart
        if distance <= 1:
            fare = 35
        elif distance <= 10:
            fare = 35 + (distance - 1) * 5
        elif distance <= 20:
            fare = 35 + (9 * 5) + (distance - 10) * 6.5
        else:
            fare = 35 + (9 * 5) + (10 * 6.5) + (distance - 20) * 7.5

        # ตรวจสอบว่ามีการเลือกช่วงเวลาเร่งด่วนหรือไม่
        if peak_hour_var.get():
            fare += 20

        # แสดงค่าโดยสาร
        result_label.config(text=f"ค่าโดยสารที่ต้องชำระคือ: {fare:.2f} บาท")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกระยะทางเป็นตัวเลข")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณค่าโดยสาร")

# ส่วนอินพุตระยะทาง
tk.Label(root, text="กรอกระยะทาง (กิโลเมตร):").grid(row=0, column=0, padx=10, pady=10)
entry_distance = tk.Entry(root)
entry_distance.grid(row=0, column=1, padx=10, pady=10)

# สร้างตัวเลือก "ช่วงเวลาเร่งด่วน"
peak_hour_var = tk.BooleanVar()
peak_hour_checkbox = tk.Checkbutton(root, text="เป็นช่วงเวลาเร่งด่วน", variable=peak_hour_var)
peak_hour_checkbox.grid(row=1, columnspan=2, padx=10, pady=10)

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณค่าโดยสาร", command=calculate_fare)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# แสดงผลค่าโดยสาร
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

# เริ่มต้นโปรแกรม Tkinter
root.mainloop()