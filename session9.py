#Task 1
def calculate_final_price(price,discount_rate):
    discount=price*discount_rate/100
    final_price=price-discount
    return final_price

price=500
discount_rate=10

print("Final Price:",calculate_final_price(price,discount_rate))

#Task 2
def get_delivery_charge(amount,city='Ahemedabad'):
    if city == 'Ahemedabad':
        return 0
    else:
        return 50

print("Delivery Charge:",get_delivery_charge(500))
print("Delivery Charge:",get_delivery_charge(500,'Mumbai'))

#Task 3
def format_price(price,currency='INR'):
    if currency == 'INR':
        return '₹'+str(price)
    elif currency == 'USD':
        return '$' +str(price)

print(format_price(500))
print(format_price(500, 'USD'))

#Task 4
def apply_coupon(price,coupon_code=None):
    if coupon_code == 'Zomato10':
        return price - (price*10/100)
    else:
        return price

print("Price without coupon:",apply_coupon(500))
print("Price with coupon:",apply_coupon(500,'Zomato10'))