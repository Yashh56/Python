from plyer import notification
import time

Repeat_Interval= 10
while True:
    notification.notify(
        title = 'Reminder',
        message = 'Hey YaSh Drink Water Buddy!!',
        app_icon = None,
        timeout = 10,
    )
    time.sleep(Repeat_Interval)
    