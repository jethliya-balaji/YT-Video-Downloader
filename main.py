import pytube
from pytube.cli import on_progress


while True:
    url = str(input("\n------------------------------------\n\nPast Youtube Link Here >>> "))
    videoStreams = pytube.YouTube(url, on_progress_callback=on_progress).streams
    videoOrAudio = str(input("\n------------------------------------\n\nTo Download In Video Formate Press 1\n\nTo Download In Audio Formate Press 2\n\n------------------------------------\n\n>>> "))
    if videoOrAudio == "1":
        quality = str(input("\n------------------------------------\n\nTo Download In High Quality H\n\nTo Download In Low Quality Press L\n\n------------------------------------\n\n>>> "))
        if quality.upper() == "H":
            videoStreams.get_highest_resolution().download()
            print("\n\n------------------------------------\n\nVideo Downloaded Successfully !! ")    
        elif quality.upper() == "L":
            videoStreams.get_lowest_resolution().download()
            print("\n------------------------------------\n\nVideo Downloaded Successfully !! ")    
    elif videoOrAudio == "2":
        videoStreams.filter(subtype='mp4',only_audio=True)[0].download()
        print("\n------------------------------------\n\Audio Downloaded Successfully !! ")    
