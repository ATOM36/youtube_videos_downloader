import webbrowser
from tkinter import Button, Label, StringVar, Tk
from pytube import YouTube


class Services:
    """Core class providing services used by the Window class"""

    def __init__(self) -> None:
        pass

    @classmethod
    def go_on_youtube(cls) -> None:
        """Opens a new YouTube tab in the default browser"""
        webbrowser.open_new_tab("https://www.youtube.com/")
    @classmethod
    def download_video(cls, window: Tk, video_link: StringVar):
        """Downloads a video from YouTube using the given link
        :param window:  the app's window
        :param video_link: a valid link to a YouTube video
        """

        url = YouTube(str(video_link.get()))
        # videos with a progressive stream have audio and video at the same time
        # the adaptative stream has whether audio, whether video
        # the filter method filters the stream's data
        videos_stream = url.streams.filter(progressive=True, file_extension="mp4")
        videos_stream.order_by('resolution')

        download_options = []
        videos = list(enumerate(videos_stream))
        for video in videos:
            download_options.append(video[1])

        height = 440
        for video in download_options:
            Button(window, text=video, bg="white", fg="green",
                   command=video.download()).place(x=950, y=height)
            height += 20

        Label(window, text="Terminé!!", font=("Lucida", 15), bg="white", fg="red").place(x=500, y=0)
