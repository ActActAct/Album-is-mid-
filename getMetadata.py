#bunch of functions to get the metadata and clean it
#also bunch of functions to get the lyrics and clean it
import json
import re
import matplotlib.pyplot as plt
from lyricsgenius import Genius
from collections import Counter



genius = Genius("U-a-_BwPRV75Nr3OolkpIJ4kk8UJpELB9PeZYEFmd32x8RvfdG0DX5Eyi45tAAZ0")
tracks = []
albumLyrics = {}


def asker():
    albumName = input("What is the name of the album you want to analyze? ")
    artistName = input("Who is the artist of the album you want to analyze? ")
    scraper(albumName, artistName)


def scraper(albumName, artistName):

    #access producers and songwriters
    album = genius.search_album(albumName, artistName)
    album.save_lyrics()

    #save json as a dictionary
    album_name = album.name.replace(" ", "")
    name = 'Lyrics_' + album_name + '.json'


    with open(name) as json_file:
        data = json.load(json_file)

    for item in data["tracks"]:
        tracks.append(dict(item))


#get the song from the album with the key
def cleaner(lyrics):
    #remove the text before the word Lyrics including the word Lyrics
    lyrics = lyrics[lyrics.find("Lyrics")+6:]
    #remove any instance of 123Embed
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    lyrics = re.sub(r'You might also like', '', lyrics)
    lyrics = re.sub(r'\d+Embed', '', lyrics)

    return lyrics


#get a single songs lyrics
def getLyrics(number):

    return cleaner(tracks[number]["song"]["lyrics"])


def getAlbumLyrics():

    for i in range(len(tracks)):
        #key is song name and item is lyrics
        albumLyrics[tracks[i]["song"]] = getLyrics(i)

    return albumLyrics

def getProducers(number):

    return 0
    #use the link write somebot/code to collect producers and songwriters
    #return list_of_dicts[number]["song"]

#can call a loop in main that does this for each song
def getLyricsDistribution(number):

    words = re.findall(r'\b\w+\b', lyrics)
    return Counter(words)


#parameter is a dictionary of words and their counts
def plot_word_distribution(word_counts):
    words = list(word_counts.keys())
    counts = list(word_counts.values())

    # sort the word counts in descending order
    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    words = list(word_counts.keys())
    counts = list(word_counts.values())

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_axes([0, 0, 1, 1])

    bars = ax.bar(words, counts)
    plt.xticks(rotation=90)
    ax.set_xlabel("Words")
    ax.set_ylabel("Frequency")
    ax.set_title("Word Distribution in Song Lyrics")

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, height, ha='center', va='bottom')

    plt.show()
    return 0





