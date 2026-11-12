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


class CD:
    def __init__(self, title: str, author: str, tracks=None):
        self.title = title
        self.author = author
        self.tracks = tracks if tracks is not None else []

    def aggiungi_brano(self, track: str) -> None:
        self.tracks.append(track)

    @property
    def durata_totale(self) -> int:
        totalDuration = 0
        for track in self.tracks:
            totalDuration += track.duration
        return totalDuration

    def filtra_brani_per_autore(self, author: str):
        newList = []
        for track in self.tracks:
            if author == track.author:
                newList.append(track)
        return newList

    def copia_brani(self):
        return [str(track) for track in self.tracks]

    def __str__(self):
        description = [str(track) for track in self.tracks]
        return f"CD: {self.title} by {self.author}\n- " + "\n- ".join(description)


if __name__ == "__main__":
    t1 = Track("Blinding Lights", "The Weeknd", 200)
    t2 = Track("Stay", "Kid LAROI & Justin Bieber", 141)
    t3 = Track("Save Your Tears", "The Weeknd", 215)
    
    print("--- Tracks ---")
    print(t1)
    print(f"Is '{t2.title}' a short song? {t2.short_song()}")
    
    print("\n--- CD Showcase ---")
    pop_cd = CD("Modern Pop Hits", "Various Artists", [t1, t2, t3])
    print(pop_cd)
    print(f"Total CD duration: {pop_cd.durata_totale} seconds")
    
    weeknd_tracks = pop_cd.filtra_brani_per_autore("The Weeknd")
    print(f"Tracks found by The Weeknd: {len(weeknd_tracks)}")

    print("\n--- Playlist Showcase ---")
    my_playlist = Playlist("My Rotation")
    my_playlist.aggiungi_brano(t1)
    my_playlist.aggiungi_brano(t3)
    print(my_playlist)
    print(f"Total playlist duration: {my_playlist.durata_totale()} seconds")