import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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
    video_id = []
    for video in search_result.get('items'):
        video_id.append({"video_id":video['id']['videoId'],"title":video["snippet"]["title"]})

    return video_id

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
        


