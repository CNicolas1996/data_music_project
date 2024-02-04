class Song:

    def __init__(self, track:int, album_name, title:str, written_by:list,
                 music_by:list, lead_vocals:list, length:str,  collaborators:dict, lyrics):
        self.track = track
        self.title = title
        self.written = written_by
        self.music_by = music_by
        self.lead_vocals = lead_vocals
        self.length = length
        self.collaborators = collaborators
        self.lyrics = lyrics



