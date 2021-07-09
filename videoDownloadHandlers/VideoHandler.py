from pytube import YouTube
import os
import fileHandler as fh
import re
from moviepy.editor import *

class VideoHandler:

    def __init__(self, url="", path="", audio=False):
        self.__audio = audio
        self.__url = url
        self.__path = path
        self.__youtubeVideo = None

# Setter and getter for the url of the video
    def setVideoUrl(self, url):
        # controll if what is passed is a string and match with a valid url for youtube's video
        if type(url) is str and re.match(r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$", url):
            self.__url = url
        else:
            raise Exception("[!] Invalid url, rewrite it [!]")

    def getVideoUrl(self):
        return self.__url
############################################

# Setter and getter for the destination path
    def setPath(self, path):
        #controll if what is passed is a string and match with a valid path for windows directory
        if type(path) is str and re.match(r'^[a-zA-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$', path):
            self.__path = path
        else:
            raise Exception("[!] Invalid path, rewrite it [!]")

    def getPath(self):
        return self.__path

############################################

# Setter and getter for the audio
    def setAudio(self, audio):
        # controll if what is passed is a boolan type
        if type(audio) is bool:
            self.__audio = audio
        else:
            raise Exception("[!] Invalid audio, insert a boolean type [!]")

    def isAudioEnable(self):
        return self.__audio

############################################


    def __setProcessedVideo(self):
        self.youtubeVideo = YouTube(self.__url)

    def getProcessedVideo(self):
        return self.youtubeVideo