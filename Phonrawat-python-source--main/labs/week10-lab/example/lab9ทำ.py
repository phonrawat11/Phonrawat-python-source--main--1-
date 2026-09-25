try:
    score1 = float(input("กรอบเลขตัวแรก"))
    score2 = float(input("กรอบเลขตัวสองตัว"))
    operator = (input("เรื่องหมาย(+,-,*,/):"))

    re = 0
    if  operator == "+":
        re = score1 + score2
    elif  operator == "-":
        re = score1 - score2
    elif  operator == "*":
        re = score1 * score2
    elif  operator == "/":
        re = score1 / score2 

    print(f"{score1}{operator} {score2}={re}")  
except ValueError:
    print(f"ข้อมูลไม่ตรงกับที่ต้องการ")
except ZeroDivisionError:
    print(f'ไม่สามารถทำตัวเลข 0 ได้')   
except Exception:
    print("ทำอะไรไม่ได้บางอย่าง")         
finally:
    print("จบการทำงาน")                            