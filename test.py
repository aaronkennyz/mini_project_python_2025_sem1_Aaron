from datetime import datetime


def expense():
    try:
        date = input("Enter date (DD-MM-YYYY): ")
        datetime.strptime(date, "%d-%m-%Y")
        category = input(" define your expense category eg sports, food etc . : ")
        amount = float(input(" enter the amount spent : "))

        # writting the given data to a csv file

        with open("store.csv", "a", newline="") as f:
            write = csv.writer(f)
            write.writerow([date, category, amount])
            print(" items added succesfully ")
    except ValueError:
        print(" please  give valid inputs ")


expense()
