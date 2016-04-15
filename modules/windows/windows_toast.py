from subprocess import call

def sendToast(message,
              time,
              ps_path=r".\modules\windows\send_toast_message.ps1"):
  call(["powershell.exe",
        "-noprofile",
        "-executionpolicy",
        "bypass",
        "-file",
        ps_path,
        "-message",
        message])

if __name__ == "__main__":
  send_toast("cat", 5, r".\send_toast_message.ps1")