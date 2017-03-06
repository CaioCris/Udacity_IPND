import webbrowser
import time

total_breaks = 3
breaks_count = 0

while (breaks_count < total_breaks):
    print("This program started on"+time.ctime())
    time.sleep(25*60)
    url = "https://www.youtube.com/watch?v=exvAjY9_BuU"
    webbrowser.open(url)
    breaks_count += 1