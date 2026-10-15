print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 300 * 100

print("\n===== YOUR RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "out of 300")
print("Percentage:", round(percentage, 2), "%")

if maths >= 35 and physics >= 35 and chemistry >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
