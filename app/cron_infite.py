import time
import os

main_script = os.path.dirname(__file__) + "/compute_controller_modified.py"

for i in range(1,100):
    os.system("python3 " + main_script)
    time.sleep(4)
    