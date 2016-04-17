# Posture Reminder

A simple program to send desktop toast notifications to remind you to fix your
posture.

### Usage

```
$ python posture.py --help
usage: posture.py [-h] [-m msg] [-d mm:ss]

A simple python script to remind you to fix your posture

optional arguments:
  -h, --help            show this help message and exit
  -m msg, --message msg
                        Custom message. Default is 'Fix your posture'
  -d mm:ss, --message_time_delay mm:ss
                        Delay in between toast messages in the format
                        'mm:ss'.Default is '30:00'
```

### Supported Operating Systems

- Windows (10)
- Linux (Ubuntu[14.04 LTS])