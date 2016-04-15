# send_toast_message.ps1
#
# A simple powershell script to send a toast message to the desktop
#
# Example Usage:
# powershell.exe -noprofile -executionpolicy bypass -file .\test.ps1 -message "cat cat kitty cat"

param (
  [string]$message = "No message input",
  [int]$time_up = 5
)

# Ensure we see error messages
$ErrorActionPreference = "Continue"

# Load our message
$notificationTitle = $message

# Get Toast Template
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
$toast_template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText01)

# Convert toast template to xml template
$toast_xml = [xml] $toast_template.GetXml()
$toast_xml.GetElementsByTagName("text").AppendChild($toast_xml.CreateTextNode($notificationTitle)) > $null

# Convert our toast template back to WinRT type
$xml_doc = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml_doc.LoadXml($toast_xml.OuterXml)

# Create the toast message and load parameters. No tag or group seem to be
# needed.
$toast_message = [Windows.UI.Notifications.ToastNotification]::new($xml_doc)
$toast_message.ExpirationTime = [DateTimeOffset]::Now.AddSeconds($time_up)

# Create the notifier and send the message
$toast_notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PowerShell")
$toast_notifier.Show($toast_message);