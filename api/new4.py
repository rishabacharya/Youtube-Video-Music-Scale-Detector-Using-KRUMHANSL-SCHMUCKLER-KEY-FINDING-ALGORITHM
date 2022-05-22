# def link_validity(url):
#     c="https://www.youtube.com/watch?v="
#     if c in url:
#         print("valid")
#     else:
#         print("Invalid")

# url="https://www.youtube.com/watch?v=jHNNMj5bNQw"
# link_validity(url)




def time_validation(starting_time,ending_time):
    c="::"
    if (c in starting_time) or (c in ending_time):
        return True
    else:
        return False
# print(time_validation("::","::"))

# import re
def finds(link):
    s=link
    a="watch"
    start = s.find(a)
    if start== -1:
        linkb=link+"\n"
        s=linkb
        substringb="https://youtu.be/"
        start = s.find(substringb) + len(substringb)
        ss=s.find(substringb)
        # print(ss)
        end = s.find("\n")+len("")
        laststring = s[start:end]

        link="https://www.youtube.com/watch?v="+laststring
    print(link)
# finds("https://youtu.be/123")
# finds("https://www.youtube.com/watch?v=123")
# x=-1
# y=-1
# link="fuihfuh"
# p=link.find("https;//www.youtube.com/")
# q=link.find("https;//youtu.be/")
# # start = s.find(a)
# if (p == -1) and (q == -1):
#     print("printed when both false")