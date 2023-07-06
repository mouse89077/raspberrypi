import time
from datetime import datetime
import os


#now = datetime.now()


data=""

cache=[]



while True:
    while True:
        try:
            f = open(FILEPATH, 'r')
            data=f.read()
            f.close
            break
        except:
            print('error')
    cache=data.split('/')
    now=time.time()*1000
    #if (now-float(cache[2]))<=100:
    #    print(data)
    #print(data)
    lat=float(cache[0])
    lon=float(cache[1])
    print(cache[0]+'and'+cache[1])
    print(str(lat) + 'and' + str(lon))
    time.sleep(0.1)
