# A program to calculate what time I need to clock out on Friday to avoid OT.

import logging
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

logging.disable(logging.CRITICAL)

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Start of program")

# Store hours worked at start of day Friday as float and calculate hours remaining.
hoursWorked = float(
    input("How many hours are on your timesheet at the start of the day?\n")
)
logging.debug(f"hoursWorked is {hoursWorked}")
logging.debug(f"hoursWorked type is {type(hoursWorked)}")
hoursRemaining = 40 - hoursWorked
logging.debug(f"hoursRemaining is {hoursRemaining}")
logging.debug(f"hoursRemaining type is {type(hoursRemaining)}")

# Store clock-in time on Friday morning as datetime object.
clockInTime = input("What time did you clock in?\n").split(":")
logging.debug(f"clockInTime is {clockInTime}")
logging.debug(f"clockInTime type is {type(clockInTime)}")
dtClockTime = datetime(
    year=datetime.now().year,
    month=datetime.now().month,
    day=datetime.now().day,
    hour=int(clockInTime[0]),
    minute=int(clockInTime[1]),
    second=00,
)
logging.debug(f"dtClockTime is {dtClockTime}")

# Calculate number of hours needed to work to get 40 hours in the week, assuming a 30 minute lunch break.
clockOutTime = dtClockTime + timedelta(minutes=((hoursRemaining * 60) + 30))
logging.debug(f"clockOutTime is {clockOutTime}")

tk.messagebox.showinfo(
    "Clock Out Time", f"You need to clock out at {clockOutTime.time()}."
)
