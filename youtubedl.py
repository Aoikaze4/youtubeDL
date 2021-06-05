import youtube_dl
import shutil
import os

videoUrl = input("plz type URL:")
audioDict = '/audio'

pref = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

with youtube_dl.YoutubeDL(pref) as ydl:
    videoInfo = ydl.extract_info(videoUrl, download='True')

shutil.move('./' + videoInfo['title'] + '.mp3', './audio')

print(videoInfo['title']+'¥n'+videoInfo['url'])
print('Downloaded.')
