from datetime import datetime


# Function get datetime today
def get_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
