import time
import ptvsd
ptvsd.enable_attach(('0.0.0.0', 3000))

while True:
    print ("123")
    time.sleep(2)
    