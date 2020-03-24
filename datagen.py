import os
import time
import glob
import datetime
from datetime import datetime, timedelta

tCurrent = time.time()
while True:
    time.sleep(10) # sleep for 250 milliseconds
    if time.time() >= tCurrent + 1:
        newfile = open("/filelocationhere"+datetime.today().strftime("%Y-%m-%d-%H-%M-%S"), "wb")
        newfile.write (os.urandom(50000))    # generate random content
        newfile.close ()
        d = datetime.today() - timedelta(hours=0, minutes=1) #time interval to clean up files
        delete_files = glob.glob('c/filelocationher'+d.strftime("%Y-%m-%d-%H-%M")+'*', recursive=True)
        tCurrent = time.time()
        print(delete_files)
        for file in delete_files:
            try:
                os.remove(file)
            except OSError:
                print("Error while deleting file")
