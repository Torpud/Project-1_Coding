def calculate_fare():
    try:
        distance = float(input("กรุณากรอกระยะทาง (กิโลเมตร): "))
        if distance < 0:
            return "ระยะทางต้องมากกว่า 0 กิโลเมตร"
        if distance <= 1:
            fare = 35
        elif distance <= 10:
            fare = 35 + (distance - 1) * 5
        elif distance <= 20:
            fare = 35 + (9 * 5) + (distance - 10) * 6.5
        else:
            fare = 35 + (9 * 5) + (10 * 6.5) + (distance - 20) * 7.5
        peak_hour_input = input("เป็นช่วงเวลาเร่งด่วนหรือไม่? (ใช่/ไม่): ").strip()

        if peak_hour_input == "ใช่":
            fare += 20
        elif peak_hour_input != "ไม่":
            return "กรุณากรอก 'ใช่' หรือ 'ไม่' เท่านั้น"
        return f"ค่าโดยสารที่ต้องชำระคือ: {fare:.2f} บาท"
    
    except ValueError:
        return "กรุณากรอกระยะทางเป็นตัวเลข"
    
print(calculate_fare())