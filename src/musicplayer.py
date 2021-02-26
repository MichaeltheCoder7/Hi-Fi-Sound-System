#coding:utf-8
#coding=gbk

import pygame
import tkinter
import os
import random

# create main window
player = tkinter.Tk()

# specify window settings
player.title("Music Player")
player.geometry("860x500+300+300")
player.resizable(0, 0) # prohibit changing size

# playlist
# path to directory that contains music files
file_path = os.path.dirname(__file__)
os.chdir(file_path + "\..\playlist")
songlist = os.listdir()

# create playlist
playlist_label = tkinter.Label(player, text="Playlist", background="light blue")
playlist = tkinter.Listbox(player, highlightcolor="blue", width=45, height=15, selectbackground="light blue", selectmode=tkinter.SINGLE)

# initialize pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5) # set initial volume

# one song for each row
for item in songlist:
    # Insert songs in reverse order
    # because insert is in that order
    position = len(songlist) - 1

    # Filtering files *.mp3
    if item.find(".mp3") !=-1:
        playlist.insert(position, item)
        pygame.mixer.music.queue(item)
    position -= 1

# global variables
is_paused = False # check if a song is paused
is_repeat = False
is_loop = False
is_random = False

# event when a song finished
SONG_END = pygame.USEREVENT + 1

# action events
def back_music():
    num = playlist.size()

    # if the there is a song selected
    if playlist.curselection():
        i = playlist.curselection()[0] # get the index of the selected song

        if i == 0:
            music_index = playlist.index(num - 1)
        else:
            music_index = playlist.index(i - 1)

        busy = pygame.mixer.music.get_busy() # determine whether there is a song playing before pressing this button
        pygame.mixer.music.load(playlist.get(music_index))
        var.set(playlist.get(tkinter.ACTIVE))

        if busy and is_paused == False:
            pygame.mixer.music.play() # play if it was already playing and not paused

        playlist.selection_clear(0, num - 1) # clear selections
        playlist.selection_set(music_index) # select the previous song
        playlist.activate(music_index) # activate the selection


def forward_music():
    num = playlist.size()

    if playlist.curselection():
        i = playlist.curselection()[0] # get the index of the selected song

        if i == num - 1:
            music_index = playlist.index(0)
        else:
            music_index = playlist.index(i + 1)

        busy = pygame.mixer.music.get_busy() # determine whether there is a song playing before pressing this button
        pygame.mixer.music.load(playlist.get(music_index))
        var.set(playlist.get(tkinter.ACTIVE))

        if busy and is_paused == False:
            pygame.mixer.music.play() # play if it was already playing and not paused
            
        playlist.selection_clear(0, num - 1) # clear selections
        playlist.selection_set(music_index) # select the next song
        playlist.activate(music_index) # activate the selection


def play_music():
    global is_paused
    is_paused = False # set pause to false

    # unpause the song if paused before and it's the same song
    # otherwise play music
    if pygame.mixer.music.get_busy() and playlist.get(tkinter.ACTIVE) == var.get():
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.load(playlist.get(tkinter.ACTIVE)) # load the song
        
        # set the song name based on selection
        var.set(playlist.get(tkinter.ACTIVE))
        pygame.mixer.music.play()

        # select the 1st song if no song is selected
        if len(playlist.curselection()) == 0:
            playlist.selection_set(0)
            playlist.activate(0)
        

def stop_music():
    global is_paused

    pygame.mixer.music.stop()
    is_paused = False


def pause_music():
    global is_paused

    pygame.mixer.music.pause()
    is_paused = True


def adjust_volume(value):
    pygame.mixer.music.set_volume(int(value) / 100)


# switch for repeat button
def switch_repeat():
    global is_loop
    global is_repeat
    global is_random

    if is_repeat:
        # turn off repeat
        button7.config(background="gray92")
        is_repeat = False
    else:
        # turn on repeat
        button7.config(background="dark gray")
        is_repeat = True

        # turn off loop if on
        if is_loop:
            button6.config(background="gray92")
            is_loop = False
        
        # turn off random if on
        if is_random:
            button8.config(background="gray92")
            is_random = False


# switch for loop button
def switch_loop():
    global is_loop
    global is_repeat
    global is_random

    if is_loop:
        # turn off loop
        button6.config(background="gray92")
        is_loop = False
    else:
        # turn on loop
        button6.config(background="dark gray")
        is_loop = True

        # turn off repeat if on
        if is_repeat:
            button7.config(background="gray92")
            is_repeat = False

        # turn off random if on
        if is_random:
            button8.config(background="gray92")
            is_random = False


