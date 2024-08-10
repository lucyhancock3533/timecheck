from math import floor
from tkinter import *
from tkinter import messagebox
import ntplib


def run():
    ntp_client = ntplib.NTPClient()
    ntp_res = ntp_client.request('uk.pool.ntp.org', version=3)

    time_delta = ntp_res.offset
    print(f"System time differs from remote time by {time_delta}s")
    root = Tk()
    root.withdraw()
    if 0 < floor(time_delta) < 30:
        messagebox.showwarning('TimeCheck', f"System time differs from remote time by {round(time_delta, 2)}s")
    elif floor(time_delta) >= 30:
        messagebox.showerror('TimeCheck', f"System time differs from remote time by {round(time_delta, 2)}s")
    else:
        messagebox.showinfo('TimeCheck', f"System time accurate, difference {round(time_delta, 2)}s")


if __name__ == "__main__":
    run()
