#A shopping mall giving discount offer if you will purchase mobile with powerbank you will get 25% discount otherwise for mobile only 5% discount. using all the cases
mobile_price = float(input("Enter the price of the mobile: "))
buy_powerbank = input("Are you buying a power bank with the mobile? (yes/no): ")
if buy_powerbank == 'yes':
    discount = 0.25 
else:
    discount = 0.05
discount_amount = mobile_price * discount
final_price = mobile_price - discount_amount
print(f"Original price: Rs {mobile_price:.2f}")
print(f"Discount: Rs {discount_amount:.2f} ({discount * 100}%)")
print(f"Final price to be paid: Rs {final_price:.2f}")


