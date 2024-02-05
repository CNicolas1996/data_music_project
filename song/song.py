
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Song:
    track: int
    title: str
    written_by: List[str]
    music_by: List[str]
    lead_vocals: List[str]
    length: str
    collaborators: Dict[str, str]
    lyrics: str