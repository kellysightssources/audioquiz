from pydub import AudioSegment
from pydub.playback import play
from pydub import effects
import random
import os
import glob

# TODO:
# 1. read from usb drive
#    ask whether to use all files found or only specific folders, if so, display checklist of folders
# 2. allow input from keyboard or virtual keyboard and match on answers
#    half credit for name of artist/show/anime, half credit for name of song
#    "did you mean" type matching, if strings are 90% similar or whatever
#    accept either song or artist or both at once
# 3. time limit
# 4. adjustable options (length of time, always start at beginning, speed, reverse, other options?)
# 5. options to replay clip or play another clip from same song but at different point, make sure segments don't overlap
#    deduct points, a few for replay, more for different segment
# 6. display answer after # of guesses or timeout or whatever
# 7. track overall score and display when quit
# 8. play until quit, or configurable number of songs
# 9. grouping? play multiple songs by artist or multiple songs from same anime

dir = 'quiz'
song_list = next(os.walk(dir))[2]
song_list_shuffle = random.sample(song_list, len(song_list))
current_segment = None

keep_going = True
count = 0
while keep_going and count < len(song_list_shuffle):
    song = AudioSegment.from_mp3(os.path.join(dir, song_list_shuffle[count]))
    duration = song.duration_seconds
    rand_beginning = random.randint(0, int(song.duration_seconds) - 20)
    rand_end = rand_beginning + 5
    current_segment = song[rand_beginning*1000:rand_end*1000]
    play(current_segment)
    print("Another? " + str(len(song_list) - (count + 1)) + " songs remain. y/n")
    count = count + 1
    if count < len(song_list_shuffle):
        answer = input()
    while answer == 'n':
        play(current_segment)
        print("Another? " + str(len(song_list) - (count + 1)) + " songs remain. y/n")
        answer = input()
    keep_going = True if answer == 'y' else False

def play_segment():
    play(current_segment)

def get_new_segment(song):
    duration = song.duration_seconds
    rand_beginning = random.randint(0, int(song.duration_seconds) - 20)
    rand_end = rand_beginning + 5
    current_segment = song[rand_beginning*1000:rand_end*1000]

def set_current_song(list, index):
    song = AudioSegment.from_mp3(os.path.join(dir, list[count]))

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
         = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
         = system('clear') 

def DisplayMenu():
    clear()
    print("            Song " + (count + 1) + " / " + str(len(song_list)))
    print()
    print("  A) Replay")
    print("  Y) Correct")
    print("  N) Incorrect")
    print("  Q) Quit")
    print("")
    print("Enter Input: ")

def Correct():
    score = score + 1

def Quit():
    keep_going = False
