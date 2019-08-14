import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime, timedelta

import requests


class qr_scanner:
    check_times = dict()

    def __init__(self, video_stream, variable_queue_1):
        self.cap = video_stream
        self.variable_queue_1 = variable_queue_1

    def qr_scan_frame(self):
        _, frame = self.cap.read()

        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            scanned_name = str(obj.data)[2:-1]
            if scanned_name not in self.check_times:
                self.check_times[scanned_name] = datetime(2019, 1, 1)
            if datetime.now() - self.check_times[scanned_name] > timedelta(minutes=3):
                self.check_times[scanned_name] = datetime.now()
                url = "http://127.0.0.1:5000/telegram/user-query"

                payload = "{\"box_id\":\"" + scanned_name + "\"}"
                headers = {
                    'telegram_username': "kensim48",
                    'cache-control': "no-cache",
                    'Postman-Token': "2786c810-05c8-43cc-ab8b-13bb7c42793c"
                }

                response = requests.request("POST", url, data=payload, headers=headers)
                self.variable_queue_1.put(scanned_name)

        return cv2.resize(frame, (0, 0), fx=2.1, fy=2.1)
