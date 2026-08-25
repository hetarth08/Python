#Task 1:Convert song title to lowercase
songs=['Shape Of You','Binding Lights','Levitating','Senorita']
lowercase_songs=list(map(lambda song:song.lower(),songs))
print(lowercase_songs)

#Task 2:Filter Restaurant Rating Above 4.0
ratings=[4.2,3.8,4.5,2.9,3.5]
high_ratings=list(filter(lambda rating:rating > 4.0,ratings))
print(high_ratings)

#Task 3:Calculate Total Shopping Cart Price
from functools import reduce
cart=[499,1299,299,799]
total=reduce(lambda x,y:x+y,cart)
print("Final Total:",total)

#Task 4:Format Follower Counts
def format_followers(number):
    if number >= 1000000:
        return str(round(number / 1000000,1)) + 'M'
    elif number >= 1000:
        return str(round(number / 1000,1)) + 'K'
    else:
        return str(number)

followers=[950,1500,25000,1200000]

formatted_followers=list(map(format_followers,followers))

print(formatted_followers)

#Task 5:Filter Out Odd IPL Scores
scores=[101,98,120,77,88]
even_scores=list(filter(lambda score: score%2 == 0,scores))
print(even_scores)