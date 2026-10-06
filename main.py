# Python Sales & Discount System

print("========== SALES SYSTEM ==========")

# Get product information
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

# Get customer type
customer_type = input("Enter customer type (vip / regular / new): ").lower()

# Calculate total price
total_price = product_price * quantity

# Calculate discount
if customer_type == "vip":
    discount_percent = 20
elif customer_type == "regular":
    discount_percent = 10
elif customer_type == "new":
    discount_percent = 5
else:
    discount_percent = 0

# Calculate discount amount
discount_amount = total_price * discount_percent / 100

# Calculate final price
final_price = total_price - discount_amount

# Display receipt
print("\n========== ORDER RECEIPT ==========")
print(f"Product: {product_name}")
print(f"Price: {product_price:,.0f}")
print(f"Quantity: {quantity}")
print(f"Customer type: {customer_type}")
print(f"Total price: {total_price:,.0f}")
print(f"Discount: {discount_percent}%")
print(f"Discount amount: {discount_amount:,.0f}")
print(f"Final price: {final_price:,.0f}")
print("===================================")