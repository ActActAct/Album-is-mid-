#bunch of functions to get the metadata and clean it
#also bunch of functions to get the lyrics and clean it
import json
from lyricsgenius import Genius

genius = Genius("U-a-_BwPRV75Nr3OolkpIJ4kk8UJpELB9PeZYEFmd32x8RvfdG0DX5Eyi45tAAZ0")
list_of_dicts = []

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
        list_of_dicts.append(dict(item))


#get the song from the album with the key
def cleaner(lyrics):
    #remove the text before the word Lyrics including the word Lyrics
    lyrics = lyrics[lyrics.find("Lyrics")+6:]
    #remove any instance of 123Embed
    return lyrics.replace("123Embed", "")



def getLyrics(number):

    return cleaner(list_of_dicts[number]["song"]["lyrics"])


def getAlbumLyrics():

    allLyrics = []

    for i in range(len(list_of_dicts)):
        allLyrics.append(getLyrics(i))

    return allLyrics

def getProducers(number):

    #use the link write somebot/code to collect producers and songwriters
    return list_of_dicts[number]["song"]






