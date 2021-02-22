#coding:utf-8
#coding=gbk

import pygame
import tkinter
import os

# create main window
player = tkinter.Tk()

# specify window settings
player.title("Music Player")
player.geometry("850x490+300+300")
player.resizable(0,0) # prohibit change form size

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

# global variable to check if a sound is paused
is_paused = False

# action events
def back_music():
    num = playlist.size()

    # if the there is song selected
    if playlist.curselection():
        i = playlist.curselection()[0] # get the index of the selected song

        if i == 0:
            music_name = playlist.index(num - 1)
        else:
            music_name = playlist.index(i - 1)

        busy = pygame.mixer.music.get_busy() # determine whether there is a song playing before pressing this button
        pygame.mixer.music.load(playlist.get(music_name))
        var.set(playlist.get(tkinter.ACTIVE))

        if busy and is_paused == False:
            pygame.mixer.music.play() # play if it was already playing and not paused

        playlist.selection_clear(0, num - 1) # clear selections
        playlist.selection_set(music_name) # select the previous song
        playlist.activate(music_name) # activate the selection


def forward_music():
    num = playlist.size()

    if playlist.curselection():
        i = playlist.curselection()[0] # get the index of the selected song

        if i == num - 1:
            music_name = playlist.index(0)
        else:
            music_name = playlist.index(i + 1)

        busy = pygame.mixer.music.get_busy() # determine whether there is a song playing before pressing this button
        pygame.mixer.music.load(playlist.get(music_name))
        var.set(playlist.get(tkinter.ACTIVE))

        if busy and is_paused == False:
            pygame.mixer.music.play() # play if it was already playing and not paused
            
        playlist.selection_clear(0, num - 1) # clear selections
        playlist.selection_set(music_name) # select the next song
        playlist.activate(music_name) # activate the selection


def play_music():
    global is_paused
    pause = False # set pause to false

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


def repeat_music():
    pygame.mixer.music.play(-1)
   

def exit_music():
    os._exit(0)


if __name__ == "__main__":

    # main image
    main_image = tkinter.PhotoImage(file=file_path + "/../images/cp.png")
    logo = tkinter.Label(player, image = main_image)

    # images for buttons
    image1 = tkinter.PhotoImage(file=file_path + "/../images/backbutton.png")
    image2 = tkinter.PhotoImage(file=file_path + "/../images/playbutton.png")
    image3 = tkinter.PhotoImage(file=file_path + "/../images/forwardbutton.png")
    image4 = tkinter.PhotoImage(file=file_path + "/../images/pausebutton.png")
    image5 = tkinter.PhotoImage(file=file_path + "/../images/stopbutton.png")
    image6 = tkinter.PhotoImage(file=file_path + "/../images/volume.png")
    image7 = tkinter.PhotoImage(file=file_path + "/../images/exitbutton.png")
    image8 = tkinter.PhotoImage(file=file_path + "/../images/repeat.png")

    # buttons
    button1 = tkinter.Button(player, width=55, height=55, image=image1, command=back_music)
    button2 = tkinter.Button(player, width=55, height=55, image=image2, command=play_music)
    button3 = tkinter.Button(player, width=55, height=55, image=image3, command=forward_music)
    button4 = tkinter.Button(player, width=55, height=55, image=image4, command=pause_music)
    button5 = tkinter.Button(player, width=55, height=55, image=image5, command=stop_music)
    button6 = tkinter.Button(player, width=35, height=35, image=image7, activebackground="light blue", command=exit_music)
    button7 = tkinter.Button(player, width=35, height=35, image=image8, command=repeat_music)

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
    playlist.grid(row=0, column=50, columnspan=500, sticky=tkinter.W+tkinter.E, padx=0, pady=60)

    # volume
    volume_icon.grid(row=1, column=50, sticky=tkinter.W+tkinter.E, ipadx=10)
    volume.grid(row=1, column=60, sticky=tkinter.N)

    # button
    button1.grid(row=1, column=10) # fastback_music
    button2.grid(row=1, column=12) # play_music
    button3.grid(row=1, column=14) # fastforward_music
    button4.grid(row=1, column=16) # pause_music
    button5.grid(row=1, column=18) # stop_music
    button6.grid(row=2, column=150, sticky=tkinter.W+tkinter.E) # exit_music
    button7.grid(row=1, column=150, sticky=tkinter.W+tkinter.E) # repeat_music

    # activate player
    player.mainloop()