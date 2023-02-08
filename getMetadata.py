#get the metadata of the song before we start using an algorithm to parse the lyrics and metadata of the song
import json
import pandas as pd
from lyricsgenius import Genius

genius = Genius("U-a-_BwPRV75Nr3OolkpIJ4kk8UJpELB9PeZYEFmd32x8RvfdG0DX5Eyi45tAAZ0")


def asker():
    albumName = input("What is the name of the album you want to analyze? ")
    artistName = input("Who is the artist of the album you want to analyze? ")
    scraper(albumName, artistName)


def scraper(albumName, artistName):

    #access producers and songwriters
    album = genius.search_album(albumName, artistName)
    album.save_lyrics()

    #save json as a dictionary
    name = 'Lyrics_' + album.name + '.json'
    with open(name) as json_file:
        data = json.load(json_file)
    json_file.close()

    #print the data from data
    #organize the data
    df = pd.DataFrame.from_dict(data, orient='index', columns=["Value"])
    print(df["tracks"])

with open("Lyrics_Donda.json") as json_file:
    data = json.load(json_file)
json_file.close()
df = pd.DataFrame.from_dict(data, orient='index', columns=["Value"])
df = df.transpose()
df = pd.json_normalize(df["tracks"])
df = df.transpose()
trackList = []
print(df[0][0])
for i in range(len(df)):
    trackList.append(pd.json_normalize(df[0][i]))
#adds a 0 to the front, becasue it thinks its an identifier
#switch the indexing to the number of the tracks
print(trackList[0])
