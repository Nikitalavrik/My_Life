from __future__ import unicode_literals
from concurrent.futures import ProcessPoolExecutor, as_completed
from bs4 import BeautifulSoup
from functools import partial
import requests
import youtube_dl 
import math
import sys
import os



sys.setrecursionlimit(5000)

full_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path2 = os.path.join(full_path, 'music', 'static', 'music') + "/"

files = os.listdir(r"./static/music/startpage")
music_files = os.listdir(r"music/static/music")

static_path  = r"/static/music/"



class Music():
    def __init__(self, url, name, yurl):
        self.url = url
        self.name = name
        self.youtube_url = yurl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
 

def ServerMusic():
    
    """Load Music from server on startpage"""

    audio = []
    static_path=r"/static/music/startpage/"
    for i in files:
        name=i[:-4]
        audio.append(Music(static_path + i, name, "#"))

    return audio  

def RequestSearch(search, numbers):

    
    req=requests.get("https://www.youtube.com/results?sp=EgIQAVAU&q=" + search)
    cont=req.content
    soup=BeautifulSoup(cont,"html.parser")

    #parser all videos
        
    all_video = soup.find_all("a", {"class" : "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})[0:numbers]
    return all_video

def SearchMusicinYoutube(all_video):

    """Function for search music on YouTube by entering request into Youtube"""

    audio=[]
    for video in all_video:
        if (video.text.replace(r'/',' ') + ".mp3") not in music_files:
            DownloadMusic(video.get("href"), video.text.replace(r'/',' '),)
            print(video.text)
        audio.append(Music(static_path + video.text.replace(r'/',' ') + ".mp3", video.text, video.get("href")))
    return audio

def DownloadMusic(path, name):

    download_path = full_path2
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': download_path + name + ".mp3",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),  
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
        ydl.download(['https://www.youtube.com' + path] ) 


def download_parralel(database):

    executor = ProcessPoolExecutor(max_workers = 4)
    fs = [executor.submit(polution_brand,link) for link in database]

    audio = []
    for future in as_completed(fs):
        audio += future.result() 
    return audio

def polution_brand(link):
    
    req=requests.get(link)
    cont=req.content
    soup=BeautifulSoup(cont,"html.parser")
    
    all_href = soup.find("div", {"class" : "yt-lockup-dismissable"})
    one_link = all_href.find("h3", {"class" : "yt-lockup-title "})
    a_link = one_link.find("a")
    audio = SearchMusicinYoutube([a_link])
        
    return audio
