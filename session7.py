#Task 1
spotify_time=int(input("Enter your Spotify listening time in minutes: "))

if spotify_time > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")

#Task 2
order_amount=int(input("Enter your Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

#Task 3
total=int(input("Enter your flipkart total: "))

if total > 2000:
    print("You get a 10% discount")
elif total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")

#Task 4
points=int(input("Enter your IPL fantasy team points: "))

if points > 800:
    print("Champion")
else:
    if points >=500:
        print("Top Performer")
    else:
        print("Keep Trying")