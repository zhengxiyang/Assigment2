from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from song import Song, SongCollection

class SongApp(App):
    def build(self):
        self.song_collection = SongCollection()

        self.song_collection.load_songs('songs.json')

        root = BoxLayout(orientation='horizontal')

        left_layout = BoxLayout(orientation='vertical')
        right_layout = BoxLayout(orientation='vertical', spacing=10)

        sort_label = Label(text="Sort by:")
        sort_dropdown = DropDown()
        sort_options = ['Title', 'Artist', 'Year', 'Learned']
        for option in sort_options:
            btn = Button(text=option, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.sort_songs(btn.text.lower()))
            sort_dropdown.add_widget(btn)

        sort_button = Button(text='Sort')
        sort_button.bind(on_release=sort_dropdown.open)
        sort_dropdown.bind(on_select=lambda instance, x: setattr(sort_button, 'text', x))

        left_layout.add_widget(sort_label)
        left_layout.add_widget(sort_button)

        self.song_buttons = []

        for song in self.song_collection.songs:
            button = Button(text=str(song), size_hint_y=None, height=40)
            button.bind(on_release=lambda btn: self.toggle_learned(btn.text))
            self.song_buttons.append(button)
            right_layout.add_widget(button)

        status_label_top = Label(text=f"Learned: {self.song_collection.get_number_of_learned_songs()} "
                                      f"Unlearned: {self.song_collection.get_number_of_unlearned_songs()}")

        status_label_bottom = Label(text="Status messages will appear here.")

        right_layout.add_widget(status_label_top)
        right_layout.add_widget(status_label_bottom)

        root.add_widget(left_layout)
        root.add_widget(right_layout)

        return root

    def sort_songs(self, key):
        self.song_collection.sort(key)
        self.update_song_buttons()

    def update_song_buttons(self):
        for button, song in zip(self.song_buttons, self.song_collection.songs):
            button.text = str(song)

    def toggle_learned(self, song_text):
        for song in self.song_collection.songs:
            if str(song) == song_text:
                song.toggle_learned()
                self.update_status_labels()
                break

    def update_status_labels(self):
        learned_count = self.song_collection.get_number_of_learned_songs()
        unlearned_count = self.song_collection.get_number_of_unlearned_songs()

        self.root.children[1].children[-2].text = f"Learned: {learned_count} Unlearned: {unlearned_count}"
        self.root.children[1].children[-1].text = "Status messages will appear here."

    def on_stop(self):
        self.song_collection.save_songs('songs.json')

if __name__ == '__main__':
    SongApp().run()

