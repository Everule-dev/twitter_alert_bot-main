# main.py

import tkinter as tk
from tkinter import scrolledtext
import threading
import time
from twitter_api import get_tweet_count

class TwitterBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Keyword Alert Bot")

        # Inputs
        tk.Label(root, text="Keyword:").grid(row=0, column=0, sticky="e")
        self.keyword_entry = tk.Entry(root, width=30)
        self.keyword_entry.grid(row=0, column=1)

        tk.Label(root, text="Tweet Count Threshold:").grid(row=1, column=0, sticky="e")
        self.threshold_entry = tk.Entry(root, width=30)
        self.threshold_entry.grid(row=1, column=1)

        tk.Label(root, text="Interval (mins):").grid(row=2, column=0, sticky="e")
        self.interval_entry = tk.Entry(root, width=30)
        self.interval_entry.grid(row=2, column=1)

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_monitoring)
        self.start_button.grid(row=3, column=0, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_monitoring, state=tk.DISABLED)
        self.stop_button.grid(row=3, column=1, pady=10)

        # Output log
        self.log_area = scrolledtext.ScrolledText(root, width=60, height=15)
        self.log_area.grid(row=4, column=0, columnspan=2)

        self.monitoring = False

    def log(self, message):
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.see(tk.END)

    def monitor_loop(self, keyword, threshold, interval):
        while self.monitoring:
            count = get_tweet_count(keyword)
            self.log(f"[{time.strftime('%H:%M:%S')}] {count} tweets for '{keyword}'")

            if count >= threshold:
                self.log(f"⚠️ ALERT: Keyword '{keyword}' exceeded threshold with {count} tweets!")

            time.sleep(interval * 60)

    def start_monitoring(self):
        keyword = self.keyword_entry.get()
        threshold = int(self.threshold_entry.get())
        interval = int(self.interval_entry.get())

        self.monitoring = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        threading.Thread(target=self.monitor_loop, args=(keyword, threshold, interval), daemon=True).start()

    def stop_monitoring(self):
        self.monitoring = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log("Stopped monitoring.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TwitterBotGUI(root)
    root.mainloop()
