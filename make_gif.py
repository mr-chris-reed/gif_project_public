"""
Steps:
1. Create virtual environment and activate it.
2. Run "python -m pip install -r requirements.txt
3. Take a short video with your phone and move it to the same workspace as this file.
4. Import moviepy.
5. Rotate clip with included code.
6. Resize clip to desired size - see "resize" from https://zulko.github.io/moviepy/gallery.html
7. Change speed of clip if desired - see "speedx" from https://zulko.github.io/moviepy/gallery.html
8. Add text on top of your clip using TextClip.
9. Generate your gif using "write_gif".
NOTE: Here is a good link that show how to use moviepy to generate gifs
https://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
"""

from moviepy.editor import *

"""
THIS MAY BE NEEDED TO ROTATE YOUR VIDEO:

# Manipulate video using moviepy.editor
# NOTE: May need to run the conditional if statement below if your video is
# a .mov file type and has been imported rotated.  Fix found at
# https://github.com/Zulko/moviepy/issues/586
if clip.rotation == 90:
    clip = clip.resize(clip.size[::-1])
    clip.rotation = 0
"""
