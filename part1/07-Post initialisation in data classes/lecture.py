from dataclasses import dataclass, field, asdict
from typing import List

CURRENT_YEAR = 2022

@dataclass
class MusicAlbum:
    tite: str
    artist: str
    year: int
    songs: List[str]
    years_from_publication: int = field(init=False)

    def __post_init__(self) -> None:
        self.years_from_publication = CURRENT_YEAR - self.year

    def to_dict(self) -> dict:
        return asdict(self)

if __name__ == "__main__":
    music_album1 = MusicAlbum("The Wall", "Pink Floyd", 1979, ["ABitW1", "ABitW2"])

    print(music_album1.years_from_publication)
    print(music_album1.to_dict())