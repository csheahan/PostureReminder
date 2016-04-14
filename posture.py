import sys

def main():
  if (sys.platform.startswith("linux")):
    # The OS is a form of Linux
    print("Linux")
  elif (sys.platform == "darwin"):
    # The OS is a form of MAC OS X
    print("MAC")
  elif (sys.platform == "win32"):
    # The OS is a form of Windows
    print("Windows")
  else:
    # The OS could not be detected, print and quit
    print("OS unable to be found")

if __name__ == "__main__":
  main()