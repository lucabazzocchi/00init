class Track:
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty")
        self._author = value

    @property
    def duration(self):
        return self._duration

    @author.setter
    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Duration must be positive")
        self._duration = value

    def short_song(self):
        return self.duration <= 180

    def __str__(self):
        return f"{self.title} - {self.author} ({self.duration} seconds)"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def aggiungi_brano(self, track):
        self.tracks.append(track)

    def durata_totale(self):
        return sum(track.duration for track in self.tracks)

    def __str__(self):
        return f"Playlist: {self.name} ({len(self.tracks)} tracks)"

