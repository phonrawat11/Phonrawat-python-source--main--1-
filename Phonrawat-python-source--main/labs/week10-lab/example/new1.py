print("calculate_electricty_cost")
progressiev_elactrivty_info = """ค่าไฟฟ้ากับปริมาณการใช้งาน
จำนวนหน่วยที่ใช้              อัตราต่อหน่วย
1-50 หน่วยแรก              2.50บาท
51-100 หน่วยแรก            3.00บาท
101-200 หน่วยแรก           3.50บาท
มากกว่า 200 ขึ้นไป           4.00บาท
"""
print(progressiev_elactrivty_info)
unit = input("unit") 
if 1 <= unit <= 50:
        cost = (unit * 2.5)+25
        print("unit",unit)
        print("cost",cost)
elif 51 <= unit <= 100:
        cost = (unit * 3.00)+25 
        print("unit",unit)
        print("cost",cost)
elif 101 <= unit <= 200:
        cost = (unit * 3.50)+25 
        print("unit",unit)
        print("cost",cost)
elif  unit > 200:
        cost= (unit * 4.00)+25
        print("unit",unit)
        print("cost",cost)    
    
      