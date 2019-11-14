import subprocess, time, sys

g1 = """Device #1 IDCODE is 020F30DD
configuring SRAM device(s)...
DONE
Exit code = 0... Success
[RPi] closed JTAG"""

g2 = """Device #1 is EPCS16
erasing ASC device(s) in sector mode...
programming ASC device(s) in sector mode...
CRC verify ASC device(s) in sector mode...
DONE
Exit code = 0... Success
[RPi] closed JTAG"""

g3 = """configuring SRAM device(s)...
DONE
Exit code = 0... Success
[RPi] closed JTAG"""


def prred(s):
  print "\033[91m{}\033[00m".format(s)

def prgreen(s):
  print "\033[92m{}\033[00m".format(s)

## Configure
def DoTest():
  tries = 3
  fail = True
  for i in range(0,tries):
    print "INFO: Initial configure",i
    s = subprocess.check_output(["sudo","./jam","-aconfigure","hl2jic.jam"])
    print s
    s = s.strip()
    s = s[-len(g1):]
    if s == g1:
      fail = False
      break
    time.sleep(1.0)

  if fail: return fail
  prgreen("SUCCESS: Initial configure")

  ## Program
  fail = True
  for i in range(0,tries):
    print "INFO: Program",i
    s = subprocess.check_output(["sudo","./jam","-aprogram","hl2jic.jam"])
    print s
    s = s.strip()
    s = s[-len(g2):]
    if s == g2:
      fail = False
      break
    time.sleep(1.0)

  if fail: return fail   
  prgreen("SUCCESS: Program")

  ## Program
  ##fail = True
  ##for i in range(0,tries):
  ##  print "INFO: Final configure",i
  ##  s = subprocess.check_output(["sudo","./jam","-aconfigure","hl2sof.jam"])
  ##  print s
  ##  s = s.strip()
  ##  s = s[-len(g3):]
  ##  if s == g3:
  ##    fail = False
  ##    break
  ##  time.sleep(1.0)
    
  ##if fail: return fail
  ##prgreen("SUCCESS: Final configure")
  ##return fail

if DoTest():
  prred("#########################################")
  prred("# FAILURE: Check cabling and try again! #")
  prred("#########################################")
else:
  prgreen("#########################################")
  prgreen("# SUCCESS: Power cycle HL2 and test!    #")
  prgreen("#########################################")


  
## Keep window open
time.sleep(300.0)
sys.exit(0)

