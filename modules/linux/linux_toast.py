def sendToast(message, time):
  from gi.repository import Notify
  Notify.init("Posture Reminder")
  Notify.Notification.new(message).show()

  Notify.uninit()