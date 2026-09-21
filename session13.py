#Task 1:Print Playlist Songs Using Recursion
def print_playlist_songs(songs):
    if len(songs)==0:
        return
    print(songs[0])
    print_playlist_songs(songs[1:])
songs=['Shape Of You','Blinding Lights','Levitating','Senorita']
print_playlist_songs(songs)

#Task 2:Count unread messages using recursion
def count_unread_messages(messages):
    total=messages.get("count",0)

    for group in messages.get("subgroups",[]):
        total=total+count_unread_messages(group)
    return total

messages={
    "count":5,
    "subgroups":[
        {
            "count":3,
            "subgroups":[
                {"count":2},
                {"count":4}
            ]
        },
        {
            "count":6
        }
    ]
}
print("Total unread messages:",count_unread_messages(messages))

#Task 3:Loacal and global variables
x='global'

def outer():
    x='outer'

    def inner():
        nonlocal x
        x='inner'
    inner()
    print('Inside outer:',x)
outer()
print('Outside:',x)

#Task 4:Number in short format using recursion
def format_number_short(n):
    if n<1000:
        return str(n)
    if n < 1000000:
        return str(round(n/1000,1))+'K'
    return str(round(n/1000000,1))+'M'

print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(500))