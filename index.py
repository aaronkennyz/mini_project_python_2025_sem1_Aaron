# Expense tracker and visualizer

"""
the objective of this program is to give the user a menu where they can enter their
expenses as per the date and visualize the expenses using a pie chart
and a bar chart and a table powered by the pandas library

"""
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import pandas as pd


# modularising the programs using functions


def expense():
    try:

        date = input(
            "Enter date (DD-MM-YYYY): "
        )  # the date is entered and filtered in the next line
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


# displayin the expenses


def view():
    try:
        df = pd.read_csv("store.csv", names=["date", "Category", "Amount"])
        print("\n all recorded expenses : \n")
        print(df.to_string(index=False))
        print(f"\n total expenses =  {df['Amount'].sum()}")
    except FileNotFoundError:
        print(" no expenses recorded yet ")


# visualizing the expenses


def chart():
    try:
        df = pd.read_csv("store.csv", names=["date", "Category", "Amount"])
        category_sum = df.groupby("Category")["Amount"].sum()

        # bar chart
        plt.figure(figsize=(7, 5))
        category_sum.plot(kind="bar", color="lightgreen", edgecolor="black")
        plt.title("Expenses by Category")
        plt.ylabel("Amount (₹)")
        plt.xlabel("Category")
        plt.grid(True, axis="y")
        plt.tight_layout()
        plt.show()

        # pie chart

        plt.figure(figsize=(6, 6))
        category_sum.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("⚠️ No expense data found to visualize!")


def main():

    while True:
        print("\n====== 💸 PERSONAL EXPENSE TRACKER 💸 ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            expense()
        elif choice == "2":
            view()
        elif choice == "3":
            chart()
        elif choice == "4":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 5.")


main()
# the progrqm starts from the main function
