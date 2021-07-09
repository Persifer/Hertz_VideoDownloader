from pytube import YouTube
import os
import fileHandler as fh
from moviepy.editor import *

class VideoHandler:

    def __init__(self, url="", path="", audio=False):
        self.audio = audio
        self.url = url
        self.path = path
        self.youtubeVideo = None

    def ProcessVideo(self):
        self.youtubeVideo = YouTube(self.url)