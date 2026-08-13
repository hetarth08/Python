#Session 6 - Dictionary and Sets in Python

#Task 1
insta_followers={
    "virat_kohli":270000000,
    "cristiano":650000000,
    "selenagomez":420000000,
    "therock":395000000,
    "zendaya":185000000
}

print("Instagram Followers:")
print(insta_followers)


#Task 2
insta_followers["arihitsingh"]=15000000
insta_followers["virat_kohli"]=2750000000
del insta_followers["zendaya"]

print("Updated Dictionary:")
print(insta_followers)


#Task 3
food_prices={
    "Pizza":250,
    "Burger":180,
    "Biryani":220,
    "Pasta":280,
    "Sandwich":150
}

print("Food items costing more than Rs.200:")

for item, price in food_prices.items():
    if price>200:
        print(item, ":", price)


#Task 4
flipkart_users={"hetarth","mohit","jaimin","dev","niahl"}
myntra_users={"kiyan","jaivish","shivam","parth","shukan"}

common_users=flipkart_users.intersection(myntra_users)

print("Users on both platform:")
print(common_users)


#Task 5
def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1={"Arijit Singh","Atif Aslam","Shreya Goshal"}
playlist2={"Arijit Singh","Taylor Swift","The Weeknd"}

unique_artists=get_unique_artists(playlist1,playlist2)

print("Unique Artists:")
print(unique_artists)