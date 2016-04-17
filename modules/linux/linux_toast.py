from gi.repository import Notify

def sendToast(message, time):
  Notify.init("Posture Reminder")
  Notify.Notification.new(message).show()

  Notify.uninit()