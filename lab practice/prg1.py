# program to display prime numbers withinh a given range

start = int(input(" enter the start value : "))
end = int(input(" enter the end value :  "))

print(f" the prime numbers in the range of {start} to {end } are : ")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end="")
