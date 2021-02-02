#coding:utf-8
#coding=gbk

import pygame
import tkinter
import os

# create main window
player = tkinter.Tk()

# specify window settings
player.title("Music Player")
player.geometry("900x500+300+300")
player.resizable(0,0) # prohibit change form size

# playlist
# path to directory that contains music files
file_path = os.path.dirname(__file__)
os.chdir(file_path + "\..\playlist")
songlist = os.listdir()

# create playlist
playlist_label = tkinter.Label(player, text="Playlist", background="light blue")
playlist = tkinter.Listbox(player, highlightcolor="blue", width=50, height=15, selectbackground="light blue", selectmode=tkinter.SINGLE)

# initialize pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5) # set initial volume

# one song for each row
for item in songlist:
    position = 0
    playlist.insert(position, item)
    position += 1
    pygame.mixer.music.queue(item)

# action events
def back_music():
    num = playlist.size()
    i = 0
    while int(i) < num:
        if playlist.selection_includes(i) == True:
            if i == 0:
                music_name=playlist.index(num - 1)
            else:
                music_name=playlist.index(i - 1)
            pygame.mixer.music.load(playlist.get(music_name))
            var.set(playlist.get(tkinter.ACTIVE))
            pygame.mixer.music.play()
            break
        else:
            i = i + 1

def forward_music():
    num = playlist.size()
    i = 0
    while int(i) < num:
        if playlist.selection_includes(i) == True:
            if i == num - 1:
                music_name=playlist.index(0)
            else:
                music_name=playlist.index(i + 1)
            pygame.mixer.music.load(playlist.get(music_name))
            var.set(playlist.get(tkinter.ACTIVE))
            pygame.mixer.music.play()
            break
        else:
            i = i + 1

def play_music():
    # unpause the song if paused before and it's the same song
    # otherwise play music
    if pygame.mixer.music.get_busy() and playlist.get(tkinter.ACTIVE) == var.get():
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.load(playlist.get(tkinter.ACTIVE)) # load the song
        # set the song name based on selection
        var.set(playlist.get(tkinter.ACTIVE))
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def adjust_volume(value):
    pygame.mixer.music.set_volume(int(value) / 100)

if __name__ == "__main__":
    pos=0
    position1=1

    # main image
    main_image = tkinter.PhotoImage(file=file_path + "/../images/cp1.png")
    logo = tkinter.Label(player, image = main_image)

    # images for buttons
    image1 = tkinter.PhotoImage(file=file_path + "/../images/backbutton1.png")
    image2 = tkinter.PhotoImage(file=file_path + "/../images/playbutton1.png")
    image3 = tkinter.PhotoImage(file=file_path + "/../images/forwardbutton1.png")
    image4 = tkinter.PhotoImage(file=file_path + "/../images/pausebutton1.png")
    image5 = tkinter.PhotoImage(file=file_path + "/../images/stopbutton1.png")
    image6 = tkinter.PhotoImage(file=file_path + "/../images/volume2.png")

    # buttons
    button1 = tkinter.Button(player, width=80, height=80, image=image1, command=back_music)
    button2 = tkinter.Button(player, width=80, height=80, image=image2, command=play_music)
    button3 = tkinter.Button(player, width=80, height=80, image=image3, command=forward_music)
    button4 = tkinter.Button(player, width=80, height=80, image=image4, command=pause_music)
    button5 = tkinter.Button(player, width=80, height=80, image=image5, command=stop_music)

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
    playlist_label.grid(row=0, column=50, columnspan=100, sticky=tkinter.N+tkinter.W+tkinter.E, pady=30)
    playlist.grid(row=0, column=50, columnspan=500, sticky=tkinter.W+tkinter.E, padx=0, pady=60)

    # volume
    volume_icon.grid(row=1, column=50, sticky=tkinter.W+tkinter.E, ipadx=10)
    volume.grid(row=1, column=80, sticky=tkinter.N)

    # button
    button1.grid(row=1, column=10) # fastback_music
    button2.grid(row=1, column=12) # play_music
    button3.grid(row=1, column=14) # fastforward_music
    button4.grid(row=1, column=16) # pause_music
    button5.grid(row=1, column=18) # stop_music

    # activate player
    player.mainloop()