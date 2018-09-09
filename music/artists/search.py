import requests

from music.constants import API_HOST
from ..utils import _send_request


def search_artists(artist_name, limit=10, page=1):
    from auth import auth_token
    return _send_request(
        requests.get(API_HOST + "/metadata/artists/search/", params={"token" : auth_token,
                                                                                       'artist' : artist_name,
                                                                                       'limit' : limit,
                                                                                       'page' : page})
    )