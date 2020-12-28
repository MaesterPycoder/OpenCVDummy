# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip1 = VideoFileClip(r"C:\Users\S.S Shanmukkha\Desktop\video\1.mp4")

# getting subclip as video is large
clip2 = VideoFileClip(r"C:\Users\S.S Shanmukkha\Desktop\video\2.mp4")
clip3 = VideoFileClip(r"C:\Users\S.S Shanmukkha\Desktop\video\3.mp4")
clip4 = VideoFileClip(r"C:\Users\S.S Shanmukkha\Desktop\video\4.mp4")
# concatinating both the clips
final = concatenate_videoclips([clip1, clip2,clip3, clip4])

# showing final clip
final.ipython_display(width = 480)
