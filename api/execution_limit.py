import time
def autofindt(url):
    print("execution limit autofindt")
    time.sleep(1)
    print("video length is 1:15:30")

def timer():
    import signal
    def signal_handler(signum, frame):
        raise Exception("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(5)   # Ten seconds


def function():
    try:
        time.sleep(6)
        timer()
        try:

            url="url"
            autofindt(url)
        except:
            print ("Video length is very long. Please enter desired time length.")
        print("next stpe after <=7 second")


    except:
        print("failed")

function()
# try:
#   findt(url)
# except Exception:
#   audio_download()
# 
# 
# 
