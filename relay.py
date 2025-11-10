"""
=========================================
💼 MINI PROJECT: PERSONAL EXPENSE TRACKER
=========================================

🎯 Objective:
To build a Python program that records daily expenses, stores them in a CSV file,
analyzes total spending by category using Pandas, and visualizes the data using Matplotlib.

📚 Concepts Used:
- Variables, loops, functions (Unit 1)
- Lists, dictionaries, file handling (Unit 2)
- Exception handling, CSV, Pandas (Unit 3)
- Matplotlib for visualization (Unit 4)
"""

# ===============================
# Import Required Libraries
# ===============================
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# ===============================
# Function 1: Add Expense
# ===============================
def add_expense():
    """Takes user input for date, category, and amount, then appends to a CSV file."""
    try:
        date = input("Enter date (DD-MM-YYYY): ")
        datetime.strptime(date, "%d-%m-%Y")  # Validate date format

        category = input("Enter category (Food, Travel, Bills, etc.): ").capitalize()
        amount = float(input("Enter amount spent: "))

        # Append new expense record to CSV file
        with open("expenses.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount])

        print("✅ Expense recorded successfully!")

    except ValueError:
        print("❌ Invalid input! Please check your date or amount.")


# ===============================
# Function 2: View All Expenses
# ===============================
def view_expenses():
    """Displays all recorded expenses and total amount spent."""
    try:
        df = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
        print("\n📘 All Recorded Expenses:\n")
        print(df.to_string(index=False))
        print(f"\n💰 Total Spent: ₹{df['Amount'].sum()}")

    except FileNotFoundError:
        print("⚠️ No expense records found yet. Add some expenses first!")


# ===============================
# Function 3: Analyze Expenses
# ===============================
def analyze_expenses():
    """Groups expenses by category and displays total spent in each."""
    try:
        df = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
        summary = df.groupby("Category")["Amount"].sum().reset_index()
        print("\n📊 Expense Summary by Category:\n")
        print(summary.to_string(index=False))

    except FileNotFoundError:
        print("⚠️ No expense records found to analyze!")


# ===============================
# Function 4: Visualize Expenses
# ===============================
def visualize_expenses():
    """Creates bar and pie charts for visual analysis of expenses."""
    try:
        df = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
        category_sum = df.groupby("Category")["Amount"].sum()

        # ----- Bar Chart -----
        plt.figure(figsize=(7, 5))
        category_sum.plot(kind="bar", color="lightgreen", edgecolor="black")
        plt.title("Expenses by Category")
        plt.ylabel("Amount (₹)")
        plt.xlabel("Category")
        plt.grid(True, axis="y")
        plt.tight_layout()
        plt.show()

        # ----- Pie Chart -----
        plt.figure(figsize=(6, 6))
        category_sum.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("⚠️ No expense data found to visualize!")


# ===============================
# Function 5: Main Menu
# ===============================
def main():
    """Displays menu options and handles user navigation."""
    while True:
        print("\n====== 💸 PERSONAL EXPENSE TRACKER 💸 ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Analyze Expenses by Category")
        print("4. Visualize Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            visualize_expenses()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")


# ===============================
# Program Entry Point
# ===============================
if __name__ == "__main__":
    main()
