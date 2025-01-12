import datetime
from pathlib import Path

# get the last exec time in the file
date_last_exec = Path('last_exec.txt').read_text()
date_last_exec = datetime.datetime.strptime(date_last_exec, "%y %m %d %H %M %S")

date_now = datetime.datetime.now()

# Calculate the diff between now and the last
diff = date_now - date_last_exec

# Write the now in the last exec for the next exec
Path('last_exec.txt').write_text(date_now.strftime("%y %m %d %H %M %S"))