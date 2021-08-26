import os
import time

with open('starwars.txt', 'r') as sw_file:
    lines = sw_file.readlines()
    _index = 0

    for line in lines:
        if _index == 0:
            time_duration = int(line.strip())
            _index += 1
            continue

        if _index < 13:
            print(line, end='')
            _index += 1
        else:
            time.sleep(time_duration/10)
            os.system('clear')
            _index = 0
