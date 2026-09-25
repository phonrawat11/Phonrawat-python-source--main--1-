print("calculate_electricty_cost")
progressiev_elactrivty_info = """ค่าไฟฟ้ากับปริมาณการใช้งาน
จำนวนหน่วยที่ใช้              อัตราต่อหน่วย
1-50 หน่วยแรก              2.50บาท
51-100 หน่วยแรก            3.00บาท
101-200 หน่วยแรก           3.50บาท
มากกว่า 200 ขึ้นไป           4.00บาท
"""
print(progressiev_elactrivty_info)
def calculate_electricty_cost(units):     
    if 1 <= units <= 50:
        cost1 = (units * 2.5) + 25
        print("ใช้งาน",units)
        print("ค่าไฟ",cost1)
    elif 51 <= units <= 100:
        cost2 = (units * 3.00) + 25 + 125 
        print("ใช่งาน",units)
        print("ค่าไฟ",cost2)
    elif 101 <= units <= 200:
        cost3 = (units * 3.50)+ 25 + 275
        print("ใช้งาน",units)
        print("ค่าไฟ",cost3)
    elif  units > 200:
        cost4 = (units * 4.00)+ 25 + 350 +275
        print("ใช้งาน",units)
        print("ค่าไฟ",cost4)  
units = int(input("unit ")) 
calculate_electricty_cost(units) 
while True:  
    print("menu")
    print("1.calculate_electricty_cost")
    print("2.Exit")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        units = int(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))
        if units < 0:
            print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
        else:
            calculate_electricty_cost(units)
    elif choice == "2":
        print("ออกจากโปรแกรม...")
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")
     