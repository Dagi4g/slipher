from rapidfuzz import fuzz
import emoji

class FilterVideo:
    def __init__(self,youtube_api,query):
        self.youtube_api = youtube_api
        self.query = query

    def build(self):
        video_rank = []
        for video in self.youtube_api.get("items"):
            video_rank.append({"video_id":video["id"]["videoId"],
            'title':video["snippet"]["title"],
            'score':self._title_match(video["snippet"]["title"])})

        video_rank.sort(key=lambda data: data['score'],reverse=True)
        
        print(video_rank)
        
        return video_rank

    def _title_match(self,title):
        """score the similarity of the title to the query from zero to 4 and return the float."""
        return fuzz.token_set_ratio(title,self.query)/20

    def ranked(self,video_rank:dict)->dict:
        ranked_videos = {}
        #for k,v in video_rank.items():


class FilterPlaylist():
    def __init__(self, youtube_api, query):
        self.youtube_api = youtube_api
        self.query = query

    def build(self):
        """Filter and rank playlists based on the search query."""
        playlists = []
        for playlist in self.youtube_api.get("items"):
            playlists.append({
                "playlist_id": playlist["id"]["playlistId"],
                "title": playlist["snippet"]["title"],
                "score": self._title_match(playlist["snippet"]["title"])
            })
        playlists.sort(key=lambda data: data['score'], reverse=True)
        return playlists

    def _title_match(self, title: str) -> float:
        """Score the similarity of the title to the query from zero to 4 and return the float."""
        return fuzz.token_set_ratio(title, self.query) / 20
