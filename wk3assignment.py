def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Get user input
try:
    price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount)
    print(f"Final price: {final_price}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
