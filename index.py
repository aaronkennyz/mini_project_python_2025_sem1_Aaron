# Expense tracker and visualizer

"""
the objective of this program is to give the user a menu where they can enter their
expenses as per the date and visualize the expenses using a pie chart
and a bar chart

"""
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import pandas as pd


# modularising the programs using functions


def expense():
    try:
        date = input("enter the date in (dd/mm/yyyy) format : ")
        datetime.strptime(date, "%d-%m-%y")

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
        print(f"\n total expenses =  {df['amount'.sum]}")
    except FileNotFoundError:
        print(" no expenses recorded yet ")

# visualizing the expenses 

def chart():
    try:
        df=pd.read_csv("store.csv",names=["date", "Category", "Amount"])
        category_sum=df.groupby("Category")["Amount"].sum()
