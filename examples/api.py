from galiboo import Galiboo

galiboo = Galiboo("<YOUR API KEY>")

print galiboo.track.smart_search("piano")
print galiboo.track.metadata("5a419ed78cc3d0d2d4249ebb") # Charlie Puth's "Attention"
print galiboo.track.get("Attention")
print galiboo.track.get(artist="Camila Cabello")
print galiboo.artist.metadata("5a43dfbec3de0d102316497e") # Charlie Puth
print galiboo.artist.get("Charlie Puth")
print galiboo.track.search_by_similar("5a419ed78cc3d0d2d4249ebb") # Tracks similar to Charlie Puth's "Attention"

# Sample query below
query = {
	"energy" : 0.2,
	"smart_tags" : {
		"Emotion-Calming_/_Soothing" : 0.9
	}
	# ... add any other tags/search criteria that you'd like!
}

print galiboo.track.search_by_tags(tags_query=query)

print galiboo.track.analyze("https://storage.googleapis.com/gb_spotify20k/spotify_preview_audios/4iLqG9SeJSnt0cSPICSjxv.mp3")
print galiboo.track.ai_analyze("https://storage.googleapis.com/gb_spotify20k/spotify_preview_audios/4iLqG9SeJSnt0cSPICSjxv.mp3")
print galiboo.track.ai_analyze("https://www.youtube.com/watch?v=nfs8NYg7yQM")