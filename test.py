import subprocess, time, sys

## Configure
def DoTest():
  time.sleep(2.0)

  subprocess.call(["./hl2setup","-v"])


DoTest()
## Keep window open
time.sleep(300.0)
sys.exit(0)

