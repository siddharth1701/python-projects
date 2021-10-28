# pafy module - Pafy is a Python library to download YouTube content and retrieve metadata.

"""
Below are the list of features Pafy offers
1. Retrieve metadata such as viewcount, duration, rating, author, thumbnail, keywords 
2. Download video or audio at requested resolution / bitrate / format / filesize 
2. Command line tool (ytdl) for downloading directly from the command line 
3. Retrieve the URL to stream the video in a player such as vlc or mplayer 
4. Works with age-restricted videos and non-embeddable videos 
5. Small, standalone, single importable module file 
6. Select highest quality stream for download or streaming 
7. Download video only (no audio) in m4v or webm format 
8. Download audio only (no video) in ogg or m4a format 
9. Retrieve playlists and playlist metadata 
10. Works with Python 2.6+ and 3.3+ 

pip install pafy
pip install youtube_dl
"""
import os
os.path.abspath(os.getcwd())
print(os.path.abspath(os.getcwd()))
print(os.path.dirname(os.path.realpath(__file__)))

dir = "audio"
if not os.path.exists(dir):
    os.mkdir(dir)

# importing pafy
import pafy

# url of video
url = input("Enter youtube URL: ")

# instant created
video = pafy.new(url)

###### Program to get the number of views on a video
# getting number of view count
# view_count = video.viewcount
# print("View Count : " + str(view_count))

###### Program to get the thumb image of a video 
# getting thumb image
# thumb_count = video.thumb
# print("Thumb Image : " + str(thumb_count))


###### Program to get the thumb image of a video 
# getting title
# title_value = video.title
# print("Title : " + str(title_value))

###### list available streams for a video:
# streams = video.streams
# print("List available streams for a video: ")
# for s in streams:
#     print(s)


###### some other attributes:
print("Video Title: ",video.title)
print("Video Thumb: ",video.thumb)
print("Video Rating: ",video.rating)
print("Video VeiwCount: ",video.viewcount)
print("Video Author: ",video.author)
print("Video Length:",video.length)
print("Video Duration: ",video.duration)
print("Video Likes:",video.likes)
print("Video Dislikes:",video.dislikes)
# print("Video Description:",video.description)
#best = video.getbest()
# print(best.resolution, best.extension)

# list available streams for a video:
streams = video.streams
print("List available streams for a video: ")
for s in streams:
    print(s.resolution, s.extension, s.get_filesize()) # , s.url --> get url, for download or streaming in mplayer / vlc etc:

print("Best Video Resolution: ",video.getbest().resolution, video.getbest().extension)

# get best resolution for a particular file format: (mp4, webm, flv or 3gp)

best = video.getbest(preftype="mp4")
print("Get best resolution for a particular file format: (mp4, webm, flv or 3gp): ", best.resolution, best.extension)

# Download video and show progress:
# print("Download video and show progress: ", best.download(quiet=False))

# Download video, use specific directory and/or filename:
# filename = best.download(filepath="tmp")
# filename = best.download(filepath="/tmp/Game." + best.extension)
# print(filename)

# Get audio-only streams (m4a and/or ogg vorbis):
audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())

# Download the 2nd audio stream from the above list:
# audiostreams[1].download()

# Get the best quality audio stream:
bestaudio = video.getbestaudio()
bestaudio.bitrate

# Download the best quality audio file:
bestaudio.download(filepath="audio")


###### show all media types for a video (video+audio, video-only and audio-only):

allstreams = video.allstreams
for s in allstreams:
    print(s.mediatype, s.extension, s.quality)