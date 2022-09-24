#!/usr/bin/python3
#taha-shaikhh 
import socket
import sys
from datetime import datetime


if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1])
else: 
	print("Enter valid syntax")


print("*"*50)
print("scanning"+target)
print("time started:"+str(datetime.now()))
print("*"*50)

try:
	for port in range(40,1000):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print(f"Checking Port{port}")
		if result==0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname cannot be resolved")
	sys.exit()
	
except socket.error:
	print("couldn't connect to server")
	sys.exit()		