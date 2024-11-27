from Track import Track

class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def add_track(self, track):
        self.tracks.append(track)
        self.tracks.sort(key=Track.sort)

    def display_tracks(self):
        if not self.tracks:
            print('No tracks in the library.')
        else:
            for i, track in enumerate(self.tracks):
                print(f"[{i + 1}] {track}")
    
    def search_track(self, title):
        if not title:
            return []
        else:
            return [track for track in self.tracks if title.lower() in track.title.lower()]
        
    def validate_duration(self, duration):
        try:
            mins, seconds = map(int, duration.split(':'))
            return mins >= 0 and 0 <= seconds < 60
        except ValueError:
            return False
        
    def input_track(self):
        title = input('Enter a track title: ').strip()
        while not title:
            print('Track title cannot be empty.')
            title = input('Enter a track title: ').strip()
        
        artist = input('Enter artist name: ').strip()
        while not artist:
            print('Artist name cannot be empty.')
            artist = input('Enter artist name: ').strip()

        album = input('Enter album name: ').strip()
        while not album:
            print('Album name cannot be empty.')
            album = input('Enter album name: ').strip()

        duration = input('Enter track duration (MM:SS): ').strip()
        while not self.validate_duration(duration):
            print('Invalid duration format. Please enter in MM:SS format.')
            duration = input('Enter track duration (MM:SS): ').strip()

        additional_artist = input('Enter additional artists (separate with comma or leave blank): ').strip()
        additional_artist = [artist.strip() for artist in additional_artist.split(',')] if additional_artist else []

        new_track = Track(title, artist, album, duration, additional_artist)
        self.add_track(new_track)
        print(f'Track {title} by {artist} added successfully!')

lib = MusicLibrary()

while True:
    lib.input_track()
    another_track = input('Would you like to add another track? (Yes/No): ').strip().lower()
    if another_track == 'no':
        break
    elif another_track != 'yes':
        print("Invalid input. Please enter 'Yes' or 'No'.")


print('\nAll Tracks\n')
lib.display_tracks()

while True:
    search_title = input('Enter a title: ').strip()
    if not search_title:
        print('Search title cannot be empty.')
        continue

    result = lib.search_track(search_title)
    if result:
        for track in result:
            print(f'\nSearched Track: \n{track}')
    else:
        print('No track found.')