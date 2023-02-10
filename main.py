#Steps
#1) download an album as a folder
        #buy on qobuz
#2) how to to open a folder and digest x amount of files in it
        #use os.listdir() to get a list of files in a folder
#3) process each song as data
        #use librosa to get the data of a song or whatever
        #figure whats the difference between each song
#4) what does data of a song look like (sounds, producers, lyrics, etc)
        #access some api to get the metadata of a song (producers, songwriters, lyrics, and order of songs so song 1 to song 2's relation)
#5) create some kind of proccessing algorithm to digest the frequencies and patterns of the different songs
#6) output some metric of how homogenous the album is
#7) maybe have a visual representation of the album
#    could be a word cloud, spotify wrap style visual, a web linking each song with % similarity between each song

#focusing on lyrics first
#finished getMetadata which correctly creates a dictionary of dictionary of the metadata of the album
#now need to clean the lyrics of the song, don't really need the perfect organizaiton of the song, but would be imporant to see keep the meaning for neural network

#***clean up code, dependencies, and data structure sI am using******
#create functions for singular song by number or by song name
#create functions for mass ports of entire album but by song names
#    if need the number for song just create a ounter variable while it iterates or something
import getMetadata
#create a dictionary
word_distribution = {}
getMetadata.asker()
allLyrics = getMetadata.getAlbumLyrics()
word_distribution = getMetadata.getLyricsDistribution(0)

for i in allLyrics:
    word_distribution.append(getMetadata.getLyricsDistribution(i))

#export the data as a data table instead and then graph in power bi
#getMetadata.plot_word_distribution(word_distribution)