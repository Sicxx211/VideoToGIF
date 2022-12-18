# Video to GIF converter 



# Why I wrote the code 

I write this little app, in order for me to create funny gifs that I can send to my friends.I used the sys module to be able to pass 2 arguments inside the console, first one would be the actual file's name, and the second one what I would want to name the GIF.I decided to use sys module to have the ability to name files right in the console because otherwise I should've open the app in a text editor and edit the file name everytime.


# How I wrote the code 

#I used moviepy to be able to convert the file to gif <br>
#I used sys to be able to pass 2 arguments in the console <br>
from moviepy.editor import VideoFileClip <br>
import sys <br>
import os <br>
<br>
clip = sys.argv[1] #This is the first argument and is the mp4 file's name <br>
name = sys.argv[2] + '.gif' #This is the second argument, what you want to name the file and the extension  <br>
<br>
gifClip = VideoFileClip(clip) <br>
gifClip.write_gif(name) <br>
