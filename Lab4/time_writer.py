import os
import time

dir_path = "C:/NUWEE/SECOND_TERM/TCS/Lab4/time_checker"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

while True:
    file_path = os.path.join(dir_path, time.strftime("%Y%m%d_%H%M%S") + ".txt")
    with open(file_path, "w") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)
