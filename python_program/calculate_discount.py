# Calculate Discount: Calculate the final price after applying a discount to an item's price.

def calc_discounted_price(price, perc):
    disc_price = price * (1 - perc / 100)
    return disc_price

price = 1200
discount = 15
discounted_price = calc_discounted_price(price, discount)
print(f"Original Price: {price}, Discount: {discount}%")
print(f"Discounted Price: {discounted_price}")