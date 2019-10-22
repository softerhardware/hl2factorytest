import subprocess, time, sys

s = subprocess.check_output(["git","pull"])
print s
time.sleep(15.0)
sys.exit(0)

