import webbrowser
from tkinter import *

from pytube import YouTube

# telechargement
def create_entry():
    message = Label(window, font=("Lucida", 10), text="Coller le lien de la vidéo ici:"
                    , relief=RAISED, bg="red", fg="white")
    can.create_image(980, 310, image=here)
    message.place(x=1020, y=280)
    lien = Entry(window, font=("Lucida", 15), bg="white", fg="black",
                 relief=RAISED, textvariable=v).place(x=1020, y=300)

    Button(window, text="Télécharger", font=("Lucida", 15), relief=RAISED, activeforeground="red",
           bg="white", fg="red", activebackground="red", command=get_video).place(x=1080, y=350)


# pour avoir plusieurs actions sur un bouton
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


def get_video():
    # les videos au flux progressif ont l'audio et la vidéo à la fois
    # le flux adaptatif a soit l'un soit l'autre

    # la méthode filter permet de filtrer les résultats de stream
    url = YouTube(str(v.get()))
    video = url.streams.filter(progressive=True, file_extension="mp4")
    video.order_by('resolution')
    l = []
    vid = list(enumerate(video))
    for i in vid:
        l.append(i[1])
    j = 440
    for i in l:
        Button(window, text=i, bg="white", fg="green",
               command=i.download()).place(x=950, y=j)
        j += 20

    Label(window, text="Terminé!!", font=("Lucida", 15), bg="white", fg="red").place(x=500, y=0)


def go_youtube():
    webbrowser.open_new_tab("https://www.youtube.com/")


# fenêtre principale
window = Tk()
window.geometry("1368x720")
window.minsize(720, 480)
window.title("Youtube video downloader")
window.config(background="#B22222")

here = PhotoImage(file='../hand.png').subsample(20)
image = PhotoImage(file="../tube2.png").subsample(1, 2).zoom(2)

can = Canvas(window, width=1368, height=720, bd=0, highlightthickness=0)
can.create_image(684, 360, image=image)

can.pack(expand=YES, fill=Y)

v = StringVar()

# boutons et textes
text1 = Label(window, text="Aller sur Youtube",
              font=("Lucida", 20), bg="white", fg="red")
text1.place(x=160, y=170)
button1 = Button(window, text="Cliquez ici", font=("Lucida", 18), bg="white", fg="red", command=go_youtube,
                 relief=RAISED, activeforeground="red", activebackground="red")

button1.place(x=200, y=220)

text2 = Label(window, text="Faire un téléchargement",
              font=("Lucida", 20), bg="white", fg="red")
text2.place(x=1020, y=170)

# le paramètre activebackground permet de changer la couleur d'arrière plan lors du clique
x = Button(window, text="Oui", font=("Lucida", 15), bg="white", fg="red", command=create_entry,
           relief=RAISED, activeforeground="red", activebackground="red", width=10, height=1).place(x=1100, y=220)

y = Button(window, text="Non,quittez l'application", font=("Lucida", 15), bg="white", fg="red",
           relief=RAISED, activeforeground="red", command=window.quit, activebackground="black").place(x=600, y=550)

window.mainloop()
