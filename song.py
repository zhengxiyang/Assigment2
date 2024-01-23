class Song:
    def __init__(self, title, artist, year, learned=False):
        """
        Constructor for Song class.

        Parameters:
        - title (str): The title of the song.
        - artist (str): The artist of the song.
        - year (int): The year the song was released.
        - learned (bool): True if the song is learned, False otherwise.
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.learned = learned

    def mark_learned(self):
        """Mark the song as learned."""
        self.learned = True

    def mark_unlearned(self):
        """Mark the song as unlearned."""
        self.learned = False

    def __str__(self):
        """
        String representation of the Song object.

        Returns:
        str: A formatted string with song details.
        """
        return f"{self.title} by {self.artist} ({self.year}) {'(Learned)' if self.learned else '(Unlearned)'}"
