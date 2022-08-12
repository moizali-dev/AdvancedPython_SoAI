from dataclasses import dataclass
from typing import List

@dataclass
class MusicAlbum:
    tite: str
    artist: str
    year: int
    songs: List[str]

if __name__ == "__main__":
    music_album1 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["ABitW1", "ABitW2"])

    music_album2 = MusicAlbum("The Dark Side of the Moon", "Pink Floyd",1972,["Time","Us and Them"])

    music_album3 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["ABitW1", "ABitW2"])

print(music_album1)
print(music_album1 == music_album3)