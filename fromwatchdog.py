import os
import sys
import time
import logging
import smtplib
import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    os.system('//fleet.ad/data/Data4/VMSSHARE/its/DOCS')


    print("found")
    # Defining your own path
    path = "//fleet.ad/data/Data4/VMSSHARE/its/DOCS"
    print("found")


    # Initilaize logging event handler
    event_handler = LoggingEventHandler()

    def on_create(event):
        print(f"{event.src_path} has been created")

    def on_move(event):
        print(f"{event.src_path} has been moved")


    LoggingEventHandler.on_create = on_create
    LoggingEventHandler.on_move = on_move

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()

    try:
        while True:
            if on_move > datetime.timestamp():
                # mal trigger
                EMAIL_ADDRESS = os.environ.get('USER_ID')
                EMAIL_PASSWORD = os.environ.get('USER_PASSWORD')

                # r= requests.get("https://fleet.my.salesforce.com", timeout=5)

                # if r.status_code!= 200:
                with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                    subject = 'ALARM: MAPILab is stuck from copying Public folders to destination'
                    body = 'Make sure server is restarted and it is backed up'
                    msg = f'Subject:{subject}\n\n{body}'

                    smtp.sendmail(EMAIL_ADDRESS, 'ryadav@elementcorp.com', msg)

            # set the thread sleep time
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()



