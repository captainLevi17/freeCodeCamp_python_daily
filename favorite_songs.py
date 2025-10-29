'''
Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).
'''
def favorite_songs(playlist):
    # Sort the playlist based on the "plays" property in descending order
    sorted_playlist = sorted(playlist, key=lambda song: song["plays"])
    # Extract the titles of the top two songs
    top_two_titles = [sorted_playlist[-1]["title"], sorted_playlist[-2]["title"]]
    # Return the titles of the two most played songs
    playlist = top_two_titles


    return playlist
print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
#Pseudocode
# Define a function favorite_songs that takes a playlist as input
# Sort the playlist based on the "plays" property in descending order
# Extract the titles of the top two songs from the sorted playlist
# Return an array containing the titles of the two most played songs    