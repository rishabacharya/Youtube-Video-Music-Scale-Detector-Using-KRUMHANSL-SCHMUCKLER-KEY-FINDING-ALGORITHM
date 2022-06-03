from logging import exception
import os
import youtube_dl
import re
import datetime
from .scale import *
from .time_selection import *


def audio_download(url,starting_time,time_diff):
    print("downloading audio......")
    import subprocess
    #cmd='youtube-dl -x --audio-format mp3 -g "{}"'.format(url)
    #cmd='youtube-dl -g "{}"'.format(url)
    cmd='yt-dlp --external-downloader ffmpeg --external-downloader-args "-ss {} -to {}" -x --audio-format mp3 -o "sample.mp3" "{}"'.format(starting_time,time_diff,url)
    #cmd=' youtube-dl --external-downloader ffmpeg --external-downloader-args "-ss {} -to {} -c:a mp3 sample.mp3".format(starting_time,time_diff) "{}"'.format
    #'ffmpeg -ss {} -i "{}" -map a -to {} -c:a mp3 sample.mp3'.format(starting_time,l,time_diff)
    print(cmd)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal = subprocess_return.decode('utf-8')
    print(normal)
    print("audio downloaded")

def check_files(): 
    print("checking existing sample.mp3 file and removing it...")
    if (os.path.isfile('sample.mp3')):
        os.remove("sample.mp3")

def title(url):
    #getting video title
    import subprocess
    cmd='youtube-dl --skip-download --get-title --no-warnings {} | sed 2d'.format(url)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring
    normal = subprocess_return.decode('utf-8')
    #data to be sent to frontend
    # p ="{} Video title: {}".format(,normal)
    title.text= normal
    print("video tile",normal)
    
def error_response():
     error_response.m="something went wrong, please try again."


# def duration(url):
#     import subprocess
#     # url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
#     cmd='youtube-dl --get-duration {}'.format(url)
#     subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#     subprocess_return = subprocess.stdout.read()
#     # normalstring 
#     normal = subprocess_return.decode('utf-8')
#     s=normal
#     start = s.find("") + len("")
#     end = s.find("\n")
#     normal = s[start:end]
#     print(normal)

def timer():
    import signal
    def signal_handler(signum, frame):
        raise Exception("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(20)   # Ten seconds

def main_process(url,start_time,end_time,flag):
    # url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
    audio='sample.mp3'
    title.text=""
    error_response.m=""
    main.s=""
    findt.text=""
    check_files()
    try:
        if start_time == "x":
            autofindt(url)
            print(autofindt.s,autofindt.to)
            audio_download(url,autofindt.s,autofindt.to)
        else:
            f=findt(url,start_time,end_time)
            print(f)
            if f != "":
                audio_download(url,start_time,f)
        main(audio)
        # title(url)
        check_files()
    except Exception as e:
        # print(e)
        if(flag==True):
            flag=False
            print("error occured and Retrying..")
            print(e)
            main_process(url,start_time,end_time,flag)
        else:
            print("second time error")
            error_response()
            

def main_func(url,start_time,end_time):
    flag=True
    main_process(url,start_time,end_time,flag)
            

