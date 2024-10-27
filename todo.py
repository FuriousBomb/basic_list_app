from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import re, requests, subprocess, urllib.parse, urllib.request 
import os

y = 20
x = 0
num_of_songs = 1

root = Tk()
root.title("G.I.D.E.O.N")
root.geometry('525x400')
root.iconbitmap('icon.ico')

tabs = 1
new_tab_count = 0

tab = ttk.Notebook(root)

def opentab():
    global tabs, new_tab_count, tab
    tabs += 1
    frame = ttk.Frame(tab)
    tab.add(frame, text=("Todo"+ " " + str(tabs)))
    tab.pack(fill="both", expand = 1)
    textbox = Text(tab, height=1, width = 50)
    textbox.place(x=2, y=40)
    button = Button(root, text="Save File As", command=save)
    button.place(x = 410, y = 35)
    results = Text(tab, height=15, width = 50)
    results.place(x=2, y=90)
    new_tab_count += 1

def save():
    txt = textbox.get('0.0', END)
    txt = txt.strip()
    text = results.get('0.0', END)
    asksave = asksaveasfile(initialfile= txt, filetypes=[("All Files", "*"),("Text Documents","*.txt"), ("Python File", "*.py"), ("Word Document", "*.docx")])    
    file = open(asksave.name, "w")
    for word in text:
        for char in word:
            file.write(char)
    file.close()
    messagebox.showinfo("", "File has been succesfully saved at " + asksave.name)
        
def remove():
    tab.forget("current")

def ask():
    root1 = Tk()
    root1.title("Music Player")
    root1.geometry('300x300')
    search = Text(root1, height=1, width = 50)
    search.pack()

    
    def play():
        music_name = search.get("0.0", END)
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        url = clip2.replace('","', "")
        os.popen("vlc --no-video " + url)
        root1.destroy()
                
    btn = Button(root1, text="Play", command=play)
    btn.place(x=130, y =40)
    
    
menu = Menu(root)
open_menu = Menu(menu)
play = Menu(menu)
menu.add_cascade(label="Add", menu=open_menu)
open_menu.add_command(label="Add New Todo", command=opentab)
menu.add_cascade(label="Play", menu=play)
play.add_command(label="Play a song", command=ask)
root.config(menu=menu)


frame1 = ttk.Frame(tab)

tab.add(frame1, text="Todo 1")
tab.pack(fill="both", expand = 1)


textbox = Text(tab, height=1, width = 50)
textbox.place(x=2, y=40)

results = Text(tab, height=15, width = 50)
results.place(x=2, y=90)

button = Button(root, text="Save File As", command=save)
button.place(x = 410, y = 35)

remove = Button(root, text="Remove Todo", command=remove)
remove.place(x = 200, y = 350)

root.mainloop()
