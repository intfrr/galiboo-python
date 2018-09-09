import requests

from music.constants import API_HOST
from ..utils import _send_request


def get_artist(artist_id, include_tracks=True):
    from auth import auth_token
    return _send_request( requests.get(API_HOST + "/metadata/artists/" + artist_id + "/", params={"token" : auth_token, 'include_tracks' : include_tracks}) )