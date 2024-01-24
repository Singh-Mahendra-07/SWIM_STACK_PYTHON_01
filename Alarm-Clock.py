import tkinter as tk
import time
import pygame
import pendulum

#set an alarm
def set_alarm():
    root.withdraw()  
    if is_24_h.get():
        alarm_h = h_spinbox.get()
    else:
        alarm_h = int(h_spinbox.get())
        if am_pm_var.get() == "PM":
            alarm_h += 12
    alarm_min = min_spinbox.get()

    selected_timezone = timezone_var.get()
    timezone = pendulum.timezone(selected_timezone)
    alarm_time = pendulum.now(timezone).replace(hour=int(alarm_h), minute=int(alarm_min), second=0, microsecond=0)

    while True:
        now = pendulum.now(timezone)
        if now >= alarm_time:
            show_alarm_window()
            break
        time.sleep(60)
#stop alarm
def stop_alarm():
    pygame.mixer.music.stop()
    global alarm_window
    alarm_window.destroy()

def snooze_alarm():
    pygame.mixer.music.stop()
    global alarm_window
    alarm_window.destroy()
    time.sleep(120)
    set_alarm()

def show_alarm_window():
    global alarm_window
    alarm_window = tk.Toplevel()
    alarm_window.title("Alarm!")
    alarm_window.geometry("300x100")

    stop_button = tk.Button(alarm_window, text="Stop", command=stop_alarm)
    stop_button.pack(pady=(20, 10))

    snooze_button = tk.Button(alarm_window, text="Snooze (2 mins)", command=snooze_alarm)
    snooze_button.pack(pady=10)

    pygame.mixer.init()
    pygame.mixer.music.load("-----") #ADD PATH OF MUSIC OR ALARM TUNE IN MP3 OR WAV FORMATE
    pygame.mixer.music.play()

root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("350x150")  

timezone_frame = tk.Frame(root)
timezone_frame.pack()

timezone_label = tk.Label(timezone_frame, text="Select Timezone:")
timezone_label.pack(side=tk.LEFT)

timezone_list = [ 'Asia/Kolkata', 'America/New_York', 'America/Los_Angeles', 'Europe/London', 'Asia/Tokyo']
timezone_var = tk.StringVar(root)
timezone_var.set(timezone_list[0])  

timezone_option = tk.OptionMenu(timezone_frame, timezone_var, *timezone_list)
timezone_option.pack(side=tk.LEFT)

format_frame = tk.Frame(root)
format_frame.pack()

is_24_h = tk.BooleanVar()
is_24_h.set(True)  

clock_format_check = tk.Checkbutton(format_frame, text="Use 24-hour format", variable=is_24_h, command=lambda: update_hour_spinbox())
clock_format_check.pack()

time_frame = tk.Frame(root)
time_frame.pack()

h_spinbox = tk.Spinbox(time_frame, from_=0, to=23, width=2)
h_spinbox.pack(side=tk.LEFT)
h_spinbox.delete(0, "end")
h_spinbox.insert(0, "00")  

min_spinbox = tk.Spinbox(time_frame, from_=0, to=59, width=2)
min_spinbox.pack(side=tk.LEFT)
min_spinbox.delete(0, "end")
min_spinbox.insert(0, "00")  

ampm_frame = tk.Frame(root)
ampm_frame.pack()

am_pm_var = tk.StringVar()
am_pm_var.set("AM")

am_pm_option = tk.OptionMenu(ampm_frame, am_pm_var, "AM", "PM")
am_pm_option.pack(side=tk.LEFT)

def update_hour_spinbox():
    if is_24_h.get():
        h_spinbox.config(from_=0, to=23)
        am_pm_option.pack_forget()  
    else:
        h_spinbox.config(from_=1, to=12)
        am_pm_option.pack()  

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()
