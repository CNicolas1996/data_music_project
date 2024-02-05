from dataclasses import dataclass, field
from typing import List, Dict
from album.album import Album

@dataclass
class Artist:
    name: str
    genres: List[str]
    year: str
    albums: Dict[str, Album]
    members: List[str]
    country: str
    id: str = field(init=False)

    def __post_init__(self):
        self.id = f"{self.name}_{self.country}_{self.genres[0]}"

    def add_album(self, album: Album):
        if album.name in self.albums:
            print(f"El álbum '{album.name}' ya existe.")
            return
        self.albums[album.name] = album
