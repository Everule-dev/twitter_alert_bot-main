# monitor.py

import threading
import time
from twitter_api import get_tweet_count

class Monitor:
    def __init__(self):
        self.running = False
        self.thread = None

    def start(self, keyword, threshold, interval, log_func):
        self.running = True
        self.thread = threading.Thread(target=self._monitor, args=(keyword, threshold, interval, log_func))
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _monitor(self, keyword, threshold, interval, log_func):
        while self.running:
            count = get_tweet_count(keyword)
            log_func(f"{count} tweets found for '{keyword}'")

            if count >= threshold:
                log_func(f"⚠️ ALERT: '{keyword}' crossed the threshold of {threshold} tweets!")

            time.sleep(interval * 60)
