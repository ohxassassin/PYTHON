'''Generate electricity bill from the following conditions:
Condition 1. If meter reading is more then 100 charagble amount will be 6.95 Rs per unit.
Condition 2. If meter reading is less then 100 charagble amount will be 5.95 Rs per unit. 
write this code in pyhton'''
meter_reading = float(input("Enter the meter reading (in units): "))
if meter_reading > 100:
    charge_per_unit = 6.95
else:
    charge_per_unit = 5.95
total_bill = meter_reading * charge_per_unit
print(f"The total electricity bill for {meter_reading} units is: Rs {total_bill:.2f}")

