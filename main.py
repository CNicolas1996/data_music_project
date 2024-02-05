from artist import artist as a
from album import album
from song import song
from src.utils.serialization import JSONSerializer


serializer = JSONSerializer

if __name__ == '__main__':

    artist1 = a.Artist(
        name="Pink Floyd",
        genres=["Prog-rock", "Psicodelich-rock", "Art-rock"],
        year=1965,
        albums={},
        members={'David Guilmour': 'Guitar', 'Roger Waters': 'Bass', 'Richard Wight': 'Keyboards', 'Nick Mason': 'Drums'},
        country='UK'
    )

    album1 = album.Album(
        name="Dark Side of the Moon",
        year="1973",
        songs={},
        producer="Alan Parsons",
        cover_image="URL de la imagen de la portada del álbum",
        rank=1,
        spotify_plays=1000
    )

    songs_to_add = [
        song.Song(
            track=1,
            title="Speak to Me",
            written_by=["Roger Waters"],
            music_by=["Roger Waters"],
            lead_vocals=["Clare Torry"],
            length="1:30",
            collaborators={},
            lyrics="This is a test"
        ),
        song.Song(
            track=2,
            title="Breathe",
            written_by=["Roger Waters", "David Gilmour"],
            music_by=["Roger Waters", "David Gilmour"],
            lead_vocals=["David Gilmour"],
            length="2:43",
            collaborators={},
            lyrics="This is another test"
        )
    ]

    # Agregar el álbum y las canciones al artista
    artist1.add_album(album1)
    album1.add_songs(songs=songs_to_add)

    print(serializer.to_json(artist1))





