student_inf0 = {
    101: "ali",
    102: "sara",
    103: "john",
    104: "rok",
}


reg = int(input("enter register number "))

if reg in student_inf0:
    print(" record found ", student_inf0[reg])
else:
    print(" reord unavailable ")


print(" the sorted list is ")

for a, b in sorted(student_inf0.items()):
    print(f"{a}:{b}")
