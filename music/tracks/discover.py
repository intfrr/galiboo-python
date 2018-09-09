import requests

from music.constants import API_HOST
from ..utils import _send_request


def find_similar_tracks(track_id, count=15):
    from auth import auth_token
    return _send_request( requests.get(API_HOST + "/discover/tracks/" + track_id + "/similar/", params={"token" : auth_token, "count" : count}) )

def find_tracks_by_tags(tags_query, count=10, page=1):
    from auth import auth_token

    return _send_request(
        requests.post(API_HOST + "/discover/tracks/find/",
                      params={"token": auth_token, "limit": count, "page": page},
                      data = tags_query
        )
    )