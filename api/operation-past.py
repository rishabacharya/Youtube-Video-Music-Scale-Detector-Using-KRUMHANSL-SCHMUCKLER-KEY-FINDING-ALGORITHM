from logging import exception
import os
import youtube_dl
import re
import datetime

def audio_download(url):
    print("downloading audio......")
    print("hy")
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
    s1=30
    #ending time
    h2=0
    m2=1
    s2=00
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
    # cmd2='ffmpeg -ss 00:03:00 -i "{}" -map a -t 00:00:10 -c:a mp3 gog-vs-triv.mp3'.format(l)
    # os.system(cmd2)
    subprocess= subprocess.Popen(cmd2, shell=False, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal2 = subprocess_return.decode('utf-8')
    print(normal2)
    print("audio downloaded")

def file_conversion():
    print("converting file....")
    ##### mp3 to wav convertor
    from os import path
    from pydub import AudioSegment
    # files                                                                         
    src = "sample.mp3"
    dst = "sample.wav"
    # conversion                                                          
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    ##### wav to midi converter
    import subprocess
    wav_file="./sample.wav"
    cmd3="audio-to-midi {} -b 120 -t 30".format(wav_file)
    subprocess= subprocess.Popen(cmd3, shell=False, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    print("file converted")
    print("finding scale....")



def scale_finder():
    import music21
    score = music21.converter.parse('sample.wav.mid')
    key = score.analyze('key')
    # print(key.tonic.name, key.mode)
    scale=key.tonic.name+" "+key.mode
    # scale_finder.scale="xxxx"
    # scale="yyyyy"
    return scale
    

def transfer_data(url):
    #getting video title
    import subprocess
    cmd='youtube-dl --skip-download --get-title --no-warnings {} | sed 2d'.format(url)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring
    normal = subprocess_return.decode('utf-8')
    #data to be sent to frontend
    transfer_data.text="{} Video title: {}".format(scale_finder(),normal)
    print(transfer_data.text)

def trasnfer_data_error():
    print("Frontend: something went wrong, please try again")

def check_files(): 
    print("checking existing files(mp3,wav,mid) and removing them...")
    if (os.path.isfile('sample.mp3')):
        os.remove("sample.mp3")
    if (os.path.isfile('sample.wav')):  
        os.remove("sample.wav")
    if (os.path.isfile('sample.wav.mid')):
        os.remove("sample.wav.mid")
    print("checking files done.")

def main_process(url,flag):
    try:
        check_files()
        import timeit

        start = timeit.default_timer()
        audio_download(url)
        print("Vayo")
        # All the program statements
        stop = timeit.default_timer()
        execution_time = stop - start

        print("Program Executed in "+str(execution_time)) # It returns time in seconds
        file_conversion()
        scale_finder()
        transfer_data(url)
        check_files()
    except Exception as e:
        # print(e)
        if(flag==True):
            print("error occured and Retrying..")
            flag=False
            main_process(url,flag)

        else:
            print("second time error")
            trasnfer_data_error()

def main_func(url):
    # url="https://www.youtube.com/watch?v=uiqrngFTX5k"
    print("main function")
    flag=True
    main-process(url,flag)

    