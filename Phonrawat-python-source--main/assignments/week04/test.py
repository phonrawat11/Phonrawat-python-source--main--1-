#รับชื่อจริง(หรือข้อความ)จากผู้ใช้
#นับจำนวนสระในข้อความว่ามีกี่ตัว(a,e,i,o,u)
#ตัวอย่างหน้าจอ
# What is you name? :
#You text have 4 vowels.
# 
# print("\nLoop ผ่าน string:")

name = input("What is you name")
count = 0
for letter in name:
    print(f"ตัวอักษร: {letter}")
    if letter == 'a': 
       count = count + 1
    if letter == 'e': 
       count = count + 1
    if letter == 'i': 
        count = count + 1    
    if letter == 'o':
        count = count + 1 
    if letter == 'u':
        count = count + 1 
print("you have ",count,"vowels")             