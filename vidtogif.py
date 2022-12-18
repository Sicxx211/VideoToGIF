#I used moviepy to be able to convert the file to gif
#I used sys to be able to pass 2 arguments in the console
from moviepy.editor import VideoFileClip
import sys
import os

clip = sys.argv[1] #This is the first argument and is the mp4 file's name
name = sys.argv[2] + '.gif' #This is the second argument, what you want to name the file and the extension

gifClip = VideoFileClip(clip)
gifClip.write_gif(name)