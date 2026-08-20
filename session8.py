#Task 1:FOOD DELIVERY APPS
food_apps=["Zomato","Swiggy","Uber Eats","Domino's","EatSure"]

for app in food_apps:
    print(app)


#Task 2:DAILY STEP COUNTS
steps=[7500,8200,9500,10500,8800,12000,9000]

day=0

while day < len(steps):
    if steps[day] > 10000:
        print("First day crossed 10,000 steps:",day+1)
        break
    day+=1


#Task 3:IPL TEAM NAMES
def long_teams(teams):
    for team in teams:
        if len(team) <=6:
            continue
        print(team)

teams=["Mumbai","Chennai","Kolkata","Rajasthan","Punjab"]

long_teams(teams)


#Task 4:SPOTIFY SONG DURATIONS
songs=[210,185,240,195,300]

for position,duration in enumerate(songs,start=1):
    print("Song",position,":",duration,"seconds")


#Task 5:FLIPKART SHOPPING CART
prices=[500,700,0,400,600,300]

total=0

for price in prices:
    if price==0:
        continue

    total=total+price

    if total > 2000:
        break

print("Final total:",total)