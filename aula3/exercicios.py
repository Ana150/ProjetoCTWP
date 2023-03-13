value = int(input("Insert the value: "))
coupon = input("Do you have a coupon (y/n): ")

if value > 500:
    discount = value * 0.88
else:
    discount = value * 0.94

if coupon == "y" or coupon == "Y":
   withCoupon = discount - 20
   print(f'You will pay: {int(withCoupon)}')

else:
   print(f'You will pay: {int(discount)}')