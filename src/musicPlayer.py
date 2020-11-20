import pygame
import tkinter
import os

# create main window
player = tkinter.Tk()

# specify window settings
player.title("Music Player")
player.geometry("235x530")

# playlist
# path to directory that contains music files
os.chdir("C:/Users/Michael Yang/OneDrive/Desktop/Music Player/playlist")
songlist = os.listdir()

# create playlist
playlist_label = tkinter.Label(player, text="Playlist", background="light grey")
playlist = tkinter.Listbox(player, highlightcolor="blue", selectmode=tkinter.SINGLE)
# one song for each row
for item in songlist:
    position = 0
    playlist.insert(position, item)
    position += 1

# initialize pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5) # set initial volume

# action events
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

def pause():
    pygame.mixer.music.pause()

def adjust_volume(value):
    pygame.mixer.music.set_volume(int(value) / 100)

# main image
main_image = tkinter.PhotoImage(file="C:/Users/Michael Yang/OneDrive/Desktop/Music Player/images/logo.png")
logo = tkinter.Label(player, image = main_image)

# images for buttons
# path to the images
image1 = tkinter.PhotoImage(file="C:/Users/Michael Yang/OneDrive/Desktop/Music Player/images/playbutton.png")
image2 = tkinter.PhotoImage(file="C:/Users/Michael Yang/OneDrive/Desktop/Music Player/images/pausebutton.png")
image3 = tkinter.PhotoImage(file="C:/Users/Michael Yang/OneDrive/Desktop/Music Player/images/stopbutton.png")
image4 = tkinter.PhotoImage(file="C:/Users/Michael Yang/OneDrive/Desktop/Music Player/images/volume.png")

# buttons
button1 = tkinter.Button(player, width=60, height=50, image=image1, command=play_music)
button2 = tkinter.Button(player, width=60, height=50, image=image2, command=pause)
button3 = tkinter.Button(player, width=60, height=50, image=image3, command=stop_music)

# scale bar for volume control
volume_icon = tkinter.Label(player, image = image4)
volume = tkinter.Scale(player, from_=0, to_=100, orient=tkinter.HORIZONTAL,
                       resolution=1, command=adjust_volume)

# label for song name
var = tkinter.StringVar() # store the song name in var
song_title = tkinter.Label(player, textvariable = var)

volume.set(50) # default value is 50 for scale bar

# place widgets
# grid
song_title.grid(row=0, column=0, columnspan=30) # title is at the top
logo.grid(row=1, column=0, padx=6, pady=3, columnspan=30)
button3.grid(row=2, column=0, padx=9, columnspan=10)
button1.grid(row=2, column=10, columnspan=10)
button2.grid(row=2, column=20, padx=9, columnspan=10)
volume_icon.grid(row=3, column=0, padx=6, pady=3)
volume.grid(row=3, column=1, columnspan=29, sticky=tkinter.W+tkinter.E, padx=6, pady=3)
playlist_label.grid(row=4, column=0, columnspan=30, sticky=tkinter.W+tkinter.E, padx=9)
playlist.grid(row=5, column=0, columnspan=30, sticky=tkinter.W+tkinter.E, padx=9)

# activate player
player.mainloop()