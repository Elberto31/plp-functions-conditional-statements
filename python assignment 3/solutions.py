def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
         # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        finalprice= price- discount_amount
        return finalprice
    else:
        return price
    
    # Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price != original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")


     