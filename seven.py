# Cart table (empty at start) 
cart = pd.DataFrame(columns=["p_id", "p_name", "quantity", "price"]) 
# Product table (simple list) 
products = { 
1: ("Notebook", 45), 
2: ("Pen", 10), 
3: ("Pencil", 5) 
} 
while True: 
    print("\n1. Add item") 
    print("2. View cart") 
    print("3. Delete item") 
    print("4. Exit") 
ch = input("Enter choice: ") 
if ch == "1": 
    print("\nProducts:") 
    for pid in products: 
        print(pid, products[pid][0], "- Rs.", products[pid][1]) 
pid = int(input("Enter product id: ")) 
qty = int(input("Enter quantity: ")) 
p_name = products[pid][0] 
price = products[pid][1] 
# Add row to DataFrame 
cart.loc[len(cart)] = [pid, p_name, qty, price] 
print("Item Added.")
elif ch == "2": 
    if cart.empty: 
print("Cart is empty.") 
else: 
print("\nCart Items:") 
print(cart) 
elif ch == "3": 
pid = int(input("Enter product id to delete: ")) 
cart = cart[cart["p_id"] != pid] 
print("Item Deleted.") 
elif ch == "4": 
print("Thank you!") 
break 
else: 
print("Invalid choice.")