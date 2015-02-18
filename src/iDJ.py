import pyechonest
from pyechonest import config
from pyechonest import song
from pyechonest import track
import numpy as np

tempo_similarity_weight = 1.0
key_similarity_weight = 1.0
energy_similarity_weight = 0.5
song_similarity_weight = 0.5
transition_location_weight = 0.5
total_similarity_weight = tempo_similarity_weight + key_similarity_weight + energy_similarity_weight + song_similarity_weight + transition_location_weight
matching_key_weight = 1.0
harmonic_key_weight = 0.8

id_catalog = '7digital-US'

config.ECHO_NEST_API_KEY='WMZH4YMYNUTS9C9VD'
config.ECHO_NEST_CONSUMER_KEY='73515d3804c26a43c54e8d1aea479c7e'
config.ECHO_NEST_SHARED_SECRET='ElTLIRUtSpq9NqcWfqkfSQ'

song1_artist = "Swedish House Mafia"
song1_title = "Don't You Worry Child"
song2_artist = "Avicii"
song2_title = "Wake Me Up"

song1_results = song.search(artist=song1_artist, title=song1_title, buckets=['id:' + id_catalog, 'tracks', 'audio_summary'], limit=True)
song2_results = song.search(artist=song2_artist, title=song2_title, buckets=['id:' + id_catalog, 'tracks', 'audio_summary'], limit=True)
song1 = song1_results[0]
song2 = song2_results[0]
song1_track_dicts = song1.get_tracks(id_catalog)
song2_track_dicts = song2.get_tracks(id_catalog)
track1_dict = song1_track_dicts[0]
track2_dict = song2_track_dicts[0]
track1 = track.track_from_id(track1_dict['id'])
track2 = track.track_from_id(track2_dict['id'])
track1.get_analysis()
track2.get_analysis()

def calculateTempoSimilarity(section1, section2):
	tempo1 = section1['tempo']
	tempo2 = section2['tempo']
	similarity = 1.0 - 1.0*abs(tempo2 - tempo1)/tempo1
	return similarity

# TODO: Incorporate beatmatching info	
def calculateKeySimilarity(section1, section2):
	key1 = section1['key']
	mode1 = section1['mode']
	key2 = section2['key']
	mode2 = section2['mode']
	similarity = 0.0
	if key1 == key2:
		if mode1 == mode2:
			similarity = matching_key_weight
		else:
			# TODO: Should this be asymmetric?
			similarity = harmonic_key_weight 
	elif mode1 == mode2:
		# TODO: Should this be asymmetric?  Is going 1 direction on wheel preferred?
		key_diff = abs(key1 - key2)
		if key_diff == 1 or key_diff == 11:
			similarity = harmonic_key_weight	 
	return similarity
	
def calculateEnergySimilarity(section1, section2):
	similarity = 0.0
	return similarity
	
def calculateSongSimilarity(section1, section2):
	similarity = 0.0
	return similarity
	
def calculateTransitionLocationSimilarity(section1, section2):
	similarity = 0.0
	return similarity

def calculateSectionSimilarity(section1, section2):
	similarity = 0.0
	tempoSimilarity = calculateTempoSimilarity(section1, section2)
	keySimilarity = calculateKeySimilarity(section1, section2)
	energySimilarity = calculateEnergySimilarity(section1, section2)
	songSimilarity = calculateSongSimilarity(section1, section2)
	transitionLocationSimilarity = calculateTransitionLocationSimilarity(section1, section2)
	
	similarity += tempo_similarity_weight * tempoSimilarity
	similarity += key_similarity_weight * keySimilarity
	similarity += energy_similarity_weight * energySimilarity
	similarity += song_similarity_weight * songSimilarity
	similarity += transition_location_weight * transitionLocationSimilarity
	
	similarity /= (total_similarity_weight)
	return similarity

def calculateTrackSimilarity(track1, track2):
	track1_sections = track1.sections
	track2_sections = track2.sections
	total_sections = len(track1_sections) + len(track2_sections)
	similarities = np.zeros((total_sections, total_sections))
	for i, section1 in enumerate(track1_sections):
		for j, section2 in enumerate(track2_sections):
			section_12_similarity = calculateSectionSimilarity(section1, section2)
			similarities[i, j + len(track1_sections)] = section_12_similarity
			section_21_similarity = calculateSectionSimilarity(section2, section1)
			similarities[j + len(track1_sections), i] = section_21_similarity
	return similarities
