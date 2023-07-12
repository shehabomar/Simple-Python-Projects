"""
from pytube import YouTube
from sys import argv 

link = argv[1]
yt = YouTube(link)


print('Title: ', yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/home/omar/Downloads/DownloadedYoutube')
"""

#####################################
# the program is buggy and needs to be checked 
####################################
from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)
print('Title:', yt.title)
print('Views:', yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/home/omar/Downloads/DownloadedYoutube')
print("Download completed successfully.")

