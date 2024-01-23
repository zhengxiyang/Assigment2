import unittest
import json
from song import Song
from songcollection import SongCollection

class TestSongCollection(unittest.TestCase):
    def setUp(self):
        self.song_collection = SongCollection()

    def test_add_song(self):
        song = Song("Test Song", "Test Artist", 2022)
        self.song_collection.add_song(song)
        self.assertIn(song, self.song_collection.songs)

    def test_get_number_of_unlearned_songs(self):
        song1 = Song("Song 1", "Artist 1", 2021)
        song2 = Song("Song 2", "Artist 2", 2022, learned=True)
        self.song_collection.songs = [song1, song2]
        self.assertEqual(self.song_collection.get_number_of_unlearned_songs(), 1)

    def test_get_number_of_learned_songs(self):
        song1 = Song("Song 1", "Artist 1", 2021)
        song2 = Song("Song 2", "Artist 2", 2022, learned=True)
        self.song_collection.songs = [song1, song2]
        self.assertEqual(self.song_collection.get_number_of_learned_songs(), 1)

    def test_load_songs(self):
        file_path = 'test_songs.json'
        with open(file_path, 'w') as file:
            json.dump([{'title': 'Test Song', 'artist': 'Test Artist', 'year': 2022, 'learned': False}], file)

        self.song_collection.load_songs(file_path)
        self.assertEqual(len(self.song_collection.songs), 1)
        self.assertEqual(self.song_collection.songs[0].title, 'Test Song')
        self.assertEqual(self.song_collection.songs[0].artist, 'Test Artist')

    def test_save_songs(self):
        file_path = 'test_songs.json'
        song = Song("Test Song", "Test Artist", 2022)
        self.song_collection.songs = [song]

        self.song_collection.save_songs(file_path)
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.assertEqual(data[0]['title'], 'Test Song')
            self.assertEqual(data[0]['artist'], 'Test Artist')

    def test_sort(self):
        song1 = Song("Song B", "Artist 1", 2021)
        song2 = Song("Song A", "Artist 2", 2022)
        self.song_collection.songs = [song1, song2]

        self.song_collection.sort('title')
        self.assertEqual(self.song_collection.songs[0].title, 'Song A')
        self.assertEqual(self.song_collection.songs[1].title, 'Song B')

if __name__ == '__main__':
    unittest.main()
