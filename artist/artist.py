import json
import datetime

class Artist:

    def __init__(self, name:str, genres:list, year:datetime, albums:dict, members:[], country:str):
        self.id = f"{name}_{country}_{genres[0]}"
        self.name = name
        self.genres = genres
        self.year = year
        self.albums = albums
        self.members = members
        self.country = country

    def add_album(self, album_name:str, album_year:datetime, songs:dict, producer:str, cover_image:str, rank:float, spotify_plays:int):
        self.albums[album_name] = {
            'year': album_year,
            'songs': dict(songs),
            'producer': producer,
            'cover_image': cover_image,
            'rank': rank,
            'spotify_plays' : spotify_plays
        }
