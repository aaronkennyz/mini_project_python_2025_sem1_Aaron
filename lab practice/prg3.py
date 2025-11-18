numbers = [
    1,
    1,
    2,
    3,
    4,
    4,
    5,
    6,
    7,
    7,
    8,
    9,
]

ct = {}

for num in numbers:
    if num in ct:
        ct[num] += 1
    else:
        ct[num] = 1

print(" the number occurences ")

for k, v in ct.items():
    print(f" {k}:{v}")
