from tkinter import *
from tkinter import ttk, filedialog
from pygame import mixer
import os

background = "#22223b"

root = Tk()
root.title("Music Player")
root.geometry("600x500")
root.config(background=background)
root.resizable(False, False)
mixer.init()



def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs =  os.listdir(path)
        print(songs)  
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
                
def play_song():
    music_name = playlist.get(ACTIVE)
    print(music_name)
    mixer.music.load(music_name)
    mixer.music.play()
#Icons Setting Up

image_icon = PhotoImage(file="assets/music_logo.png")
Label(root,image=image_icon, background=background, ).place(x=40,y=20)

Label(root, text="Music Peace", background=background, foreground="white",font=("Arial", 40, "italic")).place(x=220,y=50)


#button

play_button = PhotoImage(file="assets/play.png")
Button(root, image=play_button,background=background,command=play_song, bd=0, highlightthickness=0,).place(x=470,y=200)

pause_button = PhotoImage(file="assets/pause.png")
Button(root, image=pause_button,background=background,command=mixer.music.pause, bd=0).place(x=470,y=300)

stop_button = PhotoImage(file="assets/stop.png")
Button(root, image=stop_button,background=background,command=mixer.music.stop, bd=0).place(x=470,y=400)

#Frame
# canvas = Canvas(root,width=370,height=250,bd=2,).place(x=50,y=200)
# canvas.grid(column=0,pady=200,padx=50)

open_folder_btn = Button(root,text='Open Folder',command=open_folder, bg="#48cae4" ,fg="white",bd=0,font=("Arial",10,"bold"), width=10,height=2).place(x=340,y=150)

#Scroll Bar
playlist = Listbox(root, width=54,height=14,font=("arial", 10, ),fg="black", bd=0,cursor="hand2")
playlist.place(y=200,x=50)



root.mainloop()