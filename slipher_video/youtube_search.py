import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .video_filter import FilterVideo

DEVELOPER_KEY = 'AIzaSyBS85UF62S4K1dp59pdSHnIFPX_Yhov1P4'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(args):
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    search_result = youtube.search().list(q=args,
                                 part = 'snippet',
                                 videoCategoryId=27,
                                 type='video',
                                 videoDuration='medium',
                                maxResults=50).execute()
    test = FilterVideo(search_result,args)
    return test.build()

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    while True:
        query = str(input('search: '))
        if query.lower() == "q":
            break
        
        parser.add_argument('--q',help='search query',default=query)
        parser.add_argument('--max-results',help='max result',default=50)
        args = parser.parse_args()
        video_id = youtube_search(args)
        print(video_id)
        