# switch for random button
def switch_random():
    global is_loop
    global is_repeat
    global is_random

    if is_random:
        # turn off random
        button8.config(background="gray92")
        is_random = False
    else:
        # turn on random
        button8.config(background="dark gray")
        is_random = True

        # turn off repeat if on
        if is_repeat:
            button7.config(background="gray92")
            is_repeat = False

        # turn off loop if on
        if is_loop:
            button6.config(background="gray92")
            is_loop = False


def check_is_song_finished():
    num = playlist.size()

    # infinite loop to check for event
    for event in pygame.event.get():
        if event.type == SONG_END:
            i = playlist.curselection()[0] # get the index of the selected song

            if is_loop or is_repeat or is_random:
                if is_loop:
                    # get the next song and loop
                    if i == num - 1:
                        music_index = playlist.index(0)
                    else:
                        music_index = playlist.index(i + 1)
                elif is_repeat:
                    music_index = playlist.index(i) # get the same song and repeat
                elif is_random:
                    music_index = random.randint(0, num - 1) # get a random new song

                pygame.mixer.music.load(playlist.get(music_index))
                var.set(playlist.get(tkinter.ACTIVE))

                pygame.mixer.music.play() # play the song
                
                playlist.selection_clear(0, num - 1) # clear selections
                playlist.selection_set(music_index) # select the next song
                playlist.activate(music_index) # activate the selection

    player.after(100, check_is_song_finished) # run this function in background after GUI was activated


if __name__ == "__main__":

    # main image
    main_image = tkinter.PhotoImage(file=file_path + "/../images/cp.png")
    logo = tkinter.Label(player, image=main_image)

    # images for buttons
    image1 = tkinter.PhotoImage(file=file_path + "/../images/backbutton.png")
    image2 = tkinter.PhotoImage(file=file_path + "/../images/playbutton.png")
    image3 = tkinter.PhotoImage(file=file_path + "/../images/forwardbutton.png")
    image4 = tkinter.PhotoImage(file=file_path + "/../images/pausebutton.png")
    image5 = tkinter.PhotoImage(file=file_path + "/../images/stopbutton.png")
    image6 = tkinter.PhotoImage(file=file_path + "/../images/volume.png")
    image7 = tkinter.PhotoImage(file=file_path + "/../images/loop.png")
    image8 = tkinter.PhotoImage(file=file_path + "/../images/repeat.png")
    image9 = tkinter.PhotoImage(file=file_path + "/../images/random.png")

    # buttons
    button1 = tkinter.Button(player, width=55, height=55, image=image1, command=back_music)
    button2 = tkinter.Button(player, width=55, height=55, image=image2, command=play_music)
    button3 = tkinter.Button(player, width=55, height=55, image=image3, command=forward_music)
    button4 = tkinter.Button(player, width=55, height=55, image=image4, command=pause_music)
    button5 = tkinter.Button(player, width=55, height=55, image=image5, command=stop_music)
    button6 = tkinter.Button(player, width=27, height=27, image=image7, command=switch_loop)
    button7 = tkinter.Button(player, width=27, height=27, image=image8, command=switch_repeat)
    button8 = tkinter.Button(player, width=27, height=27, image=image9, command=switch_random)

    # scale bar for volume control
    volume_icon = tkinter.Label(player, image=image6)
    volume = tkinter.Scale(player, from_=0, to_=100, length=350, orient=tkinter.HORIZONTAL, resolution=1, command=adjust_volume)

    # label for song name
    var = tkinter.StringVar() # store the song name in var
    song_title = tkinter.Label(player, textvariable=var)

    volume.set(50) # default value is 50 for scale bar

    # place widgets
    # logo
    logo.grid(row=0, column=0, padx=20, pady=3, columnspan=30)

    # grid
    song_title.grid(row=0, column=0, columnspan=30) # song title in the center of the image
    playlist_label.grid(row=0, column=50, columnspan=150, sticky=tkinter.N+tkinter.W+tkinter.E, pady=30)
    playlist.grid(row=0, column=50, columnspan=500, sticky=tkinter.W+tkinter.E, padx=0, pady=50)

    # volume
    volume_icon.grid(row=2, column=50, sticky=tkinter.W+tkinter.E, ipadx=10)
    volume.grid(row=2, column=60, sticky=tkinter.N)

    # button
    button1.grid(row=2, column=10) # fastback_music
    button2.grid(row=2, column=12) # play_music
    button3.grid(row=2, column=14) # fastforward_music
    button4.grid(row=2, column=16) # pause_music
    button5.grid(row=2, column=18) # stop_music
    button6.grid(row=2, column=150, padx=10) # loop music
    button7.grid(row=1, column=150, padx=10) # repeat music
    button8.grid(row=3, column=150, padx=10) # random music

    # set up the endevent for loop_songs
    pygame.mixer.music.set_endevent(SONG_END)

    # background loop to check if a song has finished
    check_is_song_finished()

    # activate player
    player.mainloop()
    
    pygame.quit()
