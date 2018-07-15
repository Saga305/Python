import signal
import os

def handler(signum, frame):
    print("Alram Ended")
    os.kill(os.getpid(), signal.SIGKILL)

signal.signal(signal.SIGALRM, handler)
signal.alarm(10)
print("Alram started")

while True:
    pass