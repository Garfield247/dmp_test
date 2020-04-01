import nmap


nm = nmap.PortScanner()

ret = nm.scan("192.168.3.130","20-10000")


print(ret)

