import sys

if (sys.platform.startswith("linux")):
  from gi.repository import Notify

def sendToast(message, time):
  if (sys.platform.startswith("linux")):
    Notify.init("Posture Reminder")
    Notify.Notification.new(message).show()

    Notify.uninit()

if __name__ == "__main__":
  msg = ""

  for line in sys.stdin:
    msg += line

  sendToast(msg, 5)