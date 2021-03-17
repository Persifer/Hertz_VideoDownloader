import os

def checkFileEsistanceName(title, path, audio):
    # if the dir is empty, surely the file doesn't exist
    if len(os.listdir(path)) == 0:
        return True

    if audio:
        title+=".mp3"
    else:
        title += ".mp4"

    # check if the filename exist in the dir
    if title in os.listdir(path):
        return False # return false if exist
    else:
        return True # retrun true if the filename doesn't exist

def createAlternativeName(title, path, audio):
    # If the final substring after the last _ contains any number...
    if (title[title.rfind("_") + 1:]).isnumeric():
        # Taking the number of the file, increment by one and then replace the number in the file title
        # ES: file_1 -> file_2
        title = title.replace(title[title.rfind("_") + 1:], str(int(title[title.rfind("_") + 1:]) + 1))
    else:
        # Se non contiene un numero finale allora lo aggiungo
        title += "_1"

    if checkFileEsistanceName(title, path, audio):
        return title
    else:
        return createAlternativeName(title, path, audio)