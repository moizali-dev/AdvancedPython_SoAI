from typing import List
from __future__ import annotations

class MusicAlbum:
    def __init__(self, title: str, artist: str, year: int, songs: List[str]) -> None:
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = songs

    def __str__(self) -> str:
        return f"MusicAlbum(title='{self.title}', artists='{self.artist}'"

    def __eq__(self, other:MusicAlbum) -> bool:
        if self.title == other.title and self.artist == other.artist:
            return True
        return False

if __name__ == "__main__":
    music_album1 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["ABitW1", "ABitW2"])

    music_album2 = MusicAlbum("The Dark Side of the Moon", "Pink Floyd",1972,["Time","Us and Them"])

    music_album3 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["ABitW1", "ABitW2"])

print(music_album1 == music_album3)