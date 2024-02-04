class Album():
        def __init__(self, name: str, year: int, songs: dict, producer: str, cover_image: str, rank: float,
                     spotify_plays: int):
            self.name = name
            self.year = year
            self.songs = songs
            self.producer = producer
            self.cover_image = cover_image
            self.rank = rank
            self.spotify_plays = spotify_plays

        def add_song(self, track:int, title:str, written_by:list, music_by:list,
                     lead_vocals:list, length:str, collaborators:dict, lyrics:str):
            song = {
                'track': track,
                'title': title,
                'written_by': written_by,
                'music_by': music_by,
                'lead_vocals': lead_vocals,
                'length':  length,
                'collaborators': collaborators,
                'lyrics': lyrics
            }

            self.songs[title] = song

