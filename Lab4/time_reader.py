import os
import time

dir_path = "C:/NUWEE/SECOND_TERM/TCS/Lab4/time_checker"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

while True:
    files = os.listdir(dir_path)
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "r") as f:
            content = f.read()
            print(file_name, content)
    time.sleep(5)
