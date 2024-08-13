'''A customer wants to purchase a new car for that he visited three car showrooms for three different brands. MarutiCar, FordCar and HundaiCar. According to price range he is getting offer also in these brands. But customer having the budget only 7 lacs Rs. Which car you suggest after finding offers in:
Vehicle Price Range Offer
MarutiCar 4 lacs-6 lacs 12%
FordCar 6 lacs-7 lacs 13%
HundaiCar 7 lacs-8 lacs 14%'''

budget = 700000
maruti_price = 600000
maruti_offer = 0.12
maruti_final_price = maruti_price * (1 - maruti_offer)
ford_price = 700000
ford_offer = 0.13
ford_final_price = ford_price * (1 - ford_offer)
hundai_price = 700000
hundai_offer = 0.14
hundai_final_price = hundai_price * (1 - hundai_offer)
if maruti_final_price <= budget:
    suggested_car = "MarutiCar"
elif ford_final_price <= budget:
    suggested_car = "FordCar"
elif hundai_final_price <= budget:
    suggested_car = "HundaiCar"
else:
    suggested_car = "No suitable car within budget"
print(f"Final price of maruti {maruti_price} is:", maruti_final_price)    
print(f"Final price of ford {ford_price} is:",ford_final_price)
print(f"Final price of hundai {hundai_price} is:",hundai_final_price)
print("Suggested car is: ",suggested_car)
