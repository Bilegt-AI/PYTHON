# COUNTDOWN-TIMET.PY

import time
my_time=int(input("Enter The Time In Seconds: "))
for x in range(my_time,0,-1):
    seconds=x%60
    print(f"00:00:{seconds}")
    time.sleep(1)
print("TIME'S UP!")
