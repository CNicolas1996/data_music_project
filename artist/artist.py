class Artist:

    def __init__(self, name:str, genres:list, year:str, albums:dict, members:[], country:str):
        self.id = f"{name}_{country}_{genres[0]}"
        self.name = name
        self.genres = genres
        self.year = year
        self.albums = albums
        self.members = members
        self.country = country

    def add_album(self, album_name:str, album_year:str, songs:dict, producer:str, cover_image:str, rank:float, spotify_plays:int):
        if album_name in self.albums:
            print(f"Álbum '{album_name}' Already  Exist")
            return

        self.albums[album_name] = {
            'year': album_year,
            'songs': dict(songs),
            'producer': producer,
            'cover_image': cover_image,
            'rank': rank,
            'spotify_plays' : spotify_plays
        }

    def add_song(self,):
        def add_song(self, track: int, album_name, title: str, writen_by: list, music_by: list, lead_vocals: list,
                     length: str, collaborators: dict, lyrics):

            if album_name not in self.albums:
                print(f"Álbum '{album_name}' not found. The song cannot be added.")
                return

            album = self.albums[album_name]

            if title in album['songs']:
                print(f"Song '{title}' already exist in el album '{album_name}'. Won't be added.")
                return

            song = {
                'track': track,
                'title': title,
                'writen_by': writen_by,
                'music_by': music_by,
                'lead_vocals': lead_vocals,
                'length': length,
                'collaborators': collaborators,
                'lyrics': lyrics
            }
            self.albums[album_name]['songs'][title] = song



