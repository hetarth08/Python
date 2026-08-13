#Session 5 - Lists and Tuples in Pyhton

#Task 1
playlist_ids=[101,102,103,104,105]
print("Playlist IDs:",playlist_ids)


#Task 2
playlist_ids.append(625)
playlist_ids.extend([730,835])

print("Updated Playlist:",playlist_ids)


#Task 3
removed_song=playlist_ids.pop()

print("Removed Song ID:",removed_song)
print("Remaining Playlist:",playlist_ids)


#Task 4
insta_filters=("Vintage","Retro","Glow","Black & White")
print("Instagram Filters:",insta_filters)

#Tuples cannot changed after creation
try:
    insta_filters[0]="Classic"
except TypeError as error:
    print("Error:",error)


#Task 5
recent_zomato_orders=["Pizza","Burger","Pasta"]
ipl_team_names=("GT","MI","CSK","RCB")

#A list is used for Zomato orders because orders can be added or removed.
#A tuple is used for IPL team names because the team names are fixed

print("Zomato Orders:",recent_zomato_orders)
print("IPL team:",ipl_team_names)