#Session 3 Python Practical
#This program demonstartes data types,
#type conversion,functions,input,and boolean values.

#Task 1:Variables and data types
age=18
height_cm=175.5
name="Hetarth" 
has_spotify_account=True

print("Age:",age)
print("Type:",type(age))

print("Height:",height_cm)
print("Type:",type(height_cm))

print("Name:",name)
print("Type:",type(name))

print("Spotify Account:",has_spotify_account)
print("Type:",type(has_spotify_account))

#Task 2:Calculate total cart amount
def total_cart_amount(prices):
    total=0.0

    for price in prices:
        total+=float(price)

    return total

cart=['199.99','49','350.75']
print("Total Cart Amount:",total_cart_amount(cart))

#Task 3:Check cricket score
cricket_score=input("Enter the cricket score:")
cricket_score=int(cricket_score)

if cricket_score>=50:
    print("Half-century")
else:
    print("Keep going!")

#Task 4:Convert string to boolean
is_premium="True"
is_premium=is_premium=='True'

print("Premium Account:",is_premium)
print("Type:",type(is_premium))