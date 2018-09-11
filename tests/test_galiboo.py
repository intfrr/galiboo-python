import datetime
import responses

from galiboo import Artist, Track, User, UserEvent, Job

from .conftest import full_path


class TestGaliboo:

    def test_galiboo_instance(self, galiboo):
        assert galiboo.url == "http://secure.galiboo.com/api"
        assert isinstance(galiboo.artist, Artist) is True
        assert isinstance(galiboo.track, Track) is True
        assert isinstance(galiboo.user, User) is True
        assert isinstance(galiboo.user_event, UserEvent) is True
        assert isinstance(galiboo.job, Job) is True

    @responses.activate
    def test_galiboo_artist(self, galiboo):
        responses.add(
            responses.GET,
            "%s/%s" % (galiboo.url, "metadata/artists/5a43dfbec3de0d102316497e"),
            body=open(full_path("./fixtures/artist_metadata.json")).read(),
            content_type="application/json"
        )
        resp = galiboo.artist.metadata("5a43dfbec3de0d102316497e")
        assert resp["_id"] == "5a43dfbec3de0d102316497e"
        assert resp["name"] == "Charlie Puth"

    @responses.activate
    def test_galiboo_track(self, galiboo):
        responses.add(
            responses.GET,
            "%s/%s" % (galiboo.url, "metadata/tracks/5a419ed78cc3d0d2d4249ebb"),
            body=open(full_path("./fixtures/track_metadata.json")).read(),
            content_type="application/json"
        )
        resp = galiboo.track.metadata("5a419ed78cc3d0d2d4249ebb")
        assert resp["_id"] == "5a419ed78cc3d0d2d4249ebb"
        assert resp["artists"][0]["name"] == "Charlie Puth"

    @responses.activate
    def test_galiboo_user(self, galiboo):
        responses.add(
            responses.POST,
            "%s/%s" % (galiboo.url, "personalization/users/new/"),
            body=open(full_path("./fixtures/create_user.json")).read(),
            content_type="application/json"
        )
        resp = galiboo.user.create("test")
        assert resp["galiboo_user_id"] == "5a78e59456296c4eda8e9bf0"

    @responses.activate
    def test_galiboo_user_event(self, galiboo):
        responses.add(
            responses.POST,
            "%s/%s" % (galiboo.url, "personalization/users/test/events/new"),
            body=open(full_path("./fixtures/create_user_event.json")).read(),
            content_type="application/json"
        )
        event = {
            'timestamp' : datetime.datetime.utcnow().isoformat(),
            'type' : 'listen',
            'object' : {
                'type' : 'track',
                'id' : "5a41cdf48cc3d0d2d42b3d8c"
            }
        }
        resp = galiboo.user_event.create(user_id="test", event=event)
        assert resp["event_id"] == "5a78e78256296c4eda8e9bf1"

    @responses.activate
    def test_galiboo_job(self, galiboo):
        responses.add(
            responses.GET,
            "%s/%s" % (galiboo.url, "integration/jobs"),
            body=open(full_path("./fixtures/all_jobs.json")).read(),
            content_type="application/json"
        )
        resp = galiboo.job.all()
        assert resp["jobs"][0]["analysis_url"] == "/jobs/5b8c17c9011610000bc2de67/"
