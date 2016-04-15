import sys
import time
from modules.windows import windows_toast as windows

def main():
  toast_function = None
  toast_message = "Fix your posture"
  toast_time = 5
  second_delay = 0
  minute_delay = 30

  if (sys.platform.startswith("linux")):
    # The OS is a form of Linux
    print("Linux")
  elif (sys.platform == "darwin"):
    # The OS is a form of MAC OS X
    print("MAC")
  elif (sys.platform == "win32"):
    # The OS is a form of Windows
    toast_function = windows
  else:
    # The OS could not be detected, print and quit
    print("OS unable to be found")

  while (toast_function is not None):
    toast_function.sendToast(toast_message, toast_time)

    time.sleep(second_delay + 60 * minute_delay)

if __name__ == "__main__":
  main()