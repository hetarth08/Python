#Session 4 - String Methods in Python

#Task 1
text="Flipkart-Sale2024"
text=text.lower()
text=text.replace("-"," ")
print(text)


#Task 2
product_name="OnePlus Nord-CE 3"
product_name=product_name.strip()
product_name=product_name.upper()
product_name=product_name.replace("-",":")
print(product_name)


#Task 3
def split_product_code(product_code):
    return product_code.split("-")

code="ZOMATO-FOOD-2024"
print(split_product_code(code))


#Task 4
spotify_offer="Spotify_Premium_Offer"
print(spotify_offer[8:15])


#Task 5
product="Myntra Shirt"
price=799.5

print(f"Deal: {product} is available for ₹{price:.2f}only!")