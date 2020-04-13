import nmap
import json


nm = nmap.PortScannerAsync()

ret = nm.scan("192.168.3.130","20-10000")
# j = json.loads(ret)
# print(j)
print(ret)
