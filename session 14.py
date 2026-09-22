#Task 1:Create Playlist File
songs=['Gehra Hua',"Ashiq Tera","Tera Rasta Chodoon Na","Perfect","Winning Speech"]
file=open("playlist.txt","w")

for song in songs:
    file.write(song + "\n")

file.close()

print("Playlist created successfully")

#Task 2:Read Playlist File
file=open("playlist.txt","r")

for song in file:
    print(song.strip().upper())
file.close()

#Task 3:Read IPL Match CSV
import csv
file=open("Session14/ipl_matches.csv","r")
data=csv.DictReader(file)

for match in data:
    print("Match",match["match_id"],"Winner:",match["winner"])

file.close()

#Task 4:Read Movies JSON
import json
file=open("Session14/movies.json","r")
movies=json.load(file)

for movie in movies:
    print(movie["title"],"-",movie["rating"])

file.close()

#Task 5:Check and Create Favourite Apps JSON
from pathlib import Path

file_path=Path("my_fav_apps.json")

if file_path.exists():
    print("File already exists")
else:
    apps=[
        {"name":"Instagram","category":"Social Media"},
        {"name":"Zomato","category":"Food"},
        {"name":"Paytm","category":"Finance"}
    ]

    file=open(file_path,"w")
    json.dump(apps,file,indent=4)
    file.close()

    print("File created successfully")