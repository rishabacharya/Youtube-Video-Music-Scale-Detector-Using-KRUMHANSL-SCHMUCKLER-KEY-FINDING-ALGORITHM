



def video_duration(url):
    import subprocess
    import youtube_dl
    import re
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
    length="{}:{}:{}".format(h,m,s)
    return (length)
    





#duration separator
def time_diff(time1,time2):
    from collections import Counter
    import re
    # time1 = "10:1"
    counter = Counter(time1)
    c=counter[':']
    h1=0
    m1=0
    s1=0
    if c==0:
        #second
        s1=time1
    if c==1:
        s=time1
        #minute
        start = s.find("") + len("")
        end = s.find(":")
        m1 = s[start:end]
        #second
        start =len(m1+":")
        end = len(s)
        s1 = s[start:end]
    if c==2:
        s=time1
        #hour
        start=s.find("")+ len("")
        end = s.find(":")
        h1 = s[start:end]
        #minute
        pattern = "\:(.*?)\:"
        m1 = re.search(pattern, s).group(1)
        #second
        start =len(h1+":"+m1+":")
        end = len(s)
        s1 = s[start:end]
    # print(h1)
    # print(m1)    
    # print(s1)
    # time2 = "10:1"
    counter = Counter(time2)
    c=counter[':']
    h2=0
    m2=0
    s2=0
    if c==0:
        #second
        s2=time2
    if c==1:
        s=time2
        #minute
        start = s.find("") + len("")
        end = s.find(":")
        m2 = s[start:end]
        #second
        start =len(m2+":")
        end = len(s)
        s2 = s[start:end]
    if c==2:
        s=time2
        #hour
        start=s.find("")+ len("")
        end = s.find(":")
        h2 = s[start:end]
        #minute
        pattern = "\:(.*?)\:"
        m2 = re.search(pattern, s).group(1)
        #second
        start =len(h2+":"+m2+":")
        end = len(s)
        s2 = s[start:end]


    h1=int(h1)
    m1=int(m1)
    s1=int(s1)
    h2=int(h2)
    m2=int(m2)
    s2=int(s2)
    
    import datetime
    #finding time difference(time2-time1)
    t1 = datetime.time(h1,m1,s1)
    t2 = datetime.time(h2,m2,s2)
    date = datetime.date(5, 5, 5)
    datetime1 = datetime.datetime.combine(date, t1)
    datetime2 = datetime.datetime.combine(date, t2)
    # time_diff.diff=datetime2-datetime1
    if (datetime2 > datetime1) or (datetime2 == datetime1):
        return True
    else:
        return False

def time_diff_value(time1,time2):
    from collections import Counter
    import re
    # time1 = "10:1"
    counter = Counter(time1)
    c=counter[':']
    h1=0
    m1=0
    s1=0
    if c==0:
        #second
        s1=time1
    if c==1:
        s=time1
        #minute
        start = s.find("") + len("")
        end = s.find(":")
        m1 = s[start:end]
        #second
        start =len(m1+":")
        end = len(s)
        s1 = s[start:end]
    if c==2:
        s=time1
        #hour
        start=s.find("")+ len("")
        end = s.find(":")
        h1 = s[start:end]
        #minute
        pattern = "\:(.*?)\:"
        m1 = re.search(pattern, s).group(1)
        #second
        start =len(h1+":"+m1+":")
        end = len(s)
        s1 = s[start:end]
    # print(h1)
    # print(m1)    
    # print(s1)
    # time2 = "10:1"
    counter = Counter(time2)
    c=counter[':']
    h2=0
    m2=0
    s2=0
    if c==0:
        #second
        s2=time2
    if c==1:
        s=time2
        #minute
        start = s.find("") + len("")
        end = s.find(":")
        m2 = s[start:end]
        #second
        start =len(m2+":")
        end = len(s)
        s2 = s[start:end]
    if c==2:
        s=time2
        #hour
        start=s.find("")+ len("")
        end = s.find(":")
        h2 = s[start:end]
        #minute
        pattern = "\:(.*?)\:"
        m2 = re.search(pattern, s).group(1)
        #second
        start =len(h2+":"+m2+":")
        end = len(s)
        s2 = s[start:end]


    h1=int(h1)
    m1=int(m1)
    s1=int(s1)
    h2=int(h2)
    m2=int(m2)
    s2=int(s2)
    
    import datetime
    #finding time difference(time2-time1)
    t1 = datetime.time(h1,m1,s1)
    t2 = datetime.time(h2,m2,s2)
    date = datetime.date(5, 5, 5)
    datetime1 = datetime.datetime.combine(date, t1)
    datetime2 = datetime.datetime.combine(date, t2)
    return (datetime2-datetime1)


def findt(url,starting_time,ending_time):
    
    try:
        video_length=video_duration(url)
        # vl_st=time_diff_value(starting_time, video_length)
        # s_v=time_diff(video_length,starting_time)
        v_s=time_diff(starting_time,video_length)
        # e_v=time_diff(video_length,ending_time)
        # s_e=time_diff(ending_time,starting_time)
        e_s=time_diff(starting_time,ending_time)
        v_e=time_diff(ending_time,video_length)
        et_st=time_diff_value(starting_time,ending_time)
        if ((v_s and v_e) and e_s):
            to=et_st
            return (to)
        else:
            to=""
            findt.text="(Invalid time selected)"
            return to   
    except:
        to=""
        findt.text="(error in time selection)"
        return to

def autofindt(url):
    t1="0:00:30"
    t2="0:01:15"
    t3="0:02:15"
    v=video_duration(url)
    s1="0:00:00"
    s2="0:00:45"
    t1_v=time_diff(v,t1)
    v_t3=time_diff(t3,v)
    if t1_v:
        autofindt.s=s1
        autofindt.to=v
    if v_t3:
        autofindt.s=s2
        autofindt.to=t1
    else:
        autofindt.s=s1
        autofindt.to=t1

def link_validity(url):
    c="https://www.youtube.com/watch?v="
    if c in url:
        return True
    else:
        return False

def time_validation(starting_time,ending_time):
    c="::"
    z="0:0:0"
    if (c in starting_time) or (c in ending_time) or (z in ending_time):
        return False
    else:
        return True

def main_function():

    url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
    time1="0:0:40"
    time2="0:4:11"
    # print(time_diff_value(time1,time2))
    # print(video_duration(url))
    to=findt(time1,time2,url)
    if to != "":
        print(to)
    else:
        print("Something went wrong in given time duration")
    autofindt(url)
    print("stating time",autofindt.s,"to", autofindt.to)

# main_function()

