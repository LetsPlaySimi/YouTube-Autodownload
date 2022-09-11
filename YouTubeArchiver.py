# API client library
import googleapiclient.discovery
#pytube
import pytube
from pytube import YouTube
#time
import time
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "YOUR_KEY"
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
while(1==1):
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q="YOUR_CHANNEL_USERNAME",
        videoDefinition='high',
        maxResults=1,
        channelId="YOUR_CHANNEL_ID",
        order="date",
        fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
    )
    # Query execution
    response = request.execute()
    # Print the results
    fullVideoLink="youtu.be/"+response['items'][0]['id']['videoId']
    print("Video id:", response['items'][0]['id']['videoId'])
    print("Publish date:", response['items'][0]['snippet']['publishedAt'])
    print("Title:", response['items'][0]['snippet']['title'])
    print("Channel id:", response['items'][0]['snippet']['channelId'])
    print("Full Video Link:", fullVideoLink)
    if((open("YouTubeArchive/history.txt", 'r').read()) != response['items'][0]['id']['videoId']):
        youtube=pytube.YouTube(fullVideoLink)
        video=youtube.streams.first()
        video.download('YouTubeArchive/')
        f = open("YouTubeArchive/history.txt", 'w')
        f.write(response['items'][0]['id']['videoId'])
        f.close()
    time.sleep(600)
    request = ""
