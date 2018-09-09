import requests

from music.constants import API_HOST
from ..utils import _send_request


def get_track(track_id):
    from auth import auth_token
    return _send_request( requests.get(API_HOST + "/metadata/tracks/" + track_id + "/", params={"token" : auth_token}) )