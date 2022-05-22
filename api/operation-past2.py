from logging import exception
import os
import youtube_dl
import re
import datetime
from .scale import *
from .time_selection import *


def audio_download(url):
    print("downloading audio......")
    import subprocess
    cmd='youtube-dl -g "{}"'.format(url)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal = subprocess_return.decode('utf-8')
    # print(normal)
    #get video url
    s=normal
    start = s.find("") + len("")
    end = s.find("\n")
    substring = s[start:end]
    # print("video url:")
    # print(substring)
    #joining new line with video url
    substring=substring+"\n"
    #get audio url
    start = s.find(substring) + len(substring)
    end = s.find("\n")+ len(s)
    substring = s[start:end]
    substring=substring[:-1]   #removing new line from end of the link
    # print("\nAudio url:----")
    # print("x"+substring+"x")
    #starting time
    h1=0
    m1=0
    s1=51
    #ending time
    h2=0
    m2=1
    s2=10
    #finding time difference(time2-time1)
    t1 = datetime.time(h1,m1,s1)
    t2 = datetime.time(h2,m2,s2)
    date = datetime.date(5, 5, 5)
    datetime1 = datetime.datetime.combine(date, t1)
    datetime2 = datetime.datetime.combine(date, t2)
    time_diff = datetime2 - datetime1
    # print(time_diff)
    starting_time=str(h1)+":"+str(m1)+":"+str(s1)
    #for downloading audio
    import subprocess
    l=substring
    cmd2='ffmpeg -ss {} -i "{}" -map a -to {} -c:a mp3 sample.mp3'.format(starting_time,l,time_diff)
    # os.system(cmd2)
    subprocess= subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal2 = subprocess_return.decode('utf-8')
    print(normal2)
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


def duration(url):
    import subprocess
    # url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
    cmd='youtube-dl --get-duration {}'.format(url)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal = subprocess_return.decode('utf-8')
    s=normal
    start = s.find("") + len("")
    end = s.find("\n")
    normal = s[start:end]
    print(normal)


def main_func(url):
    # url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
    audio='sample.mp3'
    title.text=""
    error_response.m=""
    main.s=""
    try:
        check_files()
        audio_download(url)
        main(audio)
        title(url)
        check_files()
    except Exception as e:
        # print(e)
        print("error occured and Retrying..")
        try:
            check_files()
            audio_download(url)
            main(audio)
            title(url)
            check_files()

        except Exception as e:
            # print(e)
            print("second time error")
            error_response()
            