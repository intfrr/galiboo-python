import requests

from music.constants import API_HOST
from ..utils import _send_request


def add_analysis_job(url):
    from auth import auth_token
    return _send_request( requests.get(API_HOST + "/integration/tracks/analyze/", params={"token" : auth_token, "url" : url}) )

def get_analysis_job(job_id):
    from auth import auth_token

    return _send_request(
        requests.get(API_HOST + "/integration/jobs/" + job_id + "/",
                      params={"token": auth_token, "job_id": job_id})
    )

def get_jobs(page=1, show_progress=False):
    from auth import auth_token

    return _send_request(
        requests.get(API_HOST + "/integration/jobs/",
                      params={"token": auth_token, "page" : page, "show_progress" : show_progress})
    )