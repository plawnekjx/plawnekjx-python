import pprint

import plawnekjx

device = plawnekjx.get_usb_device()

deviceinfo = device.open_service("dtx:com.apple.instruments.server.services.deviceinfo")
response = deviceinfo.request({"method": "runningProcesses"})
pprint.pp(response)
