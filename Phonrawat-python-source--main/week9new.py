#3 type => syntax errors / runtime errors/ logic errors
#valueError Exception
try:
    age = int(input("กรอกอายุ :"))
    print(f'ปีหน้าอายุ{age +1}ปี')
except ValueError:
    print("กรุณากรอบอายุที่เป็นตัวเลขจำนวนเต็ม เช่น 20")    

#ZeroDivisionException
"""try:
    """   