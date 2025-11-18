for i in range(1, 3):
    hours = int(input(f" enter the hours of emp  {i} : "))

    if hours > 40:
        ov = (hours - 40) * 12
        print(f"emp {i} has rupees { ov}")
    else:
        print(" no pvt ")
