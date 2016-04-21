from subprocess import call
import sys

def sendToast(message,
              time,
              ps_path=r".\modules\windows\send_toast_message.ps1"):
  if (sys.platform == "win32"):
    call(["powershell.exe",
          "-noprofile",
          "-executionpolicy",
          "bypass",
          "-file",
          ps_path,
          "-message",
          message])

if __name__ == "__main__":
  msg = ""

  for line in sys.stdin:
    msg += line

  sendToast(msg, 5, r".\send_toast_message.ps1")