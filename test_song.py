import unittest
from song import Song

class TestSong(unittest.TestCase):
    def test_mark_learned(self):
        song = Song("Test Song", "Test Artist", 2022)
        song.mark_learned()
        self.assertTrue(song.learned)

    def test_mark_unlearned(self):
        song = Song("Test Song", "Test Artist", 2022, learned=True)
        song.mark_unlearned()
        self.assertFalse(song.learned)

    def test_str_representation(self):
        song = Song("Test Song", "Test Artist", 2022)
        self.assertEqual(
            str(song),
            "Test Song by Test Artist (2022) (Unlearned)"
        )

if __name__ == '__main__':
    unittest.main()
