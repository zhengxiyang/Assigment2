import csv
from song import Song

filename = 'songs.csv'

songs = []

def load_songs(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create Song objects from the CSV data
            title, artist, year, learned = row
            songs.append(Song(title, artist, int(year), learned == 'True'))

def list_songs():
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")

def add_song():
    title = input("Enter the title: ")
    artist = input("Enter the artist: ")
    year = int(input("Enter the year: "))
    learned = False  # New songs are initially marked as unlearned
    songs.append(Song(title, artist, year, learned))
    print(f"{title} by {artist} added to the song list.")

def complete_song():
    list_songs()
    try:
        choice = int(input("Enter the number of the song to mark as learned: "))
        if 1 <= choice <= len(songs):
            songs[choice - 1].mark_learned()
            print(f"{songs[choice - 1].title} by {songs[choice - 1].artist} marked as learned.")
        else:
            print("Invalid song number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_menu():
    print("Menu:")
    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

def handle_choice(choice):
    if choice == 'L':
        list_songs()
    elif choice == 'A':
        add_song()
    elif choice == 'C':
        complete_song()
    elif choice == 'Q':
        print("Thank you.")
    else:
        print("Invalid choice")

def main():
    print("Songs To Learn 2.0 - by Yang Zhengxi")  # Update the version number
    load_songs(filename)
    display_menu()
    choice = input(">>> ").upper()
    while choice != 'Q':
        handle_choice(choice)
        display_menu()
        choice = input(">>> ").upper()
    print("Goodbye!")

if __name__ == '__main__':
    main()
