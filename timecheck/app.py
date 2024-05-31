from datetime import datetime, UTC
from requests import get
from tkinter import *
from tkinter import messagebox


def run():
    system_time = datetime.now(UTC)
    req_start = datetime.now()
    remote_time_resp = get('https://worldtimeapi.org/api/timezone/Etc/UTC')
    req_end = datetime.now()
    res = remote_time_resp.json()
    remote_time = datetime.fromisoformat(res['datetime'])
    print(f'Time request took {req_end - req_start}')
    if (req_end - req_start).seconds > 0:
        print("Time request took too long, results may be inaccurate")
    time_delta = remote_time - system_time
    req_time = req_end - req_start
    if req_time < time_delta:
        time_delta -= req_time
    else:
        print("System time diff lower than request time")
    print(f"System time differs from remote time by {time_delta}")
    root = Tk()
    root.withdraw()
    if 0 < time_delta.seconds < 30:
        messagebox.showwarning('TimeCheck', f"System time differs from remote time by {time_delta}")
    elif time_delta.seconds >= 30:
        messagebox.showerror('TimeCheck', f"System time differs from remote time by {time_delta}")
    else:
        messagebox.showinfo('TimeCheck', f"System time accurate, difference {time_delta}")


if __name__ == "__main__":
    run()
