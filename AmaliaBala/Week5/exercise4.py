#display the current time function
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S") # the strftime is a function which displays the date in a very easy readable way


print("Current time:", current_time) # the time would be in the format hour : minutes : seconds
