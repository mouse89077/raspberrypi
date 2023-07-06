import time
from datetime import datetime
import os

FILEPATH= os.path.join(os.path.expanduser('~'), 'pygpsclient', 'data.txt')

now = datetime.now()

data = ""

#if not os.path.exists(FILEPATH):
    

for i in range(128):
    time.sleep(1)
    data = str(i)+"/"+str(now.microsecond)
    print(i)
    while True:
        try:
            f=open(FILEPATH, 'w')
            f.write(data)
            f.close
            break
        except:
            print('error')

