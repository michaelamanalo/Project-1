class Track:
    def __init__(self, title, artist, album, duration, add_artist):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.add_artist = [add_artist] if isinstance(add_artist, str) else add_artist or []

    def getDuration(self):
        mins, seconds = int(self.duration.split(':')[0]), int(self.duration.split(':')[1])
        return mins * 60 + seconds

    def getDurationstr(self):
        total_seconds = self.getDuration()
        mins = total_seconds // 60
        seconds = total_seconds % 60
        return f'{mins:02}:{seconds:02}'
    
    def sort(self):
        return self.title.lower(), self.artist.lower(), self.album.lower(), self.duration

    def __str__(self):
        add = "".join(self.add_artist)
        return f'Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nDuration: {self.duration}\nAdditional Artist: {add}\n'

class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def add_track(self, track):
        self.tracks.append(track)
        self.tracks = sorted(self.tracks, key=Track.sort)

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
            return [track for track in self.tracks if track.title.lower() == title.lower()]
        
    def input_track(self):
        title = input('Enter a track title: ')
        artist = input('Enter artist name: ')
        album = input('Enter album name: ')
        duration = input('Enter track duration (MM:SS): ')
        add_artist = input('Enter additional artists (separate with comma or leave blank): ')

        new_track = Track(title, artist, album, duration, add_artist)
        self.add_track(new_track)

lib = MusicLibrary()

while True:
    lib.input_track()
    another = input('Would you like to add another track? (Yes/No): ').strip().lower()
    if another == 'yes':
        continue
    else:
        if another == 'no':
            break



print('\nAll Tracks\n')
lib.display_tracks()

result = lib.search_track('Number One Girl')
if result:
    for track in result:
        print(f'Searched Track:\n{track}')
else:
    print('No track found.')

