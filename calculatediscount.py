def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input with percentage handling
original_price = float(input("Enter the original price of the item: "))
discount_input = input("Enter the discount percentage: ").strip('%')
discount_percent = float(discount_input)

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Improved print statement
if final_price < original_price:
    print(f"\nFinal discounted price: ${final_price:.2f}")
else:
    print(f"\nOriginal price remains: ${original_price:.2f}")
