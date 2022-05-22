# def scale_finder():
#     y="R scale"
#     return y

# def transfer_data():
#     title="title"
#     transfer_data.text="{}".format(title)

# def main1():
#     scale_finder()
#     transfer_data()

# transfer_data.text=""
# main1()
# msg=transfer_data.text
# print(msg)





import youtube_dl
import re

def video_duration(url):
    import subprocess
    cmd='youtube-dl --get-duration {}'.format(url)
    subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    # normalstring 
    normal = subprocess_return.decode('utf-8')

    #duration separator
    from collections import Counter
    str = normal[:-1]
    counter = Counter(str)
    c=counter[':']
    h=0
    m=0
    s=0
    x=0
    if c==0:
        #second
        s=str
    if c==1:
        s=str
        #minute
        start = s.find("") + len("")
        end = s.find(":")
        m = s[start:end]
        #second
        start =len(m+":")
        end = len(s)
        s = s[start:end]
    if c==2:
        s=str
        #hour
        start=s.find("")+ len("")
        end = s.find(":")
        h = s[start:end]
        #minute
        pattern = "\:(.*?)\:"
        m = re.search(pattern, s).group(1)
        #second
        start =len(h+":"+m+":")
        end = len(s)
        s = s[start:end]
    video_duration.h=h
    video_duration.m=m
    video_duration.s=s
    # print(h)
    # print(m)   
    # print(s)

def extract_duration(str):
    s=str
    #hour
    start=s.find("")+ len("")
    end = s.find(":")
    h = s[start:end]
    #minute
    pattern = "\:(.*?)\:"
    m = re.search(pattern, s).group(1)
    #second
    start =len(h+":"+m+":")
    end = len(s)
    s = s[start:end]
    if h=="":
        h=0
    if m=="":
        m=0
    if s=="":
        s=0

    extract_duration.h=h
    extract_duration.m=m
    extract_duration.s=s

    # print(extract_duration.h)
    # print(m)   
    # print(s)
def time_diff_validity(h1,m1,s1,h2,m2,s2):
    import datetime
    #finding time difference(time2-time1)
    t1 = datetime.time(h1,m1,s1)
    t2 = datetime.time(h2,m2,s2)
    date = datetime.date(5, 5, 5)
    datetime1 = datetime.datetime.combine(date, t1)
    datetime2 = datetime.datetime.combine(date, t2)
    if (datetime2 > datetime1):
        return True
    else:
        return False



def time_diff(h1,m1,s1,h2,m2,s2):
    import datetime
    #finding time difference(time2-time1)
    t1 = datetime.time(h1,m1,s1)
    t2 = datetime.time(h2,m2,s2)
    date = datetime.date(5, 5, 5)
    datetime1 = datetime.datetime.combine(date, t1)
    datetime2 = datetime.datetime.combine(date, t2)
    diff = datetime2 - datetime1
    return diff

def time_analyze(vl_h,vl_m,vl_s,st_h,st_m,st_s,et_h,et_m,et_s):
    if time_diff_validity(vl_h,vl_m,vl_s,st_h,st_m,st_s):
        time_analyze.msg="Starting time greater than video length"
    if time_diff_validity(vl_h,vl_m,vl_s,et_h,et_m,et_s) and time_diff_validity(st_h,st_m,st_s,vl_h,vl_m,vl_s):
        time_analyze.msg="Ending time greater than video length"
        vl=time_diff(st_h,st_m,st_s,vl_h,vl_m,vl_s)
        extract_duration(vl)
        # if time_diff_validity(0,0,31,extract_duration.h,extract_duration)



# url="https://www.youtube.com/watch?v=yR_8_K8CvUw"
# # url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
# video_duration(url)
# str="5:4:3"
# extract_duration(str)
# print(video_duration.h)
# print(extract_duration.h)