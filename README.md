# SWIM_STACK_PYTHON_01
SIMPLE ALARM CLOCK

This Python program is a simple alarm clock application.

**Required Libraries:**
1. `tkinter`: Used for creating the GUI of the application.
2. `time`: Used for time-related functions.
3. `pygame`: Used for playing the alarm sound.  #“I am using pygame instead of playsound because I encountered a ModuleNotFoundError on my PC.”
4. `pendulum`: Used for handling timezones.

**Required Files:**
You need to have a sound file (in .mp3 or .wav format) that will be used as the alarm sound. The path of this file should be specified in the `pygame.mixer.music.load("-----")` line of the `show_alarm_window()` function.

**Functionality:**
- The program creates a simple GUI where the user can set an alarm for a specific time and timezone.
- The user can choose whether to use a 24-hour format or a 12-hour format for setting the alarm.
- When the set time is reached, a new window pops up with the alarm sound playing.
- The user can choose to stop the alarm or snooze it for 2 minutes.

**Functions:**
- `set_alarm()`: Sets the alarm based on the user's input and checks every minute if the current time has reached the alarm time.
- `stop_alarm()`: Stops the alarm sound and closes the alarm window.
- `snooze_alarm()`: Stops the alarm sound, closes the alarm window, and sets a new alarm 2 minutes later.
- `show_alarm_window()`: Creates a new window that plays the alarm sound and gives the user the option to stop or snooze the alarm.
- `update_hour_spinbox()`: Updates the hour spinbox based on whether the user chooses to use a 24-hour format or a 12-hour format.

Please ensure that you have the required libraries installed. You can install them using pip:
```
pip install tkinter pygame pendulum
```
Remember to replace `"-----"` with the path to your sound file in the `show_alarm_window()` function. The sound file should be in .mp3 format.
