import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

def remind_to_drink_water():
    while True:
        toaster.show_toast(
            "Hydration Reminder",
            "Time to drink some water!",
            duration=5
        )
        print("Notification sent!")
        time.sleep(10)

remind_to_drink_water()
