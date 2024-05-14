from acrcloud.recognizer import ACRCloudRecognizer
import json
import azapi

"""import pyaudio
import wave"""

API = azapi.AZlyrics('duckduckgo')

config = {
    'host': 'identify-eu-west-1.acrcloud.com',
    'access_key': '1a3db2d0d6c7ae05296ac8a0adbf21d2',
    'access_secret': 'ti4Kb8RvjTtWeoS895zv5OBDzzTtgW2m5rOcjBhf',
    'debug': True,
    'timeout': 10
}

acrcloud = ACRCloudRecognizer(config)

output = acrcloud.recognize_by_file('song.mp3', 0)

json_output = json.loads(output)

print("===")
print(json_output['metadata']['music'][0])

song_name = json_output['metadata']['music'][0]['title']
artist_name = json_output['metadata']['music'][0]['artists'][0]['name']

API.artist = artist_name
API.title = song_name

print(API.artist)
print(API.title)

API.getLyrics(save=True, ext="lrc")

print(API.lyrics)
