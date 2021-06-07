import time

def countdown(seconds):
    while seconds >= 5:
        print(seconds)
        seconds -= 1
        time.sleep(1)
