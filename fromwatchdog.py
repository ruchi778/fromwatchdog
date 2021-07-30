import os
import sys
import time
import datetime


def watchDog():
    try:
        os.system('//fleet.ad/data/Data4/VMSSHARE/its/DOCS')
        ta = time.time()
        ta = datetime.datetime.fromtimestamp(ta)
        print(ta)
        tm = os.path.getmtime("//fleet.ad/data/Data4/VMSSHARE/its/DOCS")
        print(tm)
        tm = datetime.datetime.fromtimestamp(tm)
        print(tm)
        time_diff = ta.minute - tm.minute
        print(ta.minute - tm.minute)
        if time_diff > 20:
            import win32com.client as client
            outlook = client.Dispatch("Outlook.Application")
            message = outlook.CreateItem(0)
            message.Display()
            message.To = "DMange@elementcorp.com"
            message.CC = "ryadav@elementcorp.com"
            message.Subject = " Email Alert"
            message.Body = " Files are not generating in shared folder"
            # message.SentOnBehafOfName = "ryadav@elementcorp.com"
            message.Save()
            message.Send()
            time.sleep(600)
    except OSError:
        print("File is not accessible")
        time.sleep(10)

        # Defining your own path
        path = "//fleet.ad/data/Data4/VMSSHARE/its/DOCS"
        print("found")


a = 0
try:
    while (__name__ == '__main__'):
        watchDog()
        #a += 1
except KeyboardInterrupt:
    print('terminate')
    pass
