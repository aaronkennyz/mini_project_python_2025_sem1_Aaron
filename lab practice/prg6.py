# error handling


try:

    a = int(input(" enter numerator "))
    b = int(input(" enter denominator "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print(" cant divide by zero ")
except ValueError:
    print(" input proper vslyes ")
