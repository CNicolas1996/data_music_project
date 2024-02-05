from dataclasses import dataclass
from typing import Dict, List
from song.song import Song


@dataclass
class Album:
    name: str
    year: str
    songs: Dict[str, Song]
    producer: str
    cover_image: str
    rank: float
    spotify_plays: int = 0

    def add_songs(self, songs: List[Song]):
        for song in songs:
            title = song.title
            if title in self.songs:
                print(f"Canción '{title}' ya existe en el álbum '{self.name}'. No será agregada.")
            else:
                self.songs[title] = song
