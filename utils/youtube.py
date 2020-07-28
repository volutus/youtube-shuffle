import requests
from utils import file_utils

# This is your YouTube API key. You'll need to get one from the Google developers console.
YOUTUBE_API_KEY_LOCATION = 'secrets/YOUTUBE_API_KEY'


def get_api_key():
    return file_utils.read_file(YOUTUBE_API_KEY_LOCATION)


def fetch_videos(playlist_id, **kwargs):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    params = {'part': 'id,snippet', 'key': get_api_key(), 'maxResults': 50, 'playlistId': playlist_id}
    if 'page_token' in kwargs:
        params['pageToken'] = kwargs['page_token']
    response = requests.get(url=url, params=params)

    # Makes multiple assumptions about the JSON
    # 1. It contains an array called 'items'
    # 2. An Item contains a Snippet.
    # 3. A Snippet contains a lot of info, including a 'title' and 'description' string
    # 4. A Snippet also contains a ResourceId object, which itself contains a 'kind' and 'videoId' string
    response_json = response.json()

    videos = list()
    if 'videos' in kwargs:
        videos = kwargs['videos']

    for item in response_json['items']:
        snippet = item['snippet']
        title = snippet['title']
        description = snippet['description']
        resource_id = snippet['resourceId']
        video_id = resource_id['videoId']
        videos.append({'title': title, 'description': description, 'id': video_id})

    if 'nextPageToken' in response_json:
        next_page_token = response_json['nextPageToken']
        return fetch_videos(playlist_id, page_token=next_page_token, videos=videos)

    return videos


# Builds a query string array YouTube style (id=1,2,3,4)
def build_query_string_array(name, array):
    query_string = name + '='
    first_param = True
    for value in array:
        if first_param:
            query_string += value
            first_param = False
        else:
            query_string += '%2C' + value
    return query_string


# Playlist URI
# GET https://www.googleapis.com/youtube/v3/playlistItems&key=[YOUR_API_KEY] HTTP/1.1

# Single Video URI
# GET https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics
# &id=Ks-_Mh1QhMc&key=[YOUR_API_KEY] HTTP/1.1

# Many Video URI
# GET https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics
# &id=Ks-_Mh1QhMc%2Cc0KYU2j0TM4%2CeIho2S0ZahI&key=[YOUR_API_KEY] HTTP/1.1
