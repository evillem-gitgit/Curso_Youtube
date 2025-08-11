"""
DEu ruim pq não consegui baixar o arquivo ffmpeg
FFMPEG
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'