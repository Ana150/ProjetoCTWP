value = int(input("Insert the value: "))
coupon = input("Do you have a coupon (y/n): ")
couponValue = int(20)

if value > 500:
    discount = value * 0.80
else:
    discount = value * 0.88

if coupon == "y":
   withCoupon = discount - couponValue
   print(f'You will pay: {int(withCoupon)}')
   
else:
   print(f'You will pay: {int(discount)}')