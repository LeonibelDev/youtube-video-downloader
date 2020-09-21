import youtube_dl
import os

save_path = "C:/users/Leonibel/Downloads/videos"

yt_obj = {
    'outtmpl':save_path + '/%(title)s.%(ext)s'
} 

def download_video(links):
    links = links.split(" ")

    for link in links:

        with youtube_dl.YoutubeDL(yt_obj) as ydl:
            ydl.download([link])