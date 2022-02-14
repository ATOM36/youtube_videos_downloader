import os
from tkinter import Button, Label, Tk, PhotoImage, Canvas, StringVar, RAISED, Entry, YES, Y

from services import Services


class Window:
    """The whole app's GUI"""

    # video link
    link: StringVar

    # labels
    youtube_label: Label
    download_label: Label

    # buttons
    youtube_button: Button
    break_button: Button
    entry_maker: Button

    def __init__(self) -> None:
        """Creates a whole configured GUI for the app"""
        # window config
        self.background_image = None
        self.hand_image = None
        self.canvas = None
        self.window = Tk()
        self.window.geometry("1368x720")
        self.window.minsize(720, 480)
        self.window.title("Youtube video downloader")
        self.window.config(background="#B22222")
        self.load_image()

        # labels config
        self.youtube_label = Label(self.window, text="Aller sur Youtube", font=("Lucida", 20), bg="white",
                                   fg="red")
        self.youtube_label.place(x=160, y=170)

        self.download_label = Label(self.window, text="Faire un téléchargement", font=("Lucida", 20), bg="white",
                                    fg="red")
        self.download_label.place(x=1020, y=170)

        self.link = StringVar()

        # buttons config
        self.entry_maker = Button(self.window, text="Oui", font=("Lucida", 15), bg="white", fg="red",
                                  command=self.__create_entry, relief=RAISED, activeforeground="red",
                                  activebackground="red", width=10, height=1)
        self.entry_maker.place(x=1100, y=220)

        self.youtube_button = Button(self.window, text="Cliquez ici", font=("Lucida", 18), bg="white", fg="red",
                                     command=Services.go_on_youtube, relief=RAISED, activeforeground="red",
                                     activebackground="red")
        self.youtube_button.place(x=200, y=220)

        self.break_button = Button(self.window, text="Non,quittez l'application", font=("Lucida", 15), bg="white",
                                   fg="red", relief=RAISED, activeforeground="red", command=self.window.quit,
                                   activebackground="black")
        self.break_button.place(x=600, y=550)

        self.window.mainloop()

    def load_image(self):
        """Prepares the canvas and used image assets"""
        self.canvas: Canvas = Canvas(self.window, width=1368, height=720, bd=0, highlightthickness=0)
        self.background_image: PhotoImage = PhotoImage(file=self.__background_image_path()).subsample(1, 2).zoom(2)
        self.canvas.create_image(684, 360, image=self.background_image)
        self.canvas.pack(expand=YES, fill=Y)

    def __hand_image_path(self) -> str:
        """Returns the path to hand image file"""
        directory = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(directory, "assets", "hand.png")

    def __background_image_path(self) -> str:
        """Returns the path to YouTube image file"""
        directory = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(directory, "assets", "tube2.png")

    def __create_entry(self) -> None:
        """Creates the entry in which the video will be pasted"""
        Label(self.window, font=("Lucida", 10), text="Coller le lien de la vidéo ici:", relief=RAISED, bg="red",
              fg="white").place(x=1020, y=280)

        self.hand_image: PhotoImage = PhotoImage(file=self.__hand_image_path()).subsample(20)
        self.canvas.create_image(980, 310, image=self.hand_image)
        Entry(self.window, font=("Lucida", 15), bg="white", fg="black", relief=RAISED, textvariable=self.link).place(
            x=1020, y=300)

        Button(self.window, text="Télécharger", font=("Lucida", 15), relief=RAISED, activeforeground="red",
               bg="white", fg="red", activebackground="red", command=self.__download_video).place(x=1080, y=350)

    def __download_video(self) -> None:
        Services.download_video(self.window, self.link)
