import json

class SongCollection:
    def __init__(self):
        """Constructor for SongCollection class."""
        self.songs = []

    def add_song(self, song):
        """
        Add a single Song object to the song list.

        Parameters:
        - song (Song): The Song object to add.
        """
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Get the number of unlearned songs."""
        return sum(1 for song in self.songs if not song.learned)

    def get_number_of_learned_songs(self):
        """Get the number of learned songs."""
        return sum(1 for song in self.songs if song.learned)

    def load_songs(self, file_path):
        """
        Load songs from a JSON file into the list of Song objects.

        Parameters:
        - file_path (str): The path to the JSON file.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.songs = [Song(**song_data) for song_data in data]

    def save_songs(self, file_path):
        """
        Save songs from the song list into a JSON file.

        Parameters:
        - file_path (str): The path to the JSON file.
        """
        data = [{'title': song.title, 'artist': song.artist, 'year': song.year, 'learned': song.learned}
                for song in self.songs]
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def sort(self, key):
        """
        Sort the songs by the key passed in, then by title.

        Parameters:
        - key (str): The attribute to sort the songs by.
        """
        self.songs.sort(key=lambda song: (getattr(song, key), song.title))
