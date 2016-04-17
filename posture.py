#!/usr/bin/env python

import argparse
import re
import sys
import time
from modules.linux import linux_toast as linux
from modules.windows import windows_toast as windows

def main():
  desc = "A simple python script to remind you to fix your posture"
  parser = argparse.ArgumentParser(description=desc)

  # Optional Arguments (Flags)
  parser.add_argument(
    "-m",
    "--message",
    type=str,
    help="Set a custom message. Default is 'Fix your posture'",
    metavar="msg",
    default="Fix your posture"
  )

  parser.add_argument(
    "-d",
    "--message_time_delay",
    type=str,
    help=("Delay in between toast messages in the format 'mm:ss'."
          "Default is '30:00'"),
    metavar="mm:ss",
    default="30:00"
  )

  args = parser.parse_args()

  # Ensure time is of the form "mm...mm:ss" where the there is at least 1
  # number for the second and at least 1 number for the minute
  if (not re.match(r"\b\d+:[0-6]?\d", args.message_time_delay)):
    print("The time delay must be of the form 'mmm...mm:ss")
    print("\twhere there is at least 1 number for the minute and second")
    print("\twhere the first second digit, if 2 are present, is 1 through 6")
    print("\twhere only digits are used")

    exit(1)

  toast_function = None
  toast_message = args.message
  toast_time = 5
  second_delay = int(args.message_time_delay.split(":")[1])
  minute_delay = int(args.message_time_delay.split(":")[0])

  if (sys.platform.startswith("linux")):
    # The OS is a form of Linux
    toast_function = linux
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