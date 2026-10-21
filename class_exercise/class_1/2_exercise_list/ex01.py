
client = str(input("Enter your name: "))
quantity = int(input("How many products are you buying? "))
cost = float(input("Unity cost: "))
vip = str(input("Are you a VIP client? \n"
                 "[Y] yes \
                  [N] no \n"
                 ": "))

gross_total_value = quantity * cost

if vip == "Y" or vip == "y":
    discount = gross_total_value * 0.20

elif vip == "N" or vip == "n":

    if gross_total_value >= 500.00:
        discount = gross_total_value * 0.10
    elif gross_total_value >= 200.00 and gross_total_value <= 499.99:
        discount = gross_total_value * 0.05
    else:
        discount = 0

        total_discount = discount

net_total_value = gross_total_value - discount

print(f"Purchase Summary for Customer: {client} \n"
      f"Gross Total Value: € {gross_total_value} \n"
      f"Discount Applied: € {discount} \n"
      f"Final Amount Due: € {net_total_value}")