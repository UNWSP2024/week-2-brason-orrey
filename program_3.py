# Sales tax rate
tax_rate = 0.07

item_1_name = input("What are you buying?")
item1 = float(input(f"Enter the price of {item_1_name}: "))
item_2_name = input("What are you buying?")
item2 = float(input(f"Enter the price of {item_2_name}: "))
item_3_name = input("What are you buying?")
item3 = float(input(f"Enter the price of {item_3_name}: "))
item_4_name = input("What are you buying?")
item4 = float(input(f"Enter the price of {item_4_name}: "))
item_5_name = input("What are you buying?")
item5 = float(input(f"Enter the price of {item_5_name}: "))

subtotal = item1 + item2 + item3 + item4 + item5

sales_tax = subtotal * tax_rate

total = subtotal + sales_tax

print("Subtotal: $", round(subtotal, 2))
print("Sales Tax: $", round(sales_tax, 2))
print("Total: $", round(total, 2))
