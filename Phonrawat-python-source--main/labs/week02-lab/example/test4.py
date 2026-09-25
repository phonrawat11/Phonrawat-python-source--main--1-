print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()
#input
weight = float(input("input weight :"))
height = float(input("input height :"))
#process
MBI = weight / height ** 2
#output
print("BMI =",MBI)