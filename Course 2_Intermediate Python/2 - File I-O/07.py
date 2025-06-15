like_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"
}

def write_liked_songs_to_file(songs, filename):
    with open(filename, 'w') as file:
        file.write("Liked Songs:\n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
    print(f"Successfully wrote liked songs to {filename}")

write_liked_songs_to_file(like_songs, "liked_songs.txt")
