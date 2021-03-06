from pytube import YouTube
import os
import fileHandler as fh
from moviepy.editor import *

def StreamsVideo(streams):
    #print("Queste sono le risoluzioni per il video selezionato")
    list = []
    for stream in streams.filter(file_extension="mp4", mime_type="video/mp4", adaptive=True):
    #for stream in streams.filter(file_extension="mp4", mime_type="video/mp4"):
       #if "av01" in str(stream.video_codec[0:4]):
           #print("Risoluzione: "+stream.resolution)
        if not stream.resolution in list:
            list.append(stream.resolution)

    return list
    #return ["1080p", "720p", "480p", "360p"]


def downloadVideo(streams, title, res):
    try:
        # download the video as a mp4 in the selected directory stored in path
        streams.filter(file_extension="mp4", mime_type="video/mp4", resolution=res).first().download(filename=title)
        # if audio=true I want to download the video as a mp3 file
        return True
    except Exception as error:
        print(error)
        return False


def downloadAudio(streams, path, title):
    try:
        streams.filter(file_extension="mp4", mime_type="video/mp4").first().download(filename=title)
        # select the .mp4 video with the path and the title given by the user
        mp3_conv = VideoFileClip(path + "\\" + title + ".mp4")
        # conversion from mp4 to mp3
        mp3_conv.audio.write_audiofile(path + "\\" + title + ".mp3")
        # I close and "delete" the file descriptor that point at the selected .mp4 video downloaded
        mp3_conv.close()
        # deleting the video from the directory
        os.remove(path + "\\" + title + ".mp4")
        return True
    except Exception as error:
        print(error)
        return False


# streamList = list which contains all the resolution for a video
# audio = True/False indicates if the user want or not only the audio
# res = the download resolution wanted by the user
# this function checks if the resolution the user is looking for is in the list
def checkResolutionExistence(streamList, audio, res):
    # if the user wants only the audio, the program doesn't care about the resolution
    if not audio:
        # if the letter p isn't in the res string, just add it because it's important
        if "p" not in res:
            res += "p"

        # for every resolution in streamList we controll if res is in the list
        for streamResolution in streamList:
            # if there is correspondence between res and streamResolution return true
            if res == streamResolution.resolution:
                return True
        # if the compiler arrive here it means that, the resolution the user looking for doesn't exist
        return False
    else:
        # if the user only want the audio, just return true
        return True

# def printMessageBox():
#     inputWidgetHandler.CompleteGui().openMessageBox("Ho finito di scaricare il video!")

#function that allows to download the video and controll if everything is okay
def downloadVideoHandler(streams, path, audio, resolution):

    # take the title of the video
    title = streams.filter(file_extension="mp4", mime_type="video/mp4").first().title
    try:
        # checking the file existence and if the user want also the video
        #  True = file doesn't exist | not (false = want also the video) -> True and True = true
        if fh.checkFileEsistanceName(title, path, audio) and not audio:
            if downloadVideo(streams, title, resolution):
                print("[*] Ho finito di scaricare il video! [*]")
                return True
            else:
                return False
        #   True = file doesn't exist (.mp3)| true = only wants the audio -> True and True = true
        elif fh.checkFileEsistanceName(title, path, audio) and audio:
             if downloadAudio(streams, path, title):
                 print("[*] Ho finito di scaricare il video! [*]")
                 return True
             else:
                 return False
             #printMessageBox()

        else:
            title = fh.createAlternativeName(title, path, audio)
            if audio:
                if downloadAudio(streams, path, title):
                    print("[*] Ho finito di scaricare il video! [*]")
                    return True
                else:
                    return False
                #printMessageBox()

            else:
                if downloadVideo(streams, title, resolution):
                    print("[*] Ho finito di scaricare il video! [*]")
                    return True
                else:
                    return False
                # printMessageBox()


    except Exception as error:
        print("Non sono riuscito a scaricare il video :(")
        print("Error" + str(error))


def getYouTubeRef(url):
    video = YouTube(url)
    return video

def downloadVideoByUrl(url, downloadPath, res, audio):

    os.chdir(downloadPath)
    video = YouTube(url)
    # chose = str(input("Cosa vuoi scaricare? \n1) Solo audio \n2) Video\n3) Esci\n--> "))
    return downloadVideoHandler(video.streams, downloadPath, audio, res)


# https://www.youtube.com/watch?v=yKVmrjfzZLE
# https://www.youtube.com/watch?v=PCicKydX5GE -> 3 Sec Video