#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
import tkMessageBox



root = Tk()
root.wm_title("MUSIC PLAYER")
root.minsize(500,500)


listofsongs=[]
realnames = []

v =StringVar()
songlabel =Label(root,textvariable=v,width=80)
index=0
count=0

global ctr
ctr=0


def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    #return songname

def pausesong(event):
    global ctr
    ctr += 1
    if (ctr%2!=0):
        pygame.mixer.music.pause()
    if(ctr%2==0):
        pygame.mixer.music.unpause()

def playsong(event):
    pygame.mixer.music.play()


def nextsong(event):
    global index
    index += 1
    if (index < count):
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    else:
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    try:
      updatelabel()
    except NameError:
        print("")

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    try:
        updatelabel()
    except NameError:
        print("")


def stopsong(event):

    pygame.mixer.music.stop()
    #v.set("")
    #return songname
def mute(event):
    vol.set(0)



label = Label(root,text="Music Player")
label.pack()

listbox=Listbox(root,selectmode=MULTIPLE,width=100,height=20,bg="grey",fg="black")
listbox.pack(fill=X)




def directorychooser():
  global count
  global index
    #count=0

  directory = askdirectory()
  if(directory):
    count=0
    index=0
    #listbox.delete(0, END)
    del listofsongs[:]
    del realnames[:]

    os.chdir(directory)

    for  files in os.listdir(directory):

        try:
         if files.endswith(".mp3"):

              realdir = os.path.realpath(files)
              audio = ID3(realdir)
              realnames.append(audio['TIT2'].text[0])
              listofsongs.append(files)
        except:
            print(files+" is not a song")

    if listofsongs == [] :
       okay=tkMessageBox.askretrycancel("No songs found","no songs")
       if(okay==True):
           directorychooser()

    else:
        listbox.delete(0, END)
        realnames.reverse()
        for items in realnames:
            listbox.insert(0, items)
        for i in listofsongs:
            count = count + 1
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])

        pygame.mixer.music.play()
        try:
            updatelabel()
        except NameError:
            print("")
  else:
    return 1

try:
        directorychooser()
except WindowsError:
         print("thank you")


def call(event):


 if(True):
    try:
        #pygame.mixer.music.stop()
        k=directorychooser()

    except WindowsError:
         print("thank you")

realnames.reverse()







songlabel.pack()


def show_value(self):
    i = vol.get()
    pygame.mixer.music.set_volume(i)

vol = Scale(root,from_ = 10,to = 0,orient = VERTICAL ,resolution = 10,command = show_value)
vol.place(x=85, y = 380)
vol.set(10)

framemiddle =Frame(root,width=250,height=30)
framemiddle.pack()


framedown =Frame(root,width=400,height=300)
framedown.pack()

openbutton = Button(framedown,text="open")
openbutton.pack(side=LEFT)

mutebutton = Button(framedown,text=u"\U0001F507")
mutebutton.pack(side=LEFT)

previousbutton = Button(framedown,text="◄◄")
previousbutton.pack(side=LEFT)


playbutton = Button(framedown,text="►")
playbutton.pack(side=LEFT)

stopbutton = Button(framedown,text="■")
stopbutton.pack(side=LEFT)

nextbutton = Button(framedown,text="►►")
nextbutton.pack(side=LEFT)


pausebutton = Button(framedown,text="►/║║")
pausebutton.pack(side=LEFT)





mutebutton.bind("<Button-1>",mute)
openbutton.bind("<Button-1>",call)
playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)
pausebutton.bind("<Button-1>",pausesong)



root.mainloop()
