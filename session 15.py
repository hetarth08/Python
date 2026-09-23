#Task 1:Spotify Song Duration
def get_song_duration_per_minute(total_duration,number_of_songs):
    try:
        result=total_duration/number_of_songs
        print("Duration per song:",result,"minutes")
    except ZeroDivisionError:
        print("Number of songs cannot be zero.")
    finally:
        print("Spotify calculation completed.")

get_song_duration_per_minute(120,10)

#Task 2:Flipkart Price Per Item
total_amount=float(input("Enter total cart amount: "))
item_count=int(input("Enter number of items: "))

try:
    price=total_amount/item_count
    print("Price per item:",price)
except ZeroDivisionError:
    print("Item count cannot be zero.")

#Task 3:Paytm Cashback Calculator
class NoOfferApplied(Exception):
    pass

total_spend=float(input("Enter total spend: "))
offers=int(input("Enter number of offers applied: "))

try:
    if offers==0:
        raise NoOfferApplied("No offers were applied.")
    cashback=total_spend/offers
    print("Average cashback per offer:",cashback)
except NoOfferApplied as e:
    print("Error:",e)

#Task 4:Average Rating Calculator
def calculate_average_rating(total_rating,num_reviews):
    try:
        return total_rating/num_reviews
    except ZeroDivisionError:
        print("Number of reviews cannot be zero.")
        return 0
    finally:
        print("Thank you for using the calculator.")

print(calculate_average_rating(500,0))

#Task 5:Zomato Bill Split
def safe_divide_for_zomato(bill_amount,number_of_people):
    try:
        result=bill_amount/number_of_people
    except ZeroDivisionError:
        print("Number of people cannot be zero.")
    else:
        print("Amount per person:",result)
    finally:
        print("Split calculation done")

safe_divide_for_zomato(1000,4)
